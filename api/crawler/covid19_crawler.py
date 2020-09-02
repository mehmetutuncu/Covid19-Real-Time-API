import requests
from bs4 import BeautifulSoup
from datetime import datetime


from api.models import Covid19TotalData, Covid19DailyData


class Covid19Crawler:
    def __init__(self):
        self.base_url = "https://covid19.saglik.gov.tr/?lang=tr-TR"
        self.today = datetime.date(datetime.today())

    @staticmethod
    def save_total_data(soup, today):
        items = soup.select('ul.list-group.list-group-genislik')[0].select('li')

        data = dict(
            total_number_of_test=int(items[0].select('span')[1].text.replace('.', '')),
            total_number_of_patients=int(items[1].select('span')[1].text.replace('.', '')),
            total_number_of_deaths=int(items[2].select('span')[1].text.replace('.', '')),
            pneumonia_rate_in_patients=float(items[3].select('span')[1].text.replace(',', '.').replace('%', '')),
            number_of_seriously_ill_patients=int(items[4].select('span')[1].text.replace('.', '')),
            total_number_of_recovered_patients=int(items[5].select('span')[1].text.replace('.', ''))
        )
        if not Covid19TotalData.objects.filter(report_date=today).exists():
            Covid19TotalData.objects.create(**data)

    @staticmethod
    def save_daily_data(soup, today):
        items = soup.select('div.mtop-bosluk.buyuk-bilgi-l ul li')
        data = dict(
            number_of_tests_for_today=int(items[0].select('span')[1].text.replace('.', '')),
            number_of_patients_for_today=int(items[1].select('span')[1].text.replace('.', '')),
            number_of_deaths_for_today=int(items[2].select('span')[1].text.replace('.', '')),
            number_of_recovered_patients_for_today=int(items[3].select('span')[1].text.replace('.', '')),
        )
        if not Covid19DailyData.objects.filter(report_date=today).exists():
            Covid19DailyData.objects.create(**data)

    def main(self):
        response = requests.get(self.base_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'lxml')
            self.save_total_data(soup, self.today)
            self.save_daily_data(soup, self.today)


if __name__ == '__main__':
    cov19 = Covid19Crawler()
    cov19.main()
