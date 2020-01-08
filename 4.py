

def same_adjacent(x):
    for position in range(len(x)-1):
        if x[position] == x[position+1]:
            return True
    return False

def increasing(x):
    init = x[0]
    for index in range(1,len(x)):
        if int(x[index]) < int(init):
            return False
        init = x[index]
    return True

print(increasing(str(123450)))
total = 0
for x in range(265275,781584):
    if same_adjacent(str(x)) and increasing(str(x)):
        total=total +1
print (total)