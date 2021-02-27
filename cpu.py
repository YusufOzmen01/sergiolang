import pickle

class CPU:
    def __init__(self, memory, clockSpeed):
        self.clockSpeed = clockSpeed
        self.memory = memory
        self.instructions = [['set', 'data', self.set, 'both'],
                            ['write', 'address', self.write, 'int'],
                            ['print', 'address', self.print, 'int'],
                            ['abs', 'address1, address2, target', self.abs, 'int'],
                            ['sub', 'address1, address2, target', self.sub, 'int'],
                            ['div', 'address1, address2, target', self.div, 'int'],
                            ['mul', 'address1, address2, target', self.mul, 'int'],
                            ['absStr', 'address1, address2, target', self.absStr, 'string'],
                            ['inp', 'target, display_message', self.inp, 'int, string'],
                            ['dump', 'target', self.dump, 'string'],
                            ['load', 'target', self.load, 'string'],]

    # MEMORY

    def set(self, data):
        if type(data) == "int":
            print('A')
            if data > 255:
                data = 255
        else:
            dataN = ''
            for i in range(1,len(data)):
                dataN += data[i] + " "
            self.memory.tmp_memory[0] = dataN
            return False
        self.memory.tmp_memory[0] = data
        return False

    def write(self, addr):
        self.memory.memory[int(addr[1])] = self.memory.tmp_memory[0]
        self.memory.applied_memory = self.memory.tmp_memory[0]
        return True

    def dump(self, addr):
        with open(self.memory.memory[int(addr[1])], 'wb') as _m:
            pickle.dump(self.memory.memory, _m)

    def load(self, addr):
        with open(self.memory.memory[int(addr[1])], 'rb') as _m:
            self.memory.memory = pickle.load(_m)
    # MATH

    def abs(self, addr):
        try:
            self.memory.memory[int(addr[3])] = int(self.memory.memory[int(addr[1])]) + int(self.memory.memory[int(addr[2])])
        except:
            return 2

    def absStr(self, addr):
        try:
            self.memory.memory[int(addr[3])] = str(self.memory.memory[int(addr[1])]) + str(self.memory.memory[int(addr[2])])
        except:
            return 2

    def sub(self, addr):
        try:
            self.memory.memory[int(addr[3])] = int(self.memory.memory[int(addr[1])]) - int(self.memory.memory[int(addr[2])])
        except:
            return 2

    def div(self, addr):
        try:
            self.memory.memory[int(addr[3])] = int(self.memory.memory[int(addr[1])]) // int(self.memory.memory[int(addr[2])])
        except:
            return 2

    def mul(self, addr):
        try:
            self.memory.memory[int(addr[3])] = int(self.memory.memory[int(addr[1])]) * int(self.memory.memory[int(addr[2])])
        except:
            return 2
    
    # IO
    
    def inp(self, addr):
        self.memory.memory[int(addr[1])] = input(self.memory.memory[int(addr[2])])

    def print(self, addr):
        print(self.memory.memory[int(addr[1])])
