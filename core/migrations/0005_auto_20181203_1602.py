# Generated by Django 2.1.3 on 2018-12-03 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_comunion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comunion',
            old_name='nombre',
            new_name='nombreComunion',
        ),
    ]
