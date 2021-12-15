from my_schedule import Job
from utils import dingmessage

def f2():
    print('f2')

job = Job(job_func=f2, name='f2',unit='hours',interval=1,notice_fun=dingmessage)
