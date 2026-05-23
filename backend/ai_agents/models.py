from django.db import models


class LLMConnector(models.Model):
    class Provider(models.TextChoices):
        OPENAI_COMPATIBLE = "openai_compatible", "OpenAI-compatible"
        OLLAMA = "ollama", "Ollama"
        LOCAL = "local", "Local"

    name = models.CharField(max_length=160)
    provider = models.CharField(max_length=32, choices=Provider.choices)
    endpoint_url = models.URLField(blank=True)
    api_key_reference = models.CharField(max_length=240, blank=True)
    default_model = models.CharField(max_length=160, blank=True)
    parameters = models.JSONField(default=dict, blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class AIAgent(models.Model):
    name = models.CharField(max_length=160)
    persona_markdown = models.TextField()
    llm_connector = models.ForeignKey(LLMConnector, null=True, blank=True, on_delete=models.SET_NULL, related_name="agents")
    scenarios = models.ManyToManyField("scenarios.Scenario", blank=True, related_name="ai_agents")
    active = models.BooleanField(default=True)
    behavior_settings = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
