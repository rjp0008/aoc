
with open(r"C:\Users\rjp00\source\repos\rjp0008\aoc\5.txt") as f:
    position = 0
    opcodes = f.readline().split(',')

    while opcodes[position] != 99:
        command = int(opcodes[position][-2:])
        total = f"{opcodes[position]}".rjust(5,'0')
        if total[2] == '0':
            p1 = opcodes[int(opcodes[position + 1])]
        else:
            p1 = opcodes[position+1]
        if total[1] == '0':
            p2 = opcodes[int(opcodes[position + 2])]
        else:
            p2 = opcodes[position +2]
        if total[0] == '0':
            p3 = opcodes[int(opcodes[position + 3])]
        else:
            p3 = opcodes[position+3]
        p1 = int(p1)
        p2 = int(p2)
        p3 = int(p3)
        if command == 1:#add
            opcodes[int(opcodes[position + 3])] = str(p1 + p2)
            position += 4

        elif command == 2: #mult
            opcodes[int(opcodes[position + 3])] = str(p1 * p2)
            position += 4

        elif command == 3:
            opcodes[int(opcodes[position + 1])] = str(1)
            position += 2
        elif command == 4:
            print(opcodes[p1])
            position += 2

        elif command == 99:
            break

