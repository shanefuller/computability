from random import randint
from sat.clause import Clause
import random


class Sat:
    def __init__(self):
        self.clauses = []
        self.truth_assignment = []
        self.truth_values = []

        for x in range(300):
            self.clauses.append(Clause())

    def add_random_truth(self):
        for x in range(100):
            self.truth_assignment.append(random.choice([True, False]))

    def clause_value(self):
        for x in self.clauses:
            clause_values = []
            iteration = 0
            for t in x.clause:
                iteration = iteration + 1

                if t <= 100:
                    positive_literal = True
                else:
                    positive_literal = False

                if positive_literal:
                    value = self.truth_assignment[t - 1]
                else:
                    value = not (self.truth_assignment[t - 101])

                clause_values.append(value)

                #print(str(iteration) + ": " + str(clause_values))

            k = 0
            for j in clause_values:
                k = k + 1
                if j:
                    self.truth_values.append(True)
                    break
                elif k == 3:
                    self.truth_values.append(False)

            #print(self.truth_values)

    def reset_truth_values(self):
        self.truth_values = []

    def __str__(self):
        return "Clauses: {},\nTruth Assignment: {}".format(self.clauses, self.truth_assignment)

    def __repr__(self):
        return "Clauses: {},\nTruth Assignment: {}".format(self.clauses, self.truth_assignment)
