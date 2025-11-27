from stack_machine import StackMachine
import sys
import re

def main():
    if not sys.argv[1]:
        raise Exception("Please supply a program path as an argument")
    program_path: str = sys.argv[1]

    with open(program_path, "r") as file:
        program = file.read().replace('\n','').replace(' ','')

    machine = StackMachine()

    tokenized_input: dict = tokenizeInput(machine, program)

    while True:
        try:
            instruction = tokenized_input[machine.program_counter]

        except KeyError:
            break

        parseInstruction(machine, instruction)


def tokenizeInput(machine, input):
    program_parsed = {}
    current_read = ""
    index = 0
    instruction_num = 0

    while True:
        if "viaadexcellentiam" in current_read:
            break

        if "techx::" in current_read:
            label: str = current_read[2:len(current_read)-2]
            machine.addToLabelTable(instruction_num, label)

            current_read = ""

        elif "techxx" in current_read or "techtechx" in current_read or ":x" in current_read:
            program_parsed[instruction_num] = current_read

            current_read = ""
            instruction_num += 1

        else:
            current_read += input[index]
            index +=1

    return program_parsed


def parseInstruction(Machine: StackMachine, instruction: str):

    if instruction[0:2] == "::":
        label: str = ""

        for character in instruction[2:]:
            if character == ":":
                break
            else:
                label += character

        Machine.addToLabelTable(StackMachine.program_counter, label)

    else:
        operation: str = ""

        for character in instruction:
            if character == ":":
                break
            else:
                operation += character

        opcode: int = len(re.findall(r'tech', operation))

        if opcode == 1:
            params = instruction[len(operation) + 1 : len(instruction) - 1]

            if params.strip() == "":
                Machine.push(0)

            else:
                n = len(re.findall(r'techx', params))
                Machine.push(n)

        elif opcode == 2:
            Machine.duplicate()

        elif opcode == 3:
            Machine.swap()

        elif opcode == 4:
            Machine.add()

        elif opcode == 5:
            Machine.subtract()

        elif opcode == 6:
            parameter = instruction[len(operation) + 1:len(instruction) - 1]

            Machine.jumpz(parameter)

        elif opcode == 7:
            parameter = instruction[len(operation) + 1:len(instruction) - 1]
            Machine.jump(parameter)

        elif opcode == 8:
            Machine.out()

main()

