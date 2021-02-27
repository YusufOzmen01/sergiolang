class Memory:
    def __init__(self,size):
        self.tmp_memory = []
        self.memory = []
        self.size = size
        self.applied_memory = 0
        for i in range(size):
            self.memory.append(0)
            self.tmp_memory.append(0)

    def capacityLeft(self):
        freeBytes = 0
        for i in range(self.size):
            if i != 0:
                freeBytes = freeBytes + 1
        return freeBytes
