# Generated by Django 4.2.6 on 2023-11-09 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_rename_disponibilité_product_disponibilite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='disponibilite',
        ),
    ]
