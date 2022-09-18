
from functools import reduce
import math


class Operation:
    def __init__(self, op1, op2, operator):
        self.op1 = op1
        self.op2 = op2
        self.operator = operator

    def perform(self):
        if self.operator == '+':
            return self.op1 + self.op2
        elif self.operator == '-':
            return self.op1 - self.op2
        elif self.operator == '*':
            return self.op1 * self.op2
        elif self.operator == '/':
            return self.op1 / self.op2
        else:
            raise Exception("bad operator")
    
    def show(self):
        print(str(self.op1) + self.operator + str(self.op2) + " = ")