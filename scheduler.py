import my_schedule as schedule
import time
from glob import glob
import os
import sys
import argparse
from datetime import datetime

job_path = './Jobs'
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
            datetime.now()
        scheduler.run_pending()
        time.sleep(1)


