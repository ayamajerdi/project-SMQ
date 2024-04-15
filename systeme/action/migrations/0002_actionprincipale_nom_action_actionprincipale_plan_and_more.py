# Generated by Django 5.0.3 on 2024-04-14 19:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RH', '0020_clotureformation'),
        ('action', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='actionprincipale',
            name='nom_action',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='actionprincipale',
            name='plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='actions_plan', to='RH.planaction'),
        ),
        migrations.AddField(
            model_name='sousaction',
            name='nom_sous_action',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='actionprincipale',
            name='cause_action',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actions_cause', to='action.causeaction'),
        ),
        migrations.AlterField(
            model_name='actionprincipale',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_actions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='actionprincipale',
            name='gravite_action',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actions_gravite', to='action.graviteaction'),
        ),
        migrations.AlterField(
            model_name='actionprincipale',
            name='priorite_action',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actions_priorite', to='action.prioriteaction'),
        ),
        migrations.AlterField(
            model_name='actionprincipale',
            name='responsable_validation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actions_responsable_validation', to='RH.employe'),
        ),
        migrations.AlterField(
            model_name='actionprincipale',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actions_site', to='action.site'),
        ),
        migrations.AlterField(
            model_name='actionprincipale',
            name='source_action',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actions_source', to='action.sourceaction'),
        ),
        migrations.AlterField(
            model_name='actionprincipale',
            name='type_action',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actions_type', to='action.typeaction'),
        ),
        migrations.AlterField(
            model_name='actionprincipale',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_actions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='sousaction',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_sous_actions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='sousaction',
            name='gravite_action',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sous_actions_gravite', to='action.graviteaction'),
        ),
        migrations.AlterField(
            model_name='sousaction',
            name='priorite_action',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sous_actions_priorite', to='action.prioriteaction'),
        ),
        migrations.AlterField(
            model_name='sousaction',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_sous_actions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='ClotureAction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_cloture_action', models.CharField(default=None, max_length=100)),
                ('delai_cloture', models.DateField(null=True)),
                ('efficacite_action', models.CharField(max_length=100, null=True)),
                ('commentaire', models.TextField(null=True)),
                ('piece_jointe', models.FileField(blank=True, null=True, upload_to='pieces_jointes/')),
                ('created_at', models.DateTimeField(default=None, null=True)),
                ('updated_at', models.DateTimeField(default=None, null=True)),
                ('action_concerne', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clotures_actions', to='action.actionprincipale')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_clotures_actions', to=settings.AUTH_USER_MODEL)),
                ('responsable_cloture', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_clotures_actions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
