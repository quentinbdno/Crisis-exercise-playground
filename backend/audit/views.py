from rest_framework import viewsets

from audit.models import AuditLog
from audit.serializers import AuditLogSerializer


class AuditLogViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AuditLogSerializer

    def get_queryset(self):
        queryset = AuditLog.objects.select_related("actor", "exercise", "scenario")
        exercise_id = self.request.query_params.get("exercise")
        if exercise_id:
            queryset = queryset.filter(exercise_id=exercise_id)
        return queryset
