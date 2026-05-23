from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True
    dependencies = [
        ("exercises", "0001_initial"),
        ("iam", "0001_initial"),
        ("media_library", "0001_initial"),
        ("stimuli", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]
    operations = [
        migrations.CreateModel(
            name="Channel",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=160)),
                ("channel_type", models.CharField(choices=[("public", "Public"), ("private", "Private"), ("direct", "Direct")], default="public", max_length=24)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("crisis_cells", models.ManyToManyField(blank=True, related_name="channels", to="iam.crisiscell")),
                ("exercise", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="channels", to="exercises.exercise")),
                ("members", models.ManyToManyField(blank=True, related_name="channels", to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name="DirectMessage",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("exercise", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="direct_messages", to="exercises.exercise")),
                ("participants", models.ManyToManyField(related_name="direct_threads", to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name="Message",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("sender_label", models.CharField(blank=True, max_length=160)),
                ("body", models.TextField()),
                ("is_ai_generated", models.BooleanField(default=False)),
                ("pinned", models.BooleanField(default=False)),
                ("reactions", models.JSONField(blank=True, default=dict)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("attachments", models.ManyToManyField(blank=True, related_name="messages", to="media_library.attachment")),
                ("channel", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="messages", to="messaging.channel")),
                ("parent", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name="thread_replies", to="messaging.message")),
                ("sender", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ("stimulus", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to="stimuli.stimulus")),
            ],
            options={"ordering": ["created_at"]},
        ),
    ]
