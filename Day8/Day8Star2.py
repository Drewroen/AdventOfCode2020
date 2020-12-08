from copy import deepcopy

f = open("Day8.txt", "r")

vals = f.read().split('\n')

instructions = list(map(lambda inst: inst.split(' '), vals))

def process_number(number):
    if number[0:1] == '+':
        return int(number[1:])
    else:
        return 0 - int(number[1:])

def get_score(instructions):

    repeated = False
    read_vals = {}
    instruction_spot = 0
    acc = 0

    while not repeated:
        if read_vals.get(instruction_spot, False) is False:
            read_vals[instruction_spot] = True
        else:
            return -1
        try:
            temp_instruction = instructions[instruction_spot]
        except:
            return acc
        if temp_instruction[0] == 'acc':
            acc = acc + process_number(temp_instruction[1])
            instruction_spot = instruction_spot + 1
        elif temp_instruction[0] == 'jmp':
            jump_value = process_number(temp_instruction[1])
            instruction_spot = instruction_spot + jump_value
        elif temp_instruction[0] == 'nop':
            instruction_spot = instruction_spot + 1


for i in range(len(instructions)):
    new_instructions = deepcopy(instructions)
    if instructions[i][0] == 'jmp':
        new_instructions[i][0] = 'nop'
    elif instructions[i][0] == 'nop':
        new_instructions[i][0] = 'jmp'

    if get_score(new_instructions) != -1:
        print(get_score(new_instructions))
