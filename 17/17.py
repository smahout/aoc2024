import math
import re


class Computer:
    def __init__(self, a, b, c, instructions):
        self.a = a
        self.b = b
        self.c = c
        self.instructions = instructions
        self.pc = 0  # Program counter

    def operand(self, opcode, o: int):
        if opcode == 3 or opcode == 1:
            return o
        if o <= 3:
            return o
        match o:
            case 4:
                return self.a
            case 5:
                return self.b
            case 6:
                return self.c
        raise ValueError("operand was not a value between 0 and 6")

    def operate(self):
        if self.pc > len(self.instructions) - 2:
            return False
        opcode = self.instructions[self.pc]
        self.pc += 1
        operand = self.operand(opcode, self.instructions[self.pc])
        self.pc += 1
        return self.execute(opcode, operand)

    def execute(self, opcode, operand):
        match opcode:
            case 0:
                self.adv(operand)
            case 1:
                self.bxl(operand)
            case 2:
                self.bst(operand)
            case 3:
                self.jnz(operand)
            case 4:
                self.bxc(operand)
            case 5:
                return self.out(operand)
            case 6:
                self.bdv(operand)
            case 7:
                self.cdv(operand)
        return ""

    def adv(self, operand):  # 0
        self.a = int(self.a / (2 ** operand))

    def bxl(self, operand):  # 1
        self.b = self.b ^ operand

    def bst(self, operand):  # 2
        self.b = operand % 8

    def jnz(self, operand):  # 3
        if self.a == 0:
            return
        self.pc = operand

    def bxc(self, operand):  # 4
        self.b = self.b ^ self.c

    def out(self, operand):  # 5
        return operand % 8

    def bdv(self, operand):  # 6
        self.b = int(self.a / (2 ** operand))

    def cdv(self, operand):  # 7
        self.c = int(self.a / (2 ** operand))

    def run_all(self):
        out = []
        while True:
            v = self.operate()
            if v is False:
                break
            if v != "":
                out.append(v)
        return ','.join(map(str, out))


test_computer = Computer(0,0,9,[2, 6])
test_computer.operate()
assert(test_computer.b == 1)

test_computer = Computer(10,0,0,[5,0,5,1,5,4])
assert(test_computer.run_all() == '0,1,2')

test_computer = Computer(2024,0,0,[0,1,5,4,3,0])
assert(test_computer.run_all() == '4,2,5,6,7,7,7,7,3,1,0')
assert(test_computer.a == 0)

test_computer = Computer(0,29,0,[])
test_computer.execute(1, 7)
assert(test_computer.b == 26)

test_computer = Computer(0,2024,43690,[4,0])
test_computer.operate()
assert(test_computer.b == 44354)


with open("small.txt") as f:
    registers, program_str = f.read().split("\n\n")
a, b, c = re.findall('\d+', registers)
program = [int(inst) for inst in re.findall('\d', program_str)]
computer = Computer(int(a), int(b), int(c), program)
print(computer.run_all())
