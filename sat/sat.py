from random import randint
from sat.clause import Clause
import random


class Sat:
    def __init__(self):
        self.clauses = []
        self.truth_assignment = []
        self.truth_values = []

        for x in range(300):
        #for x in range(18):
            self.clauses.append(Clause())

    def add_random_truth(self):
        for x in range(100):
        #for x in range(6):
            self.truth_assignment.append(random.choice([True, False]))

    def add_empty_truth(self):
        self.truth_assignment = [None] * len(self.clauses)

    def clause_value(self):
        self.truth_values = []
        for x in self.clauses:
            clause_values = []
            iteration = 0
            for t in x.clause:
                iteration = iteration + 1

                # print(str(iteration))
                # print(len(self.clauses))
                # print(len(self.truth_assignment))

                if t <= len(self.truth_assignment):
                    positive_literal = True
                else:
                    positive_literal = False

                if positive_literal:
                    value = self.truth_assignment[t - 1]
                else:
                    value = not (self.truth_assignment[t - 101])

                clause_values.append(value)

                # print(str(iteration) + ": " + str(clause_values))

            # self.truth_values.append(clause_values)
            k = 0
            for j in clause_values:
                k = k + 1
                if j:
                    self.truth_values.append(True)
                    break
                elif k == 3:
                    self.truth_values.append(False)

            # print(self.truth_values)

    def flip_truth_assignment(self, assignment):
        if self.truth_assignment[assignment]:
            self.truth_assignment[assignment] = False
        else:
            self.truth_assignment[assignment] = True

    def count_satisfied(self):
        total = 0
        for a in self.truth_values:
            if a:
                total = total + 1

        return total

    def count_unsatisfied(self):
        total = 0
        for a in self.truth_values:
            if not a:
                total = total + 1

        return total

    def reset_truth_values(self):
        self.truth_values = []

    def __str__(self):
        return "Clauses: {},\nTruth Assignment: {}".format(self.clauses, self.truth_assignment)

    def __repr__(self):
        return "Clauses: {},\nTruth Assignment: {}".format(self.clauses, self.truth_assignment)
