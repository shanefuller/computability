import random


class Gsat:
    def __init__(self, i, u, cta):
        self.index = i
        self.unsat = u
        self.current_truth_assignment = cta

    def __str__(self):
        return "\nIndex Switched: {}\nUnsatisfied Clauses: {}\nCurrent Truth Assignment: {}]\n".format(self.index, self.unsat, self.current_truth_assignment)

    def __repr__(self):
        return "\nIndex Switched: {}\nUnsatisfied Clauses: {}\nCurrent Truth Assignment: {}]\n".format(self.index, self.unsat, self.current_truth_assignment)
