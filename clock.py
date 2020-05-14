import replurk, quote, ura_pc_gacha_config

from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=1)
def timed_job():
    replurk.replurk_appraisal_posts()

    
sched.start()
