# Generated by Django 4.1.7 on 2023-04-02 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0012_hotel_hotel_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='roombooking',
            name='checked_out',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
