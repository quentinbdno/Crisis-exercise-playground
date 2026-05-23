from rest_framework import viewsets

from ai_agents.models import AIAgent, LLMConnector
from ai_agents.serializers import AIAgentSerializer, LLMConnectorSerializer
from audit.services import audit


class LLMConnectorViewSet(viewsets.ModelViewSet):
    queryset = LLMConnector.objects.all()
    serializer_class = LLMConnectorSerializer


class AIAgentViewSet(viewsets.ModelViewSet):
    queryset = AIAgent.objects.select_related("llm_connector").prefetch_related("scenarios")
    serializer_class = AIAgentSerializer

    def perform_create(self, serializer):
        agent = serializer.save()
        audit("ai_agent.created", actor=self.request.user, resource=agent)
