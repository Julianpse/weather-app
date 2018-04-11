from crontab import CronTab
import datetime

my_cron = CronTab(user='julianse')

for job in my_cron:
    print(job)
