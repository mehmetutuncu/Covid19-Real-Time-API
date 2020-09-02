from django.db import models


# Create your models here.

class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    report_date = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True


class Covid19TotalData(BaseModel):
    total_number_of_test = models.IntegerField()
    total_number_of_patients = models.IntegerField()
    total_number_of_deaths = models.IntegerField()
    pneumonia_rate_in_patients = models.FloatField()
    number_of_seriously_ill_patients = models.IntegerField()
    total_number_of_recovered_patients = models.IntegerField()

    class Meta:
        db_table = 'covid19_total_data'


class Covid19DailyData(BaseModel):
    number_of_tests_for_today = models.IntegerField()
    number_of_patients_for_today = models.IntegerField()
    number_of_deaths_for_today = models.IntegerField()
    number_of_recovered_patients_for_today = models.IntegerField()

    class Meta:
        db_table = 'covid19_daily_data'
