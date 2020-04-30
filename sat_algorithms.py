from sat.clause import Clause
from results.results import Results
from results.totals import Totals
import time
import numpy

from sat.gsat import Gsat
from sat.sat import Sat


def unit_propagation(formula, truth_assignment_so_far):
    # setting initial values for loop and index
    w = formula[0]
    index = 1

    # find unit clause

    while w in formula:

        # if the clause is a unit clause
        if w.clause_length() == 1:

            # identify if positive or negative literal
            if w.clause[0] <= 100:
                positive_literal = True
            else:
                positive_literal = False

            # assign truth to assignment so far, identify negation for removing from clauses
            if positive_literal:
                truth_assignment_so_far[(w.clause[0] - 1)] = True
                positive_version = w.clause[0]
                negative_version = w.clause[0] + 100
            else:
                truth_assignment_so_far[(w.clause[0] - 101)] = False
                negative_version = w.clause[0]
                positive_version = w.clause[0] - 100

            previous_remove = False
            index = 0
            print("Range: " + str(range(len(formula))))
            count = 0

            # remove unit clause and negation from current iteration of clauses
            for index in range(len(formula)):
                if previous_remove:
                    index -= 1

                print("Removed: " + str(count))
                print(str(index) + ": " + str(formula[index]))
                print(positive_version)
                print(negative_version)

                print(formula[index].find_value(positive_version))
                print(formula[index].find_value(negative_version))

                if formula[index].find_value(positive_version):
                    formula.remove(formula[index])
                    previous_remove = True
                    count += 1
                elif formula[index].find_value(negative_version):
                    formula.remove(formula[index])
                    previous_remove = True
                    count += 1
                else:
                    previous_remove = False

                print("**********************")
                print(formula)
                print(previous_remove)
                print("here")
                print("**********************")
                print(index)
                index += 1
                print(index)
                if index >= len(formula)-1:
                    break

            # return back to first clause and restart process of looking for unit clauses
            w = formula[0]

        # if not a unit clause, set to next clause, check and see if more clauses to go to
        else:
            w = formula[index]
            index += 1
            if index > len(formula) - 1:
                break

    # returning the remaining formula and truth assignment
    return formula, truth_assignment_so_far


def run_dpll(formula_so_far, truth_so_far):
    # begin dpll by calling unit prop
    new_formula, new_assignment = unit_propagation(formula_so_far[:], truth_so_far[:])

    print(new_formula)
    print(new_assignment)

    # satisfiable instance
    if len(new_formula) == 0:
        # end timer for individual run
        end = time.time()

        # go to next sat instance
        return True

    # # unsatisfiable instance
    # if len(new_formula) > 0:
    #
    #     # end timer for individual run
    #     end = time.time()
    #
    #     # add totals and running times to arrays
    #     totals.append(1)
    #     running_times.append((end - start))
    #
    #     # go to next sat instance
    #     return False

    # find first variable unassigned in new_assignment
    first_unassigned_literal = 0
    for q in range(len(new_assignment)):
        if new_assignment[q] is None:
            first_unassigned_literal = q + 1
            break

    # create unit clause and add to formula
    unit_clause = Clause()
    unit_clause.create_unit_clause(first_unassigned_literal)
    new_formula.insert(0, unit_clause)

    # add to truth assignment
    new_assignment[first_unassigned_literal - 1] = True
    new_assignment[first_unassigned_literal + 99] = False

    # # add to truth assignment
    # if first_unassigned_literal <= 100:
    #     new_assignment[first_unassigned_literal-1] = True
    #     new_assignment[first_unassigned_literal+99] = False
    # else:
    #     new_assignment[first_unassigned_literal-1] = False
    #     new_assignment[first_unassigned_literal-101] = True

    print(new_assignment)
    print(new_formula)

    # recursively run dpll
    result = run_dpll(new_formula[:], new_assignment[:])

    if result:
        return True
    else:
        # create unit clause and add to formula
        unit_clause = Clause()
        unit_clause.create_unit_clause(first_unassigned_literal + 100)
        new_formula.insert(0, unit_clause)

        # add to truth assignment
        new_assignment[first_unassigned_literal - 1] = False
        new_assignment[first_unassigned_literal + 99] = True

        return run_dpll(new_formula[:], new_assignment[:])


def dpll(sat_instances):
    totals = []
    running_times = []

    # running algorithm on all 1000 instances of sat
    for j in sat_instances:

        # start timer for individual run
        start = time.time()

        # add random truth assignments
        j.add_empty_truth()

        # begin dpll algorithm
        result = run_dpll(j.clauses, j.truth_assignment)

        # add totals to array
        if result:
            totals.append(300)
        else:
            totals.append(1)

        # end timer for individual run
        end = time.time()

        # add running time to array
        running_times.append((end - start))

    # return arrays of all efficacy and corresponding running times
    return Results(Totals(totals), Totals(running_times))


def gsat(sat_instances):
    totals = []
    running_times = []

    # running algorithm on all 1000 instances of knapsack
    for j in sat_instances:

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

    # running algorithm on all instances of sat
    for j in sat_instances:
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
for x in range(1):
    cx = Sat()
    sat_instances.append(cx)

# The DPLL algorithm.
dpll_results = dpll(sat_instances)
print("DPLL ALGORITHM")
print("*************************************")
print(str(dpll_results))

# p5_e = Totals(numpy.divide(dpll_results.efficacy.eff,
#                            dpll_results.efficacy.eff))
#
# p5_rt = Totals(numpy.divide(dpll_results.running_time.eff,
#                             dpll_results.running_time.eff))

p5_e = Totals(dpll_results.efficacy.eff)

p5_rt = Totals(dpll_results.running_time.eff)

print("\nQuality of Solutions")
print("*************************************")
print(p5_e.print_results())

print("\nQuality of Running Time")
print("*************************************")
print(p5_rt.print_results())

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
