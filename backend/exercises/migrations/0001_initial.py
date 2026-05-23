from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True
    dependencies = [
        ("iam", "0001_initial"),
        ("scenarios", "0001_initial"),
        ("stimuli", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]
    operations = [
        migrations.CreateModel(
            name="Exercise",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=200)),
                ("status", models.CharField(choices=[("draft", "Draft"), ("scheduled", "Scheduled"), ("running", "Running"), ("paused", "Paused"), ("completed", "Completed"), ("cancelled", "Cancelled")], default="draft", max_length=24)),
                ("starts_at", models.DateTimeField(blank=True, null=True)),
                ("ended_at", models.DateTimeField(blank=True, null=True)),
                ("timeline_speed", models.DecimalField(decimal_places=2, default=1, max_digits=5)),
                ("metadata", models.JSONField(blank=True, default=dict)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("crisis_cells", models.ManyToManyField(blank=True, related_name="exercises", to="iam.crisiscell")),
                ("participants", models.ManyToManyField(blank=True, related_name="exercises", to=settings.AUTH_USER_MODEL)),
                ("scenario", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="exercises", to="scenarios.scenario")),
            ],
        ),
        migrations.CreateModel(
            name="ExerciseRoom",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=160)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("crisis_cell", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to="iam.crisiscell")),
                ("exercise", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="rooms", to="exercises.exercise")),
            ],
        ),
        migrations.CreateModel(
            name="StimulusDelivery",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("status", models.CharField(choices=[("pending", "Pending"), ("scheduled", "Scheduled"), ("delivered", "Delivered"), ("failed", "Failed"), ("resent", "Resent")], default="pending", max_length=24)),
                ("scheduled_for", models.DateTimeField(blank=True, null=True)),
                ("delivered_at", models.DateTimeField(blank=True, null=True)),
                ("error", models.TextField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("exercise", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="stimulus_deliveries", to="exercises.exercise")),
                ("stimulus", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="deliveries", to="stimuli.stimulus")),
            ],
        ),
    ]
