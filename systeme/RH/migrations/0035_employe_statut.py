# Generated by Django 5.0.3 on 2024-06-09 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RH', '0034_alter_evaluationcompetence_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='employe',
            name='statut',
            field=models.CharField(choices=[('En attente', 'En attente'), ('Validé', 'Validé'), ('Refusé', 'Refusé'), ('terminé', 'terminé')], default='En attente', max_length=20),
        ),
    ]