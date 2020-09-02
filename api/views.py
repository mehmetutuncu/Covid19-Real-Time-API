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
        daily_objects = Covid19DailyData.objects.last()
        total_objects = Covid19TotalData.objects.last()
        daily_serializer_data = {}
        total_serializer_data = {}
        if daily_objects is not None:
            daily_serializer = DailyReportSerializer(data=[daily_objects], many=True)
            daily_serializer.is_valid()
            daily_serializer_data = daily_serializer.data[0]

        if total_objects is not None:
            total_serializer = TotalReportSerializer(data=[total_objects], many=True)
            total_serializer.is_valid()
            total_serializer_data = total_serializer.data[0]
        return JsonResponse(dict(daily_report=daily_serializer_data, total_report=total_serializer_data))
