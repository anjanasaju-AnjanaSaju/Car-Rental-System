# Generated by Django 3.1.7 on 2021-05-20 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=100)),
                ('car_company', models.CharField(max_length=100)),
                ('car_type', models.CharField(max_length=100)),
                ('car_color', models.CharField(max_length=100)),
                ('car_capacity', models.IntegerField()),
                ('car_number', models.CharField(max_length=50)),
                ('car_fuel', models.CharField(max_length=100)),
                ('car_city', models.CharField(max_length=100)),
                ('car_district', models.CharField(max_length=100)),
                ('Car_rent_per_day', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CarBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer_name', models.CharField(max_length=100)),
                ('Customer_address', models.CharField(max_length=100)),
                ('Customer_phn_number', models.IntegerField()),
                ('car_name', models.CharField(max_length=100)),
                ('car_company', models.CharField(max_length=100)),
                ('car_type', models.CharField(max_length=100)),
                ('car_color', models.CharField(max_length=100)),
                ('car_capacity', models.IntegerField()),
                ('total_no_of_days', models.IntegerField()),
                ('total_amount', models.IntegerField()),
                ('advance_amount', models.IntegerField()),
                ('balance_amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('user_name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('email', models.CharField(max_length=50)),
                ('phone_number', models.IntegerField()),
                ('district', models.CharField(max_length=50)),
                ('booking_date', models.DateField()),
                ('total_no_of_days', models.IntegerField()),
                ('payment', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('user_name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('join_city', models.CharField(max_length=50)),
                ('join_district', models.CharField(max_length=50)),
                ('phone_number', models.IntegerField()),
            ],
        ),
    ]
