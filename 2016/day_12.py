import sys

registers = { 'a': 0, 'b': 0, 'c': 0, 'd': 0 }

def main():
    instructions = []

    for line in sys.stdin.readlines():
        line = line.strip().split()
        instructions.append(line)

    index = 0
    while index < len(instructions):
        i = instructions[index]

        if i[0] == 'cpy':
            if i[1] in registers:
                val = registers[i[1]]
            else:
                val = int(i[1])
            registers[i[2]] = val
        elif i[0] == 'inc':
            registers[i[1]] += 1
        elif i[0] == 'dec':
            registers[i[1]] -= 1
        elif i[0] == 'jnz':
            if (i[1] in registers and registers[i[1]] != 0) or (i[1].isdigit() and int(i[1]) != 0):
                index += int(i[2])
                continue
        else:
            print "Instruction '{}' unknown.".format(line[0]) 
        index += 1

    print "The value in register 'a' is {}.".format(registers['a'])


if __name__ == "__main__":
    main()
