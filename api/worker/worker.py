from apscheduler.schedulers.background import BackgroundScheduler
from api.crawler.covid19_crawler import covid19_crawler


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(covid19_crawler, 'interval', minutes=60)
    scheduler.start()
