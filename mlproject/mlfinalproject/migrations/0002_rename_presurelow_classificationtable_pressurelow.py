# Generated by Django 5.0 on 2023-12-12 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mlfinalproject', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classificationtable',
            old_name='presurelow',
            new_name='pressurelow',
        ),
    ]
