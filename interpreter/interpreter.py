from stack_machine import StackMachine
import sys
import re

def main():
    if not sys.argv[1]:
        raise Exception("Please supply a program path as an argument")
    program_path: str = sys.argv[1]

    with open(program_path, "r") as file:
        program = file.read().replace('\n','').replace(' ','')

    Machine = StackMachine()
    halt = False

def parseInstruction(Machine: StackMachine, instruction: str, program_counter: int):

    if instruction[0:2] == "::":
        label: str = ""

        for character in instruction:
            if character == ":":
                break
            else:
                label += character

        Machine.addToLabelTable(program_counter, label)

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
            
Machine = StackMachine()
parseInstruction(Machine, "techtechtechtechtechtech:techxtechxx", 2)
# main()

