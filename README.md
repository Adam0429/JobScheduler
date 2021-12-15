# JobSchedule

和 https://github.com/Adam0429/TaskManager 类似，是基于通过修改python schedule库实现功能的。
* 可以设置定时任务
* 有消息提示
* 但更容易部署。


*  单单在crontab中设置定时任务也不便于代码统一结构
*  使用tmux开后台还是怕断电
*  最终解决方案是在crontab中每天0点自启scheduler.py，并在每天24点后关闭，以保证此程序同时只运行一个

## 用法

需要在settings.py中指定Jobs文件夹的全路径，其中放的就是需要运行的所有脚本



在Jobs程序中最底部写入如下代码，设置定时：
```
from my_schedule import Job
from utils import dingmessage

job = Job(job_func=f1, name='f1',unit='days',interval=1,at_time='16:29:00',notice_fun=dingmessage)
job = Job(job_func=f2, name='f2',unit='hours',interval=1,notice_fun=dingmessage)
```

然后运行:
```
python3 scheduler.py --one_day_life
```

命令行输出
```
f1 下次运行时间: 2021-12-15 16:29:00
f2 下次运行时间: 2021-12-15 19:31:07.689126
f1 开始运行
f1
f1 下次运行时间: 2021-12-16 16:29:00
f2 开始运行
f2
f2 下次运行时间: 2021-12-15 20:31:07.885402
```
