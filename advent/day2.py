opcode = "/wrk/skripts/advent/opcode"
# The number of opcodes to consider when evaluating the address
oc_num: int = 1
#the amount of paramets in each set of instructions
param_num: int = 3

# Number to increase to reach next opcode
instr_value = oc_num+param_num

# Values to input 
noun = 0
verb = 0

with open(opcode) as f:
    main_address = f.read().split(",")
main_address = list(map(int, main_address))

def instruction1(p1, p2, pos):
    address[pos] = address[p1]+address[p2]


def instruction2(p1, p2, pos):
    address[pos] = address[p1]*address[p2]


def instruction99():
    pass


for j in range(99):
    noun = j
    for k in range(99):
        verb = k
        address = main_address.copy()
        address[1] = noun
        address[2] = verb
        i: int = 0
        while i+instr_value in range(len(address)):
            param1 = address[i+1]
            param2 = address[i+2]
            param3 = address[i+3]
            opcode = address[i]
            if address[0] == 19690720:
                print(noun)
                print(verb)
                print(100 * noun + verb)
                print(address[0])
                break
            elif opcode == 1:
                instruction1(param1, param2, param3)
            elif opcode == 2:
                instruction2(param1, param2, param3)
            elif opcode == 99:
                instruction99()
            else:
                break
            i += instr_value

