# Generated by Django 3.1.7 on 2021-06-03 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car_rental_system', '0004_auto_20210526_1249'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='first_name',
            new_name='Employee_name',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='last_name',
        ),
    ]