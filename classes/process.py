class Process:
    def __init__(self, processInfo):
        self.name = processInfo[0]
        self.pid = int(processInfo[1])
        self.execTime = int(processInfo[2])
        self.priority = int(processInfo[3])
        self.uid = int(processInfo[4])
        self.memory = int(processInfo[5])
    
    def fromString(string):
        info = string.split("|")
        return Process((info[0],info[1], info[2], info[3], info[4], info[5]))
    
    def __lt__(self, other):
        return self.priority < other.priority
    
    def __eq__(self, other) -> bool:
        return self.priority == other.priority

    
    def __str__(self):
        return f"{self.name}, {self.pid}, {self.priority}, {self.execTime:.2f}"
    
    def __repr__(self):
        return self.__str__()