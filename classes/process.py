class Process:
    def __init__(self, processInfo):
        self.name = processInfo[0]
        self.pid = int(processInfo[1])
        self.execTime = int(processInfo[2])
        self.priority = int(processInfo[3])
        self.uid = int(processInfo[4])
        self.memory = int(processInfo[5])