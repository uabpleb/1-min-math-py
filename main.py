import asyncio
import time
import random
import operation as op
import threading

MATH_OPERATORS = ['+', '-', '*', '/']

def main():
    done = [False]
    timer_thread = threading.Thread(target=clock, args=(done,))
    #done = await clock()   
    timer_thread.start()

    correct = 0
    while not done[0]:
        """
        operation = next_op()
        operation.show()
        response = input("\n")

        if float(response) == float(operation.perform()):
            correct += 1
        """
        input("trying: ")
        correct += 1
    print("Correct answers: " + str(correct))
        

def clock(done)->None:
    print("starting clock...")
    time.sleep(5)
    done[0] = True
    print("finished clock.")

def next_op() -> op.Operation:
    op1 = random.randint(0, 10)
    op2 = random.randint(1, 10)
    operator = random.choice(MATH_OPERATORS)
    
    return op.Operation(op1, op2, operator)


if __name__ == "__main__":
    #asyncio.run(main())
    main()