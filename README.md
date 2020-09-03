# Real Time Covid-19 API
Bu api 1 saat aralıklarla Sağlık Bakanlığı'nın https://covid19.saglik.gov.tr/covid19api?getir=liste <br>
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
Query String: <br> 
<b>page</b>: Gönderilmesi zorunlu değil varsayılan 1 atanır.<br>
<b>item_per_page</b>: Gönderilmesi zorunlu değil varsayılan 10 atanır.<br>
<b>filter</b>: Alabileceği değerler (gte, lte, equals, range)<br>
gte, lte ve equals için <b>start_date</b> gönderilmesi gerekir.<br>
range için start_date ve end_date aynı anda gönderilmelidir.<br>
Tarih Formatı: YYYY-MM-DD '%Y-%m-%d' şeklindedir. 

Response:
```json
{
    "daily_report": [
        {
            "id": 176,
            "report_date": "2020-09-02",
            "number_of_tests_for_today": 107927,
            "number_of_patients_for_today": 1596,
            "number_of_deaths_for_today": 45,
            "number_of_recovered_patients_for_today": 947,
            "total_number_of_test": 7355862,
            "total_number_of_patients": 273301,
            "total_number_of_deaths": 6462,
            "pneumonia_rate_in_patients": 7.6,
            "number_of_seriously_ill_patients": 1017,
            "total_number_of_recovered_patients": 246876
        },
        {
            "id": 177,
            "report_date": "2020-09-01",
            "number_of_tests_for_today": 109443,
            "number_of_patients_for_today": 1572,
            "number_of_deaths_for_today": 47,
            "number_of_recovered_patients_for_today": 1003,
            "total_number_of_test": 7247935,
            "total_number_of_patients": 271705,
            "total_number_of_deaths": 6417,
            "pneumonia_rate_in_patients": 7.6,
            "number_of_seriously_ill_patients": 991,
            "total_number_of_recovered_patients": 245929
        },
        {
            "id": 178,
            "report_date": "2020-08-31",
            "number_of_tests_for_today": 110102,
            "number_of_patients_for_today": 1587,
            "number_of_deaths_for_today": 44,
            "number_of_recovered_patients_for_today": 1087,
            "total_number_of_test": 7138492,
            "total_number_of_patients": 270133,
            "total_number_of_deaths": 6370,
            "pneumonia_rate_in_patients": 7.5,
            "number_of_seriously_ill_patients": 961,
            "total_number_of_recovered_patients": 244926
        },
        {
            "id": 179,
            "report_date": "2020-08-30",
            "number_of_tests_for_today": 91302,
            "number_of_patients_for_today": 1482,
            "number_of_deaths_for_today": 42,
            "number_of_recovered_patients_for_today": 1027,
            "total_number_of_test": 7028390,
            "total_number_of_patients": 268546,
            "total_number_of_deaths": 6326,
            "pneumonia_rate_in_patients": 7.5,
            "number_of_seriously_ill_patients": 945,
            "total_number_of_recovered_patients": 243839
        },
        {
            "id": 180,
            "report_date": "2020-08-29",
            "number_of_tests_for_today": 101414,
            "number_of_patients_for_today": 1549,
            "number_of_deaths_for_today": 39,
            "number_of_recovered_patients_for_today": 1003,
            "total_number_of_test": 6937088,
            "total_number_of_patients": 267064,
            "total_number_of_deaths": 6284,
            "pneumonia_rate_in_patients": 7.4,
            "number_of_seriously_ill_patients": 917,
            "total_number_of_recovered_patients": 242812
        },
        {
            "id": 181,
            "report_date": "2020-08-28",
            "number_of_tests_for_today": 107814,
            "number_of_patients_for_today": 1517,
            "number_of_deaths_for_today": 36,
            "number_of_recovered_patients_for_today": 1017,
            "total_number_of_test": 6835674,
            "total_number_of_patients": 265515,
            "total_number_of_deaths": 6245,
            "pneumonia_rate_in_patients": 7.4,
            "number_of_seriously_ill_patients": 896,
            "total_number_of_recovered_patients": 241809
        },
        {
            "id": 182,
            "report_date": "2020-08-27",
            "number_of_tests_for_today": 106111,
            "number_of_patients_for_today": 1491,
            "number_of_deaths_for_today": 26,
            "number_of_recovered_patients_for_today": 995,
            "total_number_of_test": 6727860,
            "total_number_of_patients": 263998,
            "total_number_of_deaths": 6209,
            "pneumonia_rate_in_patients": 7.3,
            "number_of_seriously_ill_patients": 862,
            "total_number_of_recovered_patients": 240792
        },
        {
            "id": 183,
            "report_date": "2020-08-26",
            "number_of_tests_for_today": 100109,
            "number_of_patients_for_today": 1313,
            "number_of_deaths_for_today": 20,
            "number_of_recovered_patients_for_today": 1002,
            "total_number_of_test": 6621749,
            "total_number_of_patients": 262507,
            "total_number_of_deaths": 6183,
            "pneumonia_rate_in_patients": 7.4,
            "number_of_seriously_ill_patients": 841,
            "total_number_of_recovered_patients": 239797
        },
        {
            "id": 184,
            "report_date": "2020-08-25",
            "number_of_tests_for_today": 98231,
            "number_of_patients_for_today": 1502,
            "number_of_deaths_for_today": 24,
            "number_of_recovered_patients_for_today": 887,
            "total_number_of_test": 6521640,
            "total_number_of_patients": 261194,
            "total_number_of_deaths": 6163,
            "pneumonia_rate_in_patients": 7.4,
            "number_of_seriously_ill_patients": 811,
            "total_number_of_recovered_patients": 238795
        },
        {
            "id": 185,
            "report_date": "2020-08-24",
            "number_of_tests_for_today": 95943,
            "number_of_patients_for_today": 1443,
            "number_of_deaths_for_today": 18,
            "number_of_recovered_patients_for_today": 743,
            "total_number_of_test": 6423409,
            "total_number_of_patients": 259692,
            "total_number_of_deaths": 6139,
            "pneumonia_rate_in_patients": 7.4,
            "number_of_seriously_ill_patients": 796,
            "total_number_of_recovered_patients": 237908
        }
    ],
    "total_items": 175,
    "page": 1,
    "total_page": 18,
    "item_per_page": 10
}
```
## Ekran Resmi
<a href="https://ibb.co/xFSz3xq"><img src="https://i.ibb.co/phv4nYj/Screenshot-20200903-110001.png" alt="Screenshot-20200903-110001" border="0"></a>