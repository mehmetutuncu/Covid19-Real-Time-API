import requests
from bs4 import BeautifulSoup
from datetime import datetime

from api.models import Covid19DailyData


def covid19_crawler():
    response = requests.get("https://covid19.saglik.gov.tr/covid19api?getir=liste")
    if response.status_code == 200:
        json_data = response.json()
        for item in json_data:
            report_date = datetime.strptime(item['tarih'], '%d.%m.%Y')
            if not Covid19DailyData.objects.filter(report_date=report_date).exists():
                daily_data = dict(
                    number_of_tests_for_today=int(item['gunluk_test'].replace('.', ''))
                    if item['gunluk_test'] != '' else None,
                    number_of_patients_for_today=int(item['gunluk_vaka'].replace('.', ''))
                    if item['gunluk_vaka'] != '' else None,
                    number_of_deaths_for_today=int(item['gunluk_vefat'].replace('.', ''))
                    if item['gunluk_vefat'] != '' else None,
                    number_of_recovered_patients_for_today=int(item['gunluk_iyilesen'].replace('.', ''))
                    if item['gunluk_iyilesen'] != '' else None,
                    report_date=report_date,
                    total_number_of_test=int(item['toplam_test'].replace('.', ''))
                    if item['toplam_test'] != '' else None,
                    total_number_of_patients=int(item['toplam_vaka'].replace('.', ''))
                    if item['toplam_vaka'] != '' else None,
                    total_number_of_deaths=int(item['toplam_vefat'].replace('.', ''))
                    if item['toplam_vefat'] != '' else None,
                    pneumonia_rate_in_patients=float(item['hastalarda_zaturre_oran'].replace(',', '.'))
                    if item['hastalarda_zaturre_oran'] != '' else None,
                    number_of_seriously_ill_patients=int(item['agir_hasta_sayisi'].replace('.', ''))
                    if item['agir_hasta_sayisi'] != '' else None,
                    total_number_of_recovered_patients=int(item['toplam_iyilesen'].replace('.', ''))
                    if item['toplam_iyilesen'] != '' else None,
                )
                Covid19DailyData.objects.create(**daily_data)


if __name__ == '__main__':
    covid19_crawler()
