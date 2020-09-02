from rest_framework import serializers
from api.models import Covid19DailyData, Covid19TotalData


class DailyReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Covid19DailyData
        fields = '__all__'


class TotalReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Covid19TotalData
        fields = '__all__'
