from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True
    dependencies = [("scenarios", "0001_initial"), migrations.swappable_dependency(settings.AUTH_USER_MODEL)]
    operations = [
        migrations.CreateModel(
            name="Attachment",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=240)),
                ("file", models.FileField(upload_to="attachments/")),
                ("media_type", models.CharField(choices=[("image", "Image"), ("pdf", "PDF"), ("video", "Video"), ("document", "Document"), ("audio", "Audio"), ("other", "Other")], default="other", max_length=24)),
                ("mime_type", models.CharField(blank=True, max_length=120)),
                ("size_bytes", models.PositiveBigIntegerField(default=0)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("scenario", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name="attachments", to="scenarios.scenario")),
                ("uploaded_by", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        )
    ]
