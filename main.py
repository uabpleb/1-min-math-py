import asyncio
import time
import random
import operation as op

MATH_OPERATORS = ['+', '-', '*', '/']

def main():
    done = False
    #done = await clock()

    """
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.create_task(clock())
    done = loop.run_until_complete(clock())
    """
    

    correct = 0
    while not done:
        done = asyncio.create_task(clock())
        """
        operation = next_op()
        operation.show()
        response = input("\n")

        if float(response) == float(operation.perform()):
            correct += 1
        """
        input("testeando: ")
        correct += 1
    print("Correct answers: " + str(correct))
        

async def clock()->bool:
    print("starting clock...")
    await asyncio.sleep(5)
    print("finished clock.")

    return True

def next_op() -> op.Operation:
    op1 = random.randint(0, 10)
    op2 = random.randint(1, 10)
    operator = random.choice(MATH_OPERATORS)
    
    return op.Operation(op1, op2, operator)


if __name__ == "__main__":
    #asyncio.run(main())
    main()