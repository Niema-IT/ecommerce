# Generated by Django 4.2.6 on 2023-11-09 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_commande_total_alter_commande_pays'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='disponibilité',
            field=models.CharField(default=200, max_length=200),
            preserve_default=False,
        ),
    ]
