from django.test import TestCase
from cryptography.fernet import Fernet
import json
import datetime
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()

try:
    scheduler.start()
except(KeyboardInterrupt, SystemExit):
    scheduler.shutdown()


def add_one_time(func, args, id, timi):
    # 年月日，时分秒
    # 2018-09-06 11:00:00
    # max_instances 最大实例数
    # misfire_grace_time = 失火时间最大值
    add = scheduler.add_job(func, 'date', args=(args,), run_date=timi, id=str(id), max_instances=10,
                            misfire_grace_time=300)
    return add


def get_time(id):
    job = scheduler.get_job(job_id=str(id))

    return job


def rem_time(id):
    job = scheduler.remove_job(job_id=str(id))
    return job
