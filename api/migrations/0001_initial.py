# Generated by Django 3.1.1 on 2020-09-02 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Covid19DailyData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('report_date', models.DateField(auto_now_add=True)),
                ('number_of_tests_for_today', models.IntegerField()),
                ('number_of_patients_for_today', models.IntegerField()),
                ('number_of_deaths_for_today', models.IntegerField()),
                ('number_of_recovered_patients_for_today', models.IntegerField()),
            ],
            options={
                'db_table': 'covid19_daily_data',
            },
        ),
        migrations.CreateModel(
            name='Covid19TotalData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('report_date', models.DateField(auto_now_add=True)),
                ('total_number_of_test', models.IntegerField()),
                ('total_number_of_patients', models.IntegerField()),
                ('total_number_of_deaths', models.IntegerField()),
                ('pneumonia_rate_in_patients', models.FloatField()),
                ('number_of_seriously_ill_patients', models.IntegerField()),
                ('total_number_of_recovered_patients', models.IntegerField()),
            ],
            options={
                'db_table': 'covid19_total_data',
            },
        ),
    ]
