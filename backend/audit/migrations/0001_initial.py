from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True
    dependencies = [
        ("exercises", "0001_initial"),
        ("scenarios", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]
    operations = [
        migrations.CreateModel(
            name="AuditLog",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("action", models.CharField(max_length=160)),
                ("resource_type", models.CharField(blank=True, max_length=120)),
                ("resource_id", models.CharField(blank=True, max_length=80)),
                ("correlation_id", models.CharField(blank=True, max_length=120)),
                ("ip_address", models.GenericIPAddressField(blank=True, null=True)),
                ("metadata", models.JSONField(blank=True, default=dict)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("actor", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ("exercise", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to="exercises.exercise")),
                ("scenario", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to="scenarios.scenario")),
            ],
            options={"ordering": ["-created_at"]},
        )
    ]
