from rest_framework import serializers

from scenarios.models import Scenario


class ScenarioSerializer(serializers.ModelSerializer):
    stimuli_count = serializers.IntegerField(read_only=True)
    media_count = serializers.IntegerField(read_only=True)
    linked_ai_agents = serializers.IntegerField(read_only=True)

    class Meta:
        model = Scenario
        fields = "__all__"
        read_only_fields = ["author", "created_at", "updated_at"]
