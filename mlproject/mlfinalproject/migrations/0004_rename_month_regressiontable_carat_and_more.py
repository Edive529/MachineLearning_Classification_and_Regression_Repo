# Generated by Django 5.0 on 2023-12-13 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mlfinalproject', '0003_regressiontable'),
    ]

    operations = [
        migrations.RenameField(
            model_name='regressiontable',
            old_name='Month',
            new_name='carat',
        ),
        migrations.RenameField(
            model_name='regressiontable',
            old_name='Year',
            new_name='clarity',
        ),
        migrations.RenameField(
            model_name='regressiontable',
            old_name='cdi',
            new_name='color',
        ),
        migrations.RenameField(
            model_name='regressiontable',
            old_name='dmin',
            new_name='cut',
        ),
        migrations.RenameField(
            model_name='regressiontable',
            old_name='latitude',
            new_name='depth',
        ),
        migrations.RenameField(
            model_name='regressiontable',
            old_name='longitude',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='regressiontable',
            old_name='magnitude',
            new_name='table',
        ),
        migrations.RenameField(
            model_name='regressiontable',
            old_name='mmi',
            new_name='x',
        ),
        migrations.RenameField(
            model_name='regressiontable',
            old_name='sig',
            new_name='y',
        ),
        migrations.RenameField(
            model_name='regressiontable',
            old_name='tsunami',
            new_name='z',
        ),
    ]
