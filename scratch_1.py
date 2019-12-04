import copy
with open(r"C:\Users\rjp00\source\repos\rjp0008\aoc\2.txt") as f:
    for x in f.readlines():
        opcodess = [int(n) for n in x.split(',')]
        for noun in range(99):
            for verb in range(99):
                opcodes = copy.deepcopy(opcodess)
                opcodes[1] = noun
                opcodes[2] = verb
                position = 0
                while opcodes[0] != 19690720:
                    try:
                        command = opcodes[position]
                        p1 = opcodes[opcodes[position+1]]
                        p2 = opcodes[opcodes[position+2]]
                        if command == 1:#add
                            opcodes[opcodes[position+3]] = p1 + p2
                        elif command == 2: #mult
                            opcodes[opcodes[position+3]] = p1 * p2
                        elif command == 99:
                            break
                        position += 4
                    except IndexError:
                        break

                if opcodes[0] == 19690720:
                    print(100*noun+verb)