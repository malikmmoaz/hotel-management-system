# Generated by Django 4.1.7 on 2023-04-02 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0008_rename_hotelbooking_roombooking'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotelapplication',
            name='hotel_manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hotel.hotelmanager'),
        ),
    ]
