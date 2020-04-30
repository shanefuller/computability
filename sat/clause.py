import random


class Clause:
    def __init__(self):
        self.clause = random.sample(range(1, 200), 3)

    def clause_length(self):
        return len(self.clause)

    def __str__(self):
        return "[{} V {} V {}]".format(self.clause[0], self.clause[1], self.clause[2])

    def __repr__(self):
        return "[{} V {} V {}]".format(self.clause[0], self.clause[1], self.clause[2])
