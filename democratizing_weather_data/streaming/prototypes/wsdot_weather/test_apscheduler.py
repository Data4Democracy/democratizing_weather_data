from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import sys
# 输出时间
def job():
    #print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + sys.argv[1])
# BlockingScheduler
sched = BlockingScheduler()
sched.add_job(job, 'interval', seconds=3)
sched.start()