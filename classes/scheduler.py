from classes.algorithms import Cyclic, Priority, Raffle
from classes.process import Process
from threading import Thread
from time import sleep

class Scheduler:
    def __init__(self, processes, cputime, algorithm = Priority):
        self.table = algorithm(processes)
        self.cputime = cputime
    
    def run(self):
        def __inputListener():
            while True:
                input()
                with open("newprocess.txt", "r+") as new:
                    inputLines = new.readlines()

                    try:
                        for p in inputLines[1:]:
                            self.table.insert(Process.fromString(p))
                    except Exception as e:
                        print(e)

                    new.seek(0)
                    new.truncate()
                    new.write(inputLines[0])

        try:
            listener = Thread(
                target=__inputListener,
                args=()
            )
            listener.setDaemon(True)
            listener.start()
            
            while len(self.table.PROCESSES) > 0:
                process: Process = self.table.next()
                time = min(self.cputime, process.execTime)

                print(f"Processo <{process}> executando por {time:.2f} s", end="\n", flush=True)
                sleep(time * 0.1)
                
                process.execTime -= time
                if process.execTime:
                    self.table.insert(process)
        except KeyboardInterrupt:
            return

