from rest_framework import serializers

from ai_agents.models import AIAgent, LLMConnector


class LLMConnectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = LLMConnector
        fields = "__all__"


class AIAgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AIAgent
        fields = "__all__"
