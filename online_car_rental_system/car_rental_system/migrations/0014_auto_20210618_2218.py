# Generated by Django 3.1.7 on 2021-06-18 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_rental_system', '0013_auto_20210618_1213'),
    ]

    operations = [
        migrations.CreateModel(
            name='IssueCar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customername', models.CharField(max_length=100)),
                ('car_name', models.CharField(max_length=100)),
                ('car_company', models.CharField(max_length=100)),
                ('car_type', models.CharField(max_length=100)),
                ('car_color', models.CharField(max_length=100)),
                ('car_capacity', models.IntegerField()),
                ('car_number', models.CharField(max_length=50)),
                ('car_district', models.CharField(max_length=100)),
                ('Car_rent_per_day', models.IntegerField()),
                ('issuedate', models.DateField()),
                ('retuendate', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='IssueCars',
        ),
    ]
