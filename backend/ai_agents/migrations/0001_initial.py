from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True
    dependencies = [("scenarios", "0001_initial")]
    operations = [
        migrations.CreateModel(
            name="LLMConnector",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=160)),
                ("provider", models.CharField(choices=[("openai_compatible", "OpenAI-compatible"), ("ollama", "Ollama"), ("local", "Local")], max_length=32)),
                ("endpoint_url", models.URLField(blank=True)),
                ("api_key_reference", models.CharField(blank=True, max_length=240)),
                ("default_model", models.CharField(blank=True, max_length=160)),
                ("parameters", models.JSONField(blank=True, default=dict)),
                ("active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="AIAgent",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=160)),
                ("persona_markdown", models.TextField()),
                ("active", models.BooleanField(default=True)),
                ("behavior_settings", models.JSONField(blank=True, default=dict)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("llm_connector", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="agents", to="ai_agents.llmconnector")),
                ("scenarios", models.ManyToManyField(blank=True, related_name="ai_agents", to="scenarios.scenario")),
            ],
        ),
    ]
