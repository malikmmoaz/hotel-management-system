# Generated by Django 4.1.7 on 2023-04-04 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0016_roombooking_housekeeping_required'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotelapplication',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='hotelapplication',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
