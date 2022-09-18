import asyncio
import time
import random
import src.operation as op
import threading

MATH_OPERATORS = ['+', '-', '*']

def main():
    done = [False]
    timer_thread = threading.Thread(target=clock, args=(done,))
    timer_thread.start()

    correct = 0
    while not done[0]:
        operation = next_op()
        operation.show()
        response = input("")

        if float(response) == float(operation.perform()):
            correct += 1
        else:
            print("Wrong answer!")
    print("Correct answers: " + str(correct))
        

def clock(done)->None:
    print("starting clock...")
    time.sleep(10)
    done[0] = True
    print("finished clock.")

def next_op() -> op.Operation:
    op1 = random.randint(0, 10)
    op2 = random.randint(1, 10)
    operator = random.choice(MATH_OPERATORS)
    
    return op.Operation(op1, op2, operator)


if __name__ == "__main__":
    main()