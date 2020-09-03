from django.http import JsonResponse
from django.shortcuts import render
from django.core.paginator import Paginator
# Create your views here.
from rest_framework.views import APIView
from api.serializers import DailyReportSerializer, QueryStringSerializer
from api.models import Covid19DailyData


def self_paginator(objects, item_per_page, page):
    p = Paginator(objects, item_per_page)
    total_items = p.count
    total_page = p.num_pages
    if page > total_page:
        page = 1
    page_obj = p.page(page)
    data = page_obj.object_list
    return data, total_items, total_page, page


class Covid19Report(APIView):
    permission_classes = []

    @staticmethod
    def get_serializer_data(data):
        return data.get('page'), data.get('item_per_page'), data.get('start_date'), data.get('end_date'), data.get(
            'filter')

    @staticmethod
    def query_builder(start_date, end_date, _filter):
        daily_objects = Covid19DailyData.objects.all().order_by('id')
        if _filter is not None and _filter == 'gte':
            daily_objects = daily_objects.filter(report_date__gte=start_date)
        elif _filter is not None and _filter == 'lte':
            daily_objects = daily_objects.filter(report_date__lte=start_date)
        elif _filter is not None and _filter == 'range':
            daily_objects = daily_objects.filter(report_date__range=[start_date, end_date])
        elif _filter is not None and _filter == 'equals':
            daily_objects = daily_objects.filter(report_date=start_date)
        return daily_objects

    def get(self, request):
        serializer = QueryStringSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        page, item_per_page, start_date, end_date, _filter = self.get_serializer_data(serializer.data)

        daily_objects = self.query_builder(start_date, end_date, _filter)
        daily_serializer_data = []
        daily_objects, total_items, total_page, page = self_paginator(daily_objects, item_per_page, page)
        if len(daily_objects) > 0:
            daily_serializer = DailyReportSerializer(data=daily_objects, many=True)
            daily_serializer.is_valid()
            daily_serializer_data = daily_serializer.data

        return JsonResponse(
            dict(daily_report=daily_serializer_data, total_items=total_items, page=page, total_page=total_page,
                 item_per_page=item_per_page))
