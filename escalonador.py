import threading, time
from classes.process import Process
from classes.scheduler import Scheduler

algorithm, cpuSlice = input().split('|')

scheduler = Scheduler(algorithm=algorithm, cpuSlice=int(cpuSlice))
print(scheduler.cpuSlice)
while True:
    try:
        process = Process(input().split('|'))
        scheduler.addProcess(process)
    except EOFError:
        break

while scheduler.chooseProcess():
    time.sleep(scheduler.cpuSlice)

"""def process_input():
    while True:
        cmd = input()

        if cmd == 'show':
            print("Process #1 running, 5ms to finish.")
        elif cmd == 'add':
            cmd = input()
            print(cmd)

def scheduler():
    i = 0
    while i < 10:
        time.sleep(5)
        i += 1


t2 = threading.Thread(target = scheduler, args=())
t2.start()

t1 = threading.Thread(target = process_input, args=())
t1.start()

t1.join()
t2.join()"""