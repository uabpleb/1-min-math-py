import random
from src.clock_thread import ClockThread
import src.operation as op

MATH_OPERATORS = ['+', '-', '*']

def main():
    clock = ClockThread(5)
    clock.start()

    correct = 0
    while not clock.done():
        operation = next_op()
        operation.show()
        response = input("")

        if float(response) == float(operation.perform()):
            correct += 1
        else:
            print("Wrong answer!")
        
    print("Correct answers: " + str(correct))

def next_op() -> op.Operation:
    op1 = random.randint(0, 10)
    op2 = random.randint(1, 10)
    operator = random.choice(MATH_OPERATORS)
    
    return op.Operation(op1, op2, operator)


if __name__ == "__main__":
    main()