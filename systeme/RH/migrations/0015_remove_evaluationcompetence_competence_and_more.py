# Generated by Django 5.0.3 on 2024-04-11 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RH', '0014_alter_ficheemployee_bank_account_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evaluationcompetence',
            name='competence',
        ),
        migrations.RemoveField(
            model_name='evaluationcompetence',
            name='niveau_acquis',
        ),
        migrations.AddField(
            model_name='evaluationcompetence',
            name='skills_acquis',
            field=models.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='evaluationcompetence',
            name='skills_requis',
            field=models.JSONField(default=dict),
        ),
        migrations.DeleteModel(
            name='Competence',
        ),
    ]
