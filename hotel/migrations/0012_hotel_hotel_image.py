# Generated by Django 4.1.7 on 2023-04-02 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0011_remove_roombooking_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='hotel_image',
            field=models.FileField(null=True, upload_to='hotels/<django.db.models.fields.CharField>'),
        ),
    ]
