# Generated by Django 5.0.3 on 2024-04-07 13:55

import django.db.models.deletion
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indicateur', '0002_indicateur_created_at_indicateur_created_by_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AxePolitiqueQualite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TypeIndicateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TypeResultatAttendu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='indicateur',
            name='responsable_indicateur',
        ),
        migrations.AddField(
            model_name='indicateur',
            name='piece_jointe',
            field=models.FileField(blank=True, null=True, upload_to='pieces_jointes/'),
        ),
        migrations.AlterField(
            model_name='indicateur',
            name='axe_politique_qualite',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indicateur.axepolitiquequalite'),
        ),
        migrations.CreateModel(
            name='HistoricalSuiviIndicateur',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('frequence', models.CharField(max_length=100)),
                ('objectif', models.TextField()),
                ('limite_critique', models.DecimalField(decimal_places=2, max_digits=10)),
                ('resultat', models.DecimalField(decimal_places=2, max_digits=10)),
                ('commentaire', models.TextField()),
                ('piece_jointe', models.TextField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(default=None, null=True)),
                ('updated_at', models.DateTimeField(default=None, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('created_by', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('indicateur', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='indicateur.indicateur')),
                ('updated_by', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical suivi indicateur',
                'verbose_name_plural': 'historical suivi indicateurs',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.AlterField(
            model_name='indicateur',
            name='type_indicateur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indicateur.typeindicateur'),
        ),
        migrations.CreateModel(
            name='HistoricalIndicateur',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=None, null=True)),
                ('updated_at', models.DateTimeField(default=None, null=True)),
                ('libelle', models.CharField(max_length=255)),
                ('processus_lie', models.CharField(max_length=100)),
                ('date_debut', models.DateField()),
                ('periodicite_indicateur', models.CharField(choices=[('annuelle', 'Annuelle'), ('semestrielle', 'Semestrielle'), ('trimestrielle', 'Trimestrielle'), ('mensuelle', 'Mensuelle'), ('hebdomadaire', 'Hebdomadaire'), ('quotidienne', 'Quotidienne')], max_length=20)),
                ('type_suivi', models.CharField(choices=[('manuel', 'Manuel'), ('formule', 'Formule de calcul')], max_length=10)),
                ('valeur_cible', models.DecimalField(decimal_places=2, max_digits=10)),
                ('limite_critique', models.DecimalField(decimal_places=2, max_digits=10)),
                ('piece_jointe', models.TextField(blank=True, max_length=100, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('axe_politique_qualite', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='indicateur.axepolitiquequalite')),
                ('created_by', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('type_indicateur', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='indicateur.typeindicateur')),
                ('type_resultat_attendu', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='indicateur.typeresultatattendu')),
            ],
            options={
                'verbose_name': 'historical indicateur',
                'verbose_name_plural': 'historical indicateurs',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.AlterField(
            model_name='indicateur',
            name='type_resultat_attendu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indicateur.typeresultatattendu'),
        ),
    ]