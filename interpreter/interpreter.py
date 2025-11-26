from stack_machine import StackMachine
import sys
import re

def main():
    if not sys.argv[1]:
        raise Exception("Please supply a program path as an argument")
    program_path: str = sys.argv[1]

    with open(program_path, "r") as file:
        program = file.read().replace('\n','').replace(' ','')

    program_parsed = {}
    machine = StackMachine()

    current_read = ""
    index = 0

    while True:

        if "viaadexcellentiam" in current_read:
            break

        if "techxx" in current_read or "techx::" in current_read or "techtechx" in current_read:
            parseInstruction(machine, current_read)
            program_parsed[machine.program_counter] = current_read

            current_read = ""
            machine.program_counter += 1

        else:
            current_read += program[index]
            index +=1

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
            parameter_techx = instruction[len(operation) + 1:len(instruction) - 1]
            parameter = len(re.findall(r'techx', parameter_techx))
            Machine.push(parameter)

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

