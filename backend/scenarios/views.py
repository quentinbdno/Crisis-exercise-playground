from django.db.models import Count
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from audit.services import audit
from imports_exports.services import read_scenario_zip, scenario_to_csv, validate_scenario_yaml
from scenarios.models import Scenario
from scenarios.serializers import ScenarioSerializer


class ScenarioViewSet(viewsets.ModelViewSet):
    serializer_class = ScenarioSerializer

    def get_queryset(self):
        return Scenario.objects.annotate(
            stimuli_count=Count("stimuli", distinct=True),
            media_count=Count("attachments", distinct=True),
            linked_ai_agents=Count("ai_agents", distinct=True),
        )

    def perform_create(self, serializer):
        scenario = serializer.save(author=self.request.user)
        audit("scenario.created", actor=self.request.user, resource=scenario, scenario=scenario)

    @action(detail=True, methods=["post"])
    def duplicate(self, request, pk=None):
        source = self.get_object()
        copy = Scenario.objects.create(
            name=f"{source.name} Copy",
            description=source.description,
            author=request.user,
            metadata=source.metadata,
            version=source.version,
        )
        for stimulus in source.stimuli.all():
            stimulus.pk = None
            stimulus.scenario = copy
            stimulus.save()
        audit("scenario.duplicated", actor=request.user, resource=copy, scenario=copy, metadata={"source_id": source.id})
        return Response(ScenarioSerializer(copy).data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=["post"])
    def import_file(self, request):
        uploaded = request.FILES.get("file")
        if not uploaded:
            return Response({"errors": ["file is required"]}, status=status.HTTP_400_BAD_REQUEST)
        if uploaded.name.endswith(".zip"):
            data, errors = read_scenario_zip(uploaded)
        else:
            data, errors = validate_scenario_yaml(uploaded.read().decode("utf-8"))
        if errors:
            return Response({"errors": errors}, status=status.HTTP_400_BAD_REQUEST)
        scenario = Scenario.objects.create(name=data["name"], description=data.get("description", ""), author=request.user, metadata=data)
        audit("scenario.imported", actor=request.user, resource=scenario, scenario=scenario)
        return Response(ScenarioSerializer(scenario).data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=["get"])
    def export_csv(self, request, pk=None):
        scenario = self.get_object()
        return Response({"filename": f"{scenario.id}-stimuli.csv", "content": scenario_to_csv(scenario.stimuli.all())})
