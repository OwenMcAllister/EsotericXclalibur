class StackMachine:
    def __init__(self):
        self.data_stack: list[int] = []
        self.program_counter: int = 0
        self.label_table: dict[str, int] = {}

    def push(self, n: int) -> None:
        self.data_stack.append(n)

    def duplicate(self) -> None:
        if not self.data_stack:
            raise IndexError("Cannot duplicate from empty stack")

        dup_element = self.data_stack[-1]
        self.data_stack.append(dup_element)

    def swap(self):
        if not self.data_stack:
            raise IndexError("Cannot swap from empty stack")

        addr1: int = len(self.data_stack) - 2
        addr2: int = len(self.data_stack) - 1

        temp: int = self.data_stack[addr1]
        self.data_stack[addr1] = self.data_stack[addr2]
        self.data_stack[addr2] = temp

    def add(self):
        if not self.data_stack:
            raise IndexError("Cannot add from empty stack")

        value1 = self.data_stack.pop()
        self.data_stack[len(self.data_stack) - 1] += value1

    def subtract(self):
        if not self.data_stack:
            raise IndexError("Cannot add from empty stack")

        value1 = self.data_stack.pop()
        self.data_stack[len(self.data_stack) - 1] -= value1

    def jumpz(self, label: str):
        if label not in self.label_table:
            raise IndexError(f"label: {label} DNE in program label table.")

        if self.data_stack.pop() == 0:
            self.pc = self.label_table.get(label)

    def jump(self, label: str):
        if label not in self.label_table:
            raise IndexError(f"label: {label} DNE in program label table.")

        self.pc = self.label_table.get(label)

    def out(self):
        print(self.data_stack.pop())