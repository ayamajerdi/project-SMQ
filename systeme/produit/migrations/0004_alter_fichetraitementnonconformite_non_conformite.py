# Generated by Django 5.0.3 on 2024-04-22 11:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0003_delete_produit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fichetraitementnonconformite',
            name='non_conformite',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produit.nonconformite'),
        ),
    ]
