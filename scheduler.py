import my_schedule as schedule
import time
from glob import glob
import os
import sys
import argparse
from datetime import datetime
from settings import job_path

sys.path.append(job_path)

scheduler = schedule.Scheduler()

def load_jobs():
    job_files = glob(os.path.join(job_path, '*.py'))
    for job_file in job_files:
        filepath,filename = os.path.split(job_file)
        exec(f"from {filename.replace('.py', '')} import job")
        scheduler.jobs.append(eval(f"job"))


if __name__ == '__main__':
    start_time = datetime.now()
    end_time = datetime(start_time.year,start_time.month,start_time.day,23,59,59)
    parser = argparse.ArgumentParser(description='TaskSchedule')
    parser.add_argument('--one_day_life',action='store_true', help='在24点结束运行')
    args = parser.parse_args()
    load_jobs()
    while True:
        if args.one_day_life:
            print('24点以后自动退出')
            if datetime.now() > end_time:
                print('退出程序')
                sys.exit()
        scheduler.run_pending()
        time.sleep(1)


