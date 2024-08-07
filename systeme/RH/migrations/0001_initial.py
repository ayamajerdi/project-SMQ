# Generated by Django 5.0.3 on 2024-03-27 16:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('main_mission', models.CharField(max_length=255)),
                ('required_skills', models.CharField(max_length=255)),
                ('main_activity', models.CharField(max_length=255)),
                ('pieces_jointes', models.FileField(blank=True, null=True, upload_to='pieces_jointes/')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='JobPost', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
