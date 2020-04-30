from sat.clause import Clause
from results.results import Results
from results.totals import Totals
import time
import numpy

from sat.gsat import Gsat
from sat.sat import Sat


def unit_propagation(sat_instance):
    print(sat_instance)
    print(sat_instance.truth_assignment)

    w = sat_instance.clauses[0]
    index = 1

    while w in sat_instance.clauses:
        if w.clause_length() == 1:
            if w.clause[0] <= 100:
                positive_literal = True
            else:
                positive_literal = False

            if positive_literal:
                sat_instance.truth_assignment[(w.clause[0] - 1)] = True
                positive_version = w.clause[0]
                negative_version = w.clause[0] + 100
            else:
                sat_instance.truth_assignment[(w.clause[0] - 101)] = False
                negative_version = w.clause[0]
                positive_version = w.clause[0] - 100

            for p in sat_instance.clauses:
                if positive_version in p or negative_version in p:
                    sat_instance.clauses.remove(p)

            w = sat_instance.clauses[0]

        else:
            w = sat_instance.clauses[index]
            index += 1
            if index > len(sat_instance.clauses)-1:
                break



def dpll(sat_instances):
    totals = []
    running_times = []

    # running algorithm on all 1000 instances of sat
    for j in sat_instances:
        # reset truth values
        j.reset_truth_values()

        # start timer for individual run
        start = time.time()

        # add random truth assignments
        j.add_random_truth()

        # assign truth values within a single clause
        j.clause_value()

        # end timer for individual run
        end = time.time()

        # add totals and running times to arrays
        totals.append(j.count_satisfied())
        running_times.append((end - start))

    # return arrays of all efficacy and corresponding running times
    return Results(Totals(totals), Totals(running_times))


def gsat(sat_instances):
    totals = []
    running_times = []

    # running algorithm on all 1000 instances of knapsack
    for j in sat_instances:

        # reset truth values
        j.reset_truth_values()

        # start timer for individual run
        start = time.time()

        # set max try variable
        # max_try = 100
        max_try = 10

        # add random truth assignments
        j.add_random_truth()

        # assign truth value for random assignment
        j.clause_value()

        # start gsat loop
        for gs in range(max_try):
            gsat_instances = []
            for index in range((len(j.truth_assignment))):
                j.flip_truth_assignment(index)
                j.clause_value()
                gsat_instances.append(Gsat(index, j.count_unsatisfied(), j.truth_assignment[:]))
                j.flip_truth_assignment(index)

                index += 1

            best = len(j.clauses)

            for t in gsat_instances:
                if t.unsat <= best:
                    j.truth_assignment = t.current_truth_assignment[:]
                    best = t.unsat

            max_try += 1

        # assign truth value for final assignment
        j.clause_value()

        # end timer for individual run
        end = time.time()

        # add totals and running times to arrays
        totals.append(j.count_satisfied())
        running_times.append((end - start))

    # return arrays of all efficacy and corresponding running times
    return Results(Totals(totals), Totals(running_times))


def randomized_maxsat(sat_instances):
    totals = []
    running_times = []

    # running algorithm on all 1000 instances of knapsack
    for j in sat_instances:
        # reset truth values
        j.reset_truth_values()

        # start timer for individual run
        start = time.time()

        # add random truth assignments
        j.add_random_truth()

        # assign truth values within a single caluse
        j.clause_value()

        # end timer for individual run
        end = time.time()

        # add totals and running times to arrays
        totals.append(j.count_satisfied())
        running_times.append((end - start))

    # return arrays of all efficacy and corresponding running times
    return Results(Totals(totals), Totals(running_times))


# creating array to hold sat instances
sat_instances = []

# filling array with 1000 sat instances
for x in range(20):
    cx = Sat()
    sat_instances.append(cx)

sat_in = Sat()
sat_in.add_empty_truth()
unit_propagation(sat_in)

print(sat_in.truth_assignment)

# The DPLL algorithm.
# dpll_results = dpll(sat_instances)
# print("DPLL ALGORITHM")
# print("*************************************")
# print(str(dpll_results))
#
# p5_e = Totals(dpll_results.efficacy.eff)
#
# p5_rt = Totals(numpy.divide(dpll_results.running_time.eff,
#                             dpll_results.running_time.eff))
#
# print("\nQuality of Solutions")
# print("*************************************")
# print(p5_e.print_results())
#
# print("\nQuality of Running Time")
# print("*************************************")
# print(p5_rt.print_results())


# GSAT
# gsat_results = gsat(sat_instances)
# print("\n\nGSAT ALGORITHM")
# print("*************************************")
# print(str(gsat_results))
#
# # p6_e = Totals(numpy.divide(gsat_results.efficacy.eff,
# #                            gsat_results.efficacy.eff))
# #
# # p6_rt = Totals(numpy.divide(gsat_results.running_time.eff,
# #                             gsat_results.running_time.eff))
#
# p6_e = Totals(gsat_results.efficacy.eff)
#
# p6_rt = Totals(gsat_results.running_time.eff)
#
# print("\nQuality of Solutions")
# print("*************************************")
# print(p6_e.print_results())
#
# print("\nQuality of Running Time")
# print("*************************************")
# print(p6_rt.print_results())
#
# # The simple randomized 7/8 approximation algorithm for MAX3SAT.
# randomized_maxsat_results = randomized_maxsat(sat_instances)
# print("\n\nRANDOMIZED MAXSAT ALGORITHM")
# print("*************************************")
# print(str(randomized_maxsat_results))
#
# # p7_e = Totals(numpy.divide(randomized_maxsat_results.efficacy.eff,
# #                            randomized_maxsat_results.efficacy.eff))
# #
# # p7_rt = Totals(numpy.divide(randomized_maxsat_results.running_time.eff,
# #                             randomized_maxsat_results.running_time.eff))
#
# p7_e = Totals(randomized_maxsat_results.efficacy.eff)
#
# p7_rt = Totals(randomized_maxsat_results.running_time.eff)
#
# print("\nQuality of Solutions")
# print("*************************************")
# print(p7_e.print_results())
#
# print("\nQuality of Running Time")
# print("*************************************")
# print(p7_rt.print_results())
