# Generated by Django 5.0 on 2023-12-14 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mlfinalproject', '0005_remove_regressiontable_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='regressiontable',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
