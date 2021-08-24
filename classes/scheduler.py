from classes.algorithms import Cyclic, Priority, Raffle
from classes.process import Process
from threading import Thread
from time import sleep


scheduleAlgorithms = {
    'alternancia':  Cyclic,
    'loteria':      Raffle,
    'prioridade':   Priority
}

class Scheduler:
    def __init__(self, algorithm, processes, cputime):
        self.table = (scheduleAlgorithms[algorithm])(processes)
        self.cputime = cputime
    
    def run(self):

        while len(self.table.PROCESSES) > 0:
            process: Process = self.table.next()
            time = min(self.cputime, process.execTime)
            
            print(f"Processo <{process}> executando por {time} ms", end="\n", flush=True)
            sleep(time*10e-3)
            
            process.execTime -= time
            if process.execTime:
                self.table.insert(process)
            





# from random import randint
# class Scheduler:
#     def __init__(self, algorithm, cpuSlice):
#         self.algorithm = algorithm
#         self.cpuSlice = cpuSlice
#         self.processList = []

#         self.totalTickets = 0

#     def addProcess(self, process):
#         if self.algorithm == 'alternancia':
#             pass
#         elif self.algorithm == 'prioridade':
#             pass
#         elif self.algorithm == 'loteria':
#             self._lotteryAddProcess(process)

#     def _lotteryAddProcess(self, process):
#         self.totalTickets += process.priority
#         self.processList.append(process)
    
#     def chooseProcess(self):
#         if self.algorithm == 'loteria':
#             if self.totalTickets == 0:
#                 return False

#             self._lotteryChooseProcess()
#             return True
#         else:
#             pass

#     def _lotteryChooseProcess(self):
#         ticket = randint(1, self.totalTickets)

#         ticketSum = 0
#         for i in range(len(self.processList)):
#             if self.processList[i].execTime == 0:
#                 continue

#             ticketSum += self.processList[i].priority

#             if ticketSum >= ticket:
#                 process = self.processList[i]
                
#                 if self.cpuSlice >= process.execTime:
#                     process.execTime = 0
#                     self.totalTickets -= process.priority
#                 else:
#                     process.execTime -= self.cpuSlice

#                 break
        
#         return True

#     def finishProcess(self, idx):
#         if self.algorithm == 'loteria':
#             self.totalTickets -= self.processList[idx].priority
#             pass
