from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True
    dependencies = [
        ("ai_agents", "0001_initial"),
        ("media_library", "0001_initial"),
        ("scenarios", "0001_initial"),
    ]
    operations = [
        migrations.CreateModel(
            name="Stimulus",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("planned_time_seconds", models.PositiveIntegerField(default=0)),
                ("sender_label", models.CharField(max_length=160)),
                ("recipient_label", models.CharField(blank=True, max_length=240)),
                ("stimulus_type", models.CharField(choices=[("chat_message", "Chat message"), ("email", "Email"), ("fake_tweet", "Fake tweet"), ("fake_news", "Fake news"), ("voice_call", "Voice call"), ("system_notification", "System notification"), ("video", "Video"), ("attachment", "Attachment")], max_length=32)),
                ("delivery_channel", models.CharField(choices=[("public_channel", "Public channel"), ("private_channel", "Private channel"), ("direct_message", "Direct message"), ("email", "Email"), ("system", "System")], max_length=32)),
                ("subject", models.CharField(blank=True, max_length=240)),
                ("body", models.TextField(blank=True)),
                ("payload", models.JSONField(blank=True, default=dict)),
                ("order", models.PositiveIntegerField(default=0)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("ai_agent", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="stimuli", to="ai_agents.aiagent")),
                ("attachments", models.ManyToManyField(blank=True, related_name="stimuli", to="media_library.attachment")),
                ("scenario", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="stimuli", to="scenarios.scenario")),
            ],
            options={"ordering": ["planned_time_seconds", "order"]},
        )
    ]
