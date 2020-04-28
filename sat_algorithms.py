from sat.clause import Clause
from results.results import Results
from results.totals import Totals
import time
import numpy
from sat.sat import Sat

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

        # assign truth values within a single caluse
        j.clause_value()

        # end timer for individual run
        end = time.time()

        # count how many clauses result in truth
        total = 0
        for a in j.truth_values:
            if a:
                total = total + 1

        # add totals and running times to arrays
        totals.append(total)
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

        # add random truth assignments
        j.add_random_truth()

        # assign truth values within a single caluse
        j.clause_value()

        # end timer for individual run
        end = time.time()

        # count how many clauses result in truth
        total = 0
        for a in j.truth_values:
            if a:
                total = total + 1

        # add totals and running times to arrays
        totals.append(total)
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

        # count how many clauses result in truth
        total = 0
        for a in j.truth_values:
            if a:
                total = total + 1

        # add totals and running times to arrays
        totals.append(total)
        running_times.append((end - start))

    # return arrays of all efficacy and corresponding running times
    return Results(Totals(totals), Totals(running_times))


# creating array to hold sat instances
sat_instances = []

# filling array with 1000 sat instances
for x in range(1000):
    cx = Sat()
    sat_instances.append(cx)


# The DPLL algorithm.
dpll_results = dpll(sat_instances)
print("DPLL ALGORITHM")
print("*************************************")
print(str(dpll_results))

p5_e = Totals(numpy.divide(dpll_results.efficacy.eff,
                           dpll_results.efficacy.eff))

p5_rt = Totals(numpy.divide(dpll_results.running_time.eff,
                            dpll_results.running_time.eff))

print("\nQuality of Solutions")
print("*************************************")
print(p5_e.print_results())

print("\nQuality of Running Time")
print("*************************************")
print(p5_rt.print_results())



# GSAT
gsat_results = gsat(sat_instances)
print("\n\nGSAT ALGORITHM")
print("*************************************")
print(str(gsat_results))

p6_e = Totals(numpy.divide(gsat_results.efficacy.eff,
                           gsat_results.efficacy.eff))

p6_rt = Totals(numpy.divide(gsat_results.running_time.eff,
                            gsat_results.running_time.eff))

print("\nQuality of Solutions")
print("*************************************")
print(p6_e.print_results())

print("\nQuality of Running Time")
print("*************************************")
print(p6_rt.print_results())

# The simple randomized 7/8 approximation algorithm for MAX3SAT.
randomized_maxsat_results = randomized_maxsat(sat_instances)
print("\n\nRANDOMIZED MAXSAT ALGORITHM")
print("*************************************")
print(str(randomized_maxsat_results))

p7_e = Totals(numpy.divide(randomized_maxsat_results.efficacy.eff,
                           randomized_maxsat_results.efficacy.eff))

p7_rt = Totals(numpy.divide(randomized_maxsat_results.running_time.eff,
                            randomized_maxsat_results.running_time.eff))

print("\nQuality of Solutions")
print("*************************************")
print(p7_e.print_results())

print("\nQuality of Running Time")
print("*************************************")
print(p7_rt.print_results())