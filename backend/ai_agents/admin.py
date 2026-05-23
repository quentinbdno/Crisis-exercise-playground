from django.contrib import admin

from ai_agents.models import AIAgent, LLMConnector

admin.site.register(AIAgent)
admin.site.register(LLMConnector)
