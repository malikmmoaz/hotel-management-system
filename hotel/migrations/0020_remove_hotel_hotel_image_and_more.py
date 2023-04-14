# Generated by Django 4.1.7 on 2023-04-14 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0019_hotel_hotel_manager'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='hotel_image',
        ),
        migrations.RemoveField(
            model_name='hotelapplication',
            name='hotel_image',
        ),
        migrations.AlterField(
            model_name='hotelimage',
            name='hotel_image',
            field=models.FileField(upload_to='hotels/hotel_images/'),
        ),
    ]
