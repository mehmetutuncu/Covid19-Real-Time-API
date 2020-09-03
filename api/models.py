from django.db import models


# Create your models here.

class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    report_date = models.DateField(auto_now_add=False)

    class Meta:
        abstract = True


class Covid19DailyData(BaseModel):
    number_of_tests_for_today = models.IntegerField(null=True, blank=True)
    number_of_patients_for_today = models.IntegerField(null=True, blank=True)
    number_of_deaths_for_today = models.IntegerField(null=True, blank=True)
    number_of_recovered_patients_for_today = models.IntegerField(null=True, blank=True)
    total_number_of_test = models.IntegerField(null=True, blank=True)
    total_number_of_patients = models.IntegerField(null=True, blank=True)
    total_number_of_deaths = models.IntegerField(null=True, blank=True)
    pneumonia_rate_in_patients = models.FloatField(null=True, blank=True)
    number_of_seriously_ill_patients = models.IntegerField(null=True, blank=True)
    total_number_of_recovered_patients = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'covid19_daily_data'
