from apscheduler.schedulers.background import BackgroundScheduler
from api.crawler.covid19_crawler import Covid19Crawler


def run_crawler():
    cov19 = Covid19Crawler()
    cov19.main()


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(run_crawler, 'interval', seconds=5)
    scheduler.start()
