from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]
    operations = [
        migrations.CreateModel(
            name="Permission",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("key", models.CharField(max_length=120, unique=True)),
                ("name", models.CharField(max_length=160)),
                ("description", models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="Role",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=120, unique=True)),
                ("description", models.TextField(blank=True)),
                ("inherits", models.ManyToManyField(blank=True, related_name="children", to="iam.role")),
                ("permissions", models.ManyToManyField(blank=True, related_name="roles", to="iam.permission")),
            ],
        ),
        migrations.CreateModel(
            name="CrisisCell",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=160)),
                ("description", models.TextField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("members", models.ManyToManyField(blank=True, related_name="crisis_cells", to=settings.AUTH_USER_MODEL)),
                ("roles", models.ManyToManyField(blank=True, related_name="crisis_cells", to="iam.role")),
            ],
        ),
        migrations.CreateModel(
            name="UserRoleAssignment",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("crisis_cell", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to="iam.crisiscell")),
                ("role", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="iam.role")),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="role_assignments", to=settings.AUTH_USER_MODEL)),
            ],
            options={"unique_together": {("user", "role", "crisis_cell")}},
        ),
    ]
