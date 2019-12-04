puzzle = "/wrk/skripts/advent/mod_list"
gas: float = 0

with open(puzzle) as f:
    modules = f.read().splitlines() # reads lines into list
modules = list(map(int, modules)) # We label all items as int

for i in range(len(modules)): #for each item in the list range
    gas += (int((modules[i])/3)-2) # gas = gas + this math You can also do the math on each item as it puts into list then use sum() of the list

print(gas)
