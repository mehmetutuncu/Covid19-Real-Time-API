# Real Time Covid-19 API
Bu api 1 saat aralıklarla Sağlık Bakanlığı'nın https://covid19.saglik.gov.tr/?lang=tr-TR <br>
adresinden açıklamış olduğu verileri otomatik olarak arka planda çeker. <br>
Çektiği bu verileri veritabanına kaydedip tetiklenmesi ile Json olarak serialize edip kullanıma sunar.

### Bağımlılıkların Kurulumu ve API Çalıştırılması:
```
pip install -r requirements.pip
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
##### Docker üzeride kurulum:
```
docker build . -t covid19-api
docker run -d --restart always -p 8000:8000 --name covid19-api covid19-api
```
##### Sonuçlara ulaşmak için:
Method: GET <br>
endpoint: api/reports <br>
Response:
```json
{
    "daily_report": {
        "id": 1,
        "report_date": "2020-09-02",
        "number_of_tests_for_today": 109443,
        "number_of_patients_for_today": 1572,
        "number_of_deaths_for_today": 47,
        "number_of_recovered_patients_for_today": 1003
    },
    "total_report": {
        "id": 1,
        "report_date": "2020-09-02",
        "total_number_of_test": 7247935,
        "total_number_of_patients": 271705,
        "total_number_of_deaths": 6417,
        "pneumonia_rate_in_patients": 7.6,
        "number_of_seriously_ill_patients": 991,
        "total_number_of_recovered_patients": 245929
    }
}
```
## Ekran Resmi
<a href="https://ibb.co/CtQbVkN"><img src="https://i.ibb.co/SxBtVhW/Screenshot-20200902-123159.png" alt="Screenshot-20200902-123159" border="0"></a>