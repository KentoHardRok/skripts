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
addr = address.copy()

def instruct_set():
    if opcodes == 1:
        addr[opcodes] = sum(param_list)
    elif opcodes == 2:
        addr[opcodes] = functools.reduce(operator.mul, param_list)
    elif opcodes == 99:
        pass
    else:
        exit(100)
    print(addr[0])

while i+instr_value in range(len(addr)):
    opcodes = int(map(int, addr[i:oc_count]))
    params = map(int, addr[i + oc_count:i + param_count])
    instruct_set()
    i += instr_value

print(100 * noun + verb)
