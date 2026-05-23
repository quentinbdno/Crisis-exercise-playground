from django.utils import timezone
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from audit.services import audit
from exercises.models import Exercise, StimulusDelivery
from exercises.serializers import ExerciseSerializer, StimulusDeliverySerializer
from exercises.tasks import deliver_stimulus


class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.select_related("scenario").prefetch_related("participants", "crisis_cells")
    serializer_class = ExerciseSerializer

    @action(detail=True, methods=["post"])
    def launch(self, request, pk=None):
        exercise = self.get_object()
        exercise.status = Exercise.Status.RUNNING
        exercise.starts_at = exercise.starts_at or timezone.now()
        exercise.save(update_fields=["status", "starts_at", "updated_at"])
        for stimulus in exercise.scenario.stimuli.all():
            delivery = StimulusDelivery.objects.create(exercise=exercise, stimulus=stimulus, status=StimulusDelivery.Status.SCHEDULED)
            deliver_stimulus.apply_async(args=[delivery.id], countdown=stimulus.planned_time_seconds)
        audit("exercise.launched", actor=request.user, resource=exercise, exercise=exercise, scenario=exercise.scenario)
        return Response(ExerciseSerializer(exercise).data)

    @action(detail=True, methods=["post"])
    def pause(self, request, pk=None):
        exercise = self.get_object()
        exercise.status = Exercise.Status.PAUSED
        exercise.save(update_fields=["status", "updated_at"])
        audit("exercise.paused", actor=request.user, resource=exercise, exercise=exercise, scenario=exercise.scenario)
        return Response(ExerciseSerializer(exercise).data)

    @action(detail=True, methods=["post"])
    def resume(self, request, pk=None):
        exercise = self.get_object()
        exercise.status = Exercise.Status.RUNNING
        exercise.save(update_fields=["status", "updated_at"])
        audit("exercise.resumed", actor=request.user, resource=exercise, exercise=exercise, scenario=exercise.scenario)
        return Response(ExerciseSerializer(exercise).data)

    @action(detail=True, methods=["post"])
    def accelerate(self, request, pk=None):
        exercise = self.get_object()
        exercise.timeline_speed = request.data.get("timeline_speed", exercise.timeline_speed)
        exercise.save(update_fields=["timeline_speed", "updated_at"])
        audit("exercise.timeline_accelerated", actor=request.user, resource=exercise, exercise=exercise, scenario=exercise.scenario)
        return Response(ExerciseSerializer(exercise).data)

    @action(detail=True, methods=["post"])
    def inject_stimulus(self, request, pk=None):
        exercise = self.get_object()
        delivery = StimulusDelivery.objects.create(
            exercise=exercise,
            stimulus_id=request.data["stimulus_id"],
            status=StimulusDelivery.Status.SCHEDULED,
        )
        deliver_stimulus.delay(delivery.id)
        audit("stimulus.manual_injection", actor=request.user, resource=delivery, exercise=exercise, scenario=exercise.scenario)
        return Response(StimulusDeliverySerializer(delivery).data)

    @action(detail=True, methods=["post"])
    def resend_stimulus(self, request, pk=None):
        exercise = self.get_object()
        delivery = StimulusDelivery.objects.create(
            exercise=exercise,
            stimulus_id=request.data["stimulus_id"],
            status=StimulusDelivery.Status.RESENT,
        )
        deliver_stimulus.delay(delivery.id)
        audit("stimulus.resent", actor=request.user, resource=delivery, exercise=exercise, scenario=exercise.scenario)
        return Response(StimulusDeliverySerializer(delivery).data)
