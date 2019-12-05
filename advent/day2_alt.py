import operator
import functools

i: int = 0
oc_count: int = 1
param_count: int = 3
instr_value = oc_count + param_count

noun = 12
verb = 2

opfile = "/wrk/skripts/advent/opcode"
with open(opfile) as f:
    address = f.read().split(",")
address = list(map(int, address))

address[1] = noun
address[2] = verb


class Instructions:
    def __init__(self, count, addr, oc_num, param_list):
        self.param_list = param_list
        self.oc_num = oc_num
        self.addr = addr
        self.count = count
        self.instr_value = self.oc_num + len(self.param_list)
        self.opcodes = self.addr[count]

    def instruct_set(self):
        if self.opcodes == 1:
            self.addr[self.opcodes] = sum(self.param_list)
        elif self.opcodes == 2:
            self.addr[self.opcodes] = functools.reduce(operator.mul, self.param_list)
        elif self.opcodes == 99:
            pass
        else:
            exit(100)
        print(self.addr[0])

while i+instr_value in range(len(address)):
    oc = address[i:oc_count]
    params = address[i + oc_count:i + param_count]
    Instructions(i, address, oc, params())
    i += instr_value

print(100 * noun + verb)
