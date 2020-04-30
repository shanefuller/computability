import random


class Clause:
    def __init__(self):
        self.clause = random.sample(range(1, 200), 3)
        # for x in self.clause:
        #     if x <= 100:
        #         if x+100 in self.clause:
        #             self.clause.replace

    def clause_length(self):
        return len(self.clause)

    def create_unit_clause(self, unit):
        self.clause.pop(0)
        self.clause.pop(0)
        self.clause[0] = unit

    def find_value(self, val):
        if val in self.clause:
            return True
        else:
            return False

    def __str__(self):
        result = "["
        for t in range(len(self.clause) + 1):
            if t < len(self.clause) - 1:
                result = result + str(self.clause[t]) + " V "
            elif t == len(self.clause) - 1:
                result = result + str(self.clause[t]) + "]"

        return result

    def __repr__(self):
        result = "["
        for t in range(len(self.clause)+1):
            if t < len(self.clause)-1:
                result = result + str(self.clause[t]) + " V "
            elif t == len(self.clause)-1:
                result = result + str(self.clause[t]) + "]"

        return result
