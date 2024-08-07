# Generated by Django 5.0.3 on 2024-03-31 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RH', '0009_alter_jobpost_created_at_alter_jobpost_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ficheemployee',
            name='address',
        ),
        migrations.RemoveField(
            model_name='ficheemployee',
            name='work_address',
        ),
        migrations.RemoveField(
            model_name='competence',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='competence',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='evaluationcompetence',
            name='competence',
        ),
        migrations.RemoveField(
            model_name='department',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='department',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='ficheemployee',
            name='department',
        ),
        migrations.RemoveField(
            model_name='employe',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='employe',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='employe',
        ),
        migrations.RemoveField(
            model_name='formation',
            name='responsable_validation',
        ),
        migrations.RemoveField(
            model_name='postefonction',
            name='relation_fonctionnelle',
        ),
        migrations.RemoveField(
            model_name='formation',
            name='participants',
        ),
        migrations.RemoveField(
            model_name='ficheemployee',
            name='manager',
        ),
        migrations.RemoveField(
            model_name='ficheemployee',
            name='employe_concerne',
        ),
        migrations.RemoveField(
            model_name='ficheemployee',
            name='coach',
        ),
        migrations.RemoveField(
            model_name='evaluationchaud',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='evaluationchaud',
            name='participant',
        ),
        migrations.RemoveField(
            model_name='evaluationchaud',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='evaluationcompetence',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='evaluationcompetence',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='planaction',
            name='evaluation',
        ),
        migrations.RemoveField(
            model_name='evaluationfroid',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='evaluationfroid',
            name='responsable_formation',
        ),
        migrations.RemoveField(
            model_name='evaluationfroid',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='ficheemployee',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='ficheemployee',
            name='job_position',
        ),
        migrations.RemoveField(
            model_name='ficheemployee',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='formation',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='formation',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='planaction',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='planaction',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='postefonction',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='postefonction',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='responsableformation',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='responsableformation',
            name='updated_by',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='Competence',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='Employe',
        ),
        migrations.DeleteModel(
            name='EvaluationChaud',
        ),
        migrations.DeleteModel(
            name='EvaluationCompetence',
        ),
        migrations.DeleteModel(
            name='EvaluationFroid',
        ),
        migrations.DeleteModel(
            name='FicheEmployee',
        ),
        migrations.DeleteModel(
            name='Formation',
        ),
        migrations.DeleteModel(
            name='Notification',
        ),
        migrations.DeleteModel(
            name='Participant',
        ),
        migrations.DeleteModel(
            name='PlanAction',
        ),
        migrations.DeleteModel(
            name='PosteFonction',
        ),
        migrations.DeleteModel(
            name='ResponsableFormation',
        ),
    ]
