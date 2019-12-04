import math

#str = ["R75,D30,R83,U83,L12,D49,R71,U7,L72","U62,R66,U55,R34,D71,R55,D58,R83"]
str = ["R8,U5,L5,D3","U7,R6,D4,L4"]
width = 0
height = 0
tempx = 0
tempy = 0
for x in str:
    minx = 0
    maxx= 0
    miny=0
    maxy = 0
    tempx = 0
    tempy = 0
    for y in x.split(','):
        if y[0] == 'R':
            tempx += int(y[1:])

            minx = min(minx,tempx)
            maxx = max(maxx,tempx)
        if y[0] == 'D':
            tempy -= int(y[1:])

            miny = min(miny,tempy)
            maxy = max(maxy,tempy)
        if y[0] == 'L':
            tempx -= int(y[1:])

            minx = min(minx,tempx)
            maxx = max(maxx,tempx)
        if y[0] == 'U':
            tempy += int(y[1:])

            miny = min(miny,tempy)
            maxy = max(maxy,tempy)
map = []
for y in range(maxy-miny+1):
    map.append([])
    for x in range(maxx-minx+1):
        map[-1].append('')

for x in range(len(str)):
    tempx = 0
    tempy = 0
    for y in str[x].split(','):
        count = int(y[1:])
        if y[0] == 'R':
            for num in range(count):
                if str(x) not in map[len(map)-tempy][tempx+num]:
                    map[len(map)-tempy][tempx+num]+=str(x)
            tempx += count
        if y[0] == 'D':
            tempy -= count
            for num in range(count):
                map[len(map)-tempy+num][tempx]

        if y[0] == 'L':
            tempx -= count

        if y[0] == 'U':
            tempy += count

        
print(minx)
print(len(map)-miny)
for row in map:
    print(row)