import time
import sched
import winsound as ws

def set_alarm(altime, song, mssg):
    s = sched.scheduler(time.time, time.sleep) #passing funcs
    s.enterabs(altime, 1 , print, argument=(mssg,)) #altime be numeric
    s.enterabs(altime, 1 , ws.PlaySound, argument=(song, ws.SND_FILENAME))

    print('alarm set for ', time.asctime(time.localtime(altime)))
    s.run()


set_alarm(time.time()+5, 'alarm.wav', 'Wake up!!!')
