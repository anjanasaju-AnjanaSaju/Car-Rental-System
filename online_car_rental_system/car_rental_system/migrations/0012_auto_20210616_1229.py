# Generated by Django 3.1.7 on 2021-06-16 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_rental_system', '0011_auto_20210616_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='imgs',
            field=models.ImageField(blank=True, null=True, upload_to='Car'),
        ),
    ]
