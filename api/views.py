from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from api.serializers import DailyReportSerializer, TotalReportSerializer
from api.models import Covid19DailyData, Covid19TotalData


class Covid19Report(APIView):
    permission_classes = []

    @staticmethod
    def get(request):
        daily_serializer = DailyReportSerializer(data=[Covid19DailyData.objects.last()], many=True)
        daily_serializer.is_valid()
        total_serializer = TotalReportSerializer(data=[Covid19TotalData.objects.last()], many=True)
        total_serializer.is_valid()
        return JsonResponse(dict(daily_report=daily_serializer.data[0], total_report=total_serializer.data[0]))
