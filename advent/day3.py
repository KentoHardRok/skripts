cable_path = "/wrk/skripts/advent/cable_path"
cable_coord = [dict(),dict()]
# puts file in list
with open(cable_path) as f:
    cables = f.read().split("\n")
# splits list into array with individual steps
for i in range(len(cables)):
    cables[i] = cables[i].split(",")

for j in range(i):
    print("Cable Num: ",j+1)
    x = 0
    y = 0
    for k in range(len(cables[j])):
        if cables[j][k][0] == "R":
            x += int(cables[j][k][1:])
        elif cables[j][k][0] == "L":
            x -= int(cables[j][k][1:])
        elif cables[j][k][0] == "U":
            y += int(cables[j][k][1:])
        elif cables[j][k][0] == "D":
            y -= int(cables[j][k][1:])
        cable_coord[j][k] = (x,y)    
            

print(cable_coord[1][199][0])
print(i)
print(x, y)