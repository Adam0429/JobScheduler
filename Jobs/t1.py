from my_schedule import Job
from utils import dingmessage

def f1():
    print('f1')

job = Job(job_func=f1, name='f1',unit='days',interval=1,at_time='16:29:00',notice_fun=dingmessage)
