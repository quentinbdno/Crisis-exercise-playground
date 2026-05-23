from rest_framework import viewsets

from audit.services import audit
from stimuli.models import Stimulus
from stimuli.serializers import StimulusSerializer


class StimulusViewSet(viewsets.ModelViewSet):
    queryset = Stimulus.objects.select_related("scenario", "ai_agent").prefetch_related("attachments")
    serializer_class = StimulusSerializer

    def perform_create(self, serializer):
        stimulus = serializer.save()
        audit("stimulus.created", actor=self.request.user, resource=stimulus, scenario=stimulus.scenario)
