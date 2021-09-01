import heapq
from classes.process import Process
from random import randint

class Priority:
    def __init__(self, processes):
        self.PROCESSES = [(-p.priority, p) for p in processes]
        heapq.heapify(self.PROCESSES)

    def insert(self, process: Process):
        heapq.heappush(self.PROCESSES, (-process.priority, process))
    
    def next(self):
        return heapq.heappop(self.PROCESSES)[1]

class Cyclic:
    def __init__(self, processes):
        self.PROCESSES: list = processes
    
    def insert(self, process):
        self.PROCESSES.append(process)
    
    def next(self):
        return self.PROCESSES.pop(0)

class Raffle:
    def __init__(self, processes):
        self.PROCESSES: list = processes
    
    def insert(self, process):
        self.PROCESSES.append(process)
    
    def next(self):
        ticket = randint(1, sum(p.priority for p in self.PROCESSES))

        current = 0
        for p in range(len(self.PROCESSES)):
            current += self.PROCESSES[p].priority
            if ticket <= current:
                return self.PROCESSES.pop(p)
        