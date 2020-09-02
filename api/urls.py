from django.urls import path

from api.views import Covid19Report

app_name = "api"

urlpatterns = [
    path('reports', Covid19Report.as_view(), name='Covid19Report'),
]