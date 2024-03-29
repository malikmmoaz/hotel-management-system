# Generated by Django 4.1.7 on 2023-03-26 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HotelApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=100)),
                ('hotel_address', models.CharField(max_length=100)),
                ('hotel_contact', models.CharField(max_length=100)),
                ('hotel_email', models.CharField(max_length=100)),
                ('hotel_description', models.CharField(max_length=100)),
                ('hotel_image', models.ImageField(upload_to='applications/<django.db.models.fields.CharField>')),
                ('hotel_status', models.BooleanField(default=False)),
            ],
        ),
    ]
