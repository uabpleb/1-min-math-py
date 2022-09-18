import collections


class Algorithms:
    def __init__(self):
        pass

    #TODO: find multiplicity
    def divisor_generator(n: int)->list[int]:
        l = []
        for i in range(1, (n/2)+1):
            if n % i == 0:
                l.append(i)
        return l