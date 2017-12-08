'''


'''

TEST_INPUT_FILENAME = 'test.txt'
MY_FILENAME = 'input.txt'


def parse_instructions(filename):
    with open(filename) as myfile:
        instructions = [line.split() for line in myfile]

    registers = {}
    largest_max_val = 0

    for instruction in instructions:
        if not instruction[0] in registers: # the named register
            registers[instruction[0]] = 0

        if not instruction[4] in registers:  # the register in the condition
            registers[instruction[4]] = 0

        is_cond_met = False

        if instruction[5] == '>' :
            is_cond_met = registers[instruction[4]] > int(instruction[6])
        elif instruction[5] == '>=':
            is_cond_met = registers[instruction[4]] >= int(instruction[6])
        elif instruction[5] == '==':
            is_cond_met = registers[instruction[4]] == int(instruction[6])
        elif instruction[5] == '<=':
            is_cond_met = registers[instruction[4]] <= int(instruction[6])
        elif instruction[5] == '<':
            is_cond_met = registers[instruction[4]] < int(instruction[6])
        elif instruction[5] == '!=':
            is_cond_met = registers[instruction[4]] != int(instruction[6])

        if is_cond_met :
            if instruction[1] == 'inc':
                registers[instruction[0]] += int(instruction[2])
            elif instruction[1] == 'dec':
                registers[instruction[0]] -= int(instruction[2])

        max_val = max(registers.values())
        if max_val > largest_max_val:
            largest_max_val = max_val

    print 'Max value in a register is: ' + str(max_val)
    print 'Largest value in a register was: ' + str(largest_max_val)

if __name__ == '__main__':
    parse_instructions(MY_FILENAME)