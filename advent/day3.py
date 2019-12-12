
cable_path = "/wrk/skripts/advent/cable_path"
cable_coord = [dict(), dict()]

# puts file in list
with open(cable_path) as f:
    cables = f.read().split("\n")
# splits list into array with individual steps
for i in range(len(cables)):
    cables[i] = cables[i].split(",")

for j in range(i):
    x = 0
    y = 0
    nc = 0
    for k in range(len(cables[j])):
        if cables[j][k][0] == "R":
            for c in list(range(x, int(cables[j][k][1:]))):
                x += 1
                cable_coord[j][nc] = (x,y)
                nc = nc+1
            c=0
        elif cables[j][k][0] == "L":
            for c in list(range(x, int(cables[j][k][1:]))):
                x -= 1
                cable_coord[j][nc] = (x,y)
                nc += 1
            c=0
        elif cables[j][k][0] == "U":
            for c in list(range(y, int(cables[j][k][1:]))):
                y += 1
                cable_coord[j][nc] = (x,y)
                nc += 1
            c=0

        elif cables[j][k][0] == "D":
            for c in list(range(y, int(cables[j][k][1:]))):
                y -= 1
                cable_coord[j][nc] = (x,y)
                nc += 1
            c=0

cable_list=list(cable_coord(0))
print (cable_list)



