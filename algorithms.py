from knapsack.knapsack import Knapsack
from results.results import Results
from results.totals import Totals
import time
import numpy

from results.totals import Totals


def optimal_dynamic_programming(knapsack_instances):
    totals = []
    running_times = []

    # running algorithm on all 1000 instances of knapsack
    for j in knapsack_instances:

        # start timer for individual run
        start = time.time()

        # create variables for what is taken, and sum of values taken
        taken = []
        left = j.capacity
        total = 0

        # print introduction to algorithm
        # print("BEFORE GREEDY TWO APPROXIMATION ALGORITHM RUN")
        # print(str(j))
        # print("Taken: " + str(taken))
        # print("L: " + str(left))

        # start greedy two approximation algorithm
        for a in j.items:
            if left > 0:
                if a.weight <= left:
                    taken.append(a)
                    left = left - a.weight
                    total = total + a.value
                else:
                    pass
                    # print(str(a.weight) + " is greater than " + str(left))
            else:
                pass
                # print(str(left) + ": taken as much as possible")

        # end timer for individual run
        end = time.time()

        # print results for individual run
        # print("AFTER GREEDY TWO APPROXIMATION ALGORITHM RUN")
        # print("Taken: " + str(taken))
        # print("L: " + str(left))
        # print("\nTotal Value: " + str(total))
        # print("Total Time: " + str(start - end))
        # print("\n************************************")

        # add totals and running times to arrays
        totals.append(total)
        running_times.append((end - start))

    # return arrays of all efficacy and corresponding running times
    return Results(Totals(totals), Totals(running_times))


def min_cost(knapsack_instances):
    totals = []
    running_times = []

    # running algorithm on all 1000 instances of knapsack
    for j in knapsack_instances:

        # start timer for individual run
        start = time.time()

        # create variables for what is taken, and sum of values taken
        taken = []
        left = j.capacity
        total = 0

        # print introduction to algorithm
        # print("BEFORE GREEDY TWO APPROXIMATION ALGORITHM RUN")
        # print(str(j))
        # print("Taken: " + str(taken))
        # print("L: " + str(left))

        # start greedy two approximation algorithm
        for a in j.items:
            if left > 0:
                if a.weight <= left:
                    taken.append(a)
                    left = left - a.weight
                    total = total + a.value
                else:
                    pass
                    # print(str(a.weight) + " is greater than " + str(left))
            else:
                pass
                # print(str(left) + ": taken as much as possible")

        # end timer for individual run
        end = time.time()

        # print results for individual run
        # print("AFTER GREEDY TWO APPROXIMATION ALGORITHM RUN")
        # print("Taken: " + str(taken))
        # print("L: " + str(left))
        # print("\nTotal Value: " + str(total))
        # print("Total Time: " + str(start - end))
        # print("\n************************************")

        # add totals and running times to arrays
        totals.append(total)
        running_times.append((end - start))

    # return arrays of all efficacy and corresponding running times
    return Results(Totals(totals), Totals(running_times))


def greedy_two_approximation(knapsack_instances):
    totals = []
    running_times = []

    # running algorithm on all 1000 instances of knapsack
    for j in knapsack_instances:

        # start timer for individual run
        start = time.time()

        # create variables for what is taken, and sum of values taken
        taken = []
        left = j.capacity
        total = 0

        # print introduction to algorithm
        # print("BEFORE GREEDY TWO APPROXIMATION ALGORITHM RUN")
        # print(str(j))
        # print("Taken: " + str(taken))
        # print("L: " + str(left))

        # start greedy two approximation algorithm
        for a in j.items:
            if left > 0:
                if a.weight <= left:
                    taken.append(a)
                    left = left - a.weight
                    total = total + a.value
                else:
                    pass
                    # print(str(a.weight) + " is greater than " + str(left))
            else:
                pass
                # print(str(left) + ": taken as much as possible")

        # end timer for individual run
        end = time.time()

        # print results for individual run
        # print("AFTER GREEDY TWO APPROXIMATION ALGORITHM RUN")
        # print("Taken: " + str(taken))
        # print("L: " + str(left))
        # print("\nTotal Value: " + str(total))
        # print("Total Time: " + str(start - end))
        # print("\n************************************")

        # add totals and running times to arrays
        totals.append(total)
        running_times.append((end - start))

    # return arrays of all efficacy and corresponding running times
    return Results(Totals(totals), Totals(running_times))


def fptas(knapsack_instances):
    totals = []
    running_times = []

    # running algorithm on all 1000 instances of knapsack
    for j in knapsack_instances:

        # start timer for individual run
        start = time.time()

        # create variables for what is taken, and sum of values taken
        taken = []
        left = j.capacity
        total = 0

        # print introduction to algorithm
        # print("BEFORE GREEDY TWO APPROXIMATION ALGORITHM RUN")
        # print(str(j))
        # print("Taken: " + str(taken))
        # print("L: " + str(left))

        # start greedy two approximation algorithm
        for a in j.items:
            if left > 0:
                if a.weight <= left:
                    taken.append(a)
                    left = left - a.weight
                    total = total + a.value
                else:
                    pass
                    # print(str(a.weight) + " is greater than " + str(left))
            else:
                pass
                # print(str(left) + ": taken as much as possible")

        # end timer for individual run
        end = time.time()

        # print results for individual run
        # print("AFTER GREEDY TWO APPROXIMATION ALGORITHM RUN")
        # print("Taken: " + str(taken))
        # print("L: " + str(left))
        # print("\nTotal Value: " + str(total))
        # print("Total Time: " + str(start - end))
        # print("\n************************************")

        # add totals and running times to arrays
        totals.append(total)
        running_times.append((end - start))

    # return arrays of all efficacy and corresponding running times
    return Results(Totals(totals), Totals(running_times))


# creating array to hold knapsack instances
k_instances = []

# filling array with 1000 knapsack instances
for x in range(1000):
    cx = Knapsack()
    cx.add_items()
    cx.greedy_sort_items()
    k_instances.append(cx)

# The O(nW) dynamic programming algorithm that we discussed in CS305.
optimal_dynamic_programming_results = optimal_dynamic_programming(k_instances)
print("OPTIMAL DYNAMIC PROGRAMMING ALGORITHM")
print("*************************************")
print(str(optimal_dynamic_programming_results))

p1_e = Totals(numpy.divide(optimal_dynamic_programming_results.efficacy.eff,
                           optimal_dynamic_programming_results.efficacy.eff))

p1_rt = Totals(numpy.divide(optimal_dynamic_programming_results.running_time.eff,
                            optimal_dynamic_programming_results.running_time.eff))

print("\nQuality of Solutions")
print("*************************************")
print(p1_e)

print("\nQuality of Running Time")
print("*************************************")
print(p1_rt.print_results())

# The O(n·v(amax)) dynamic programming algorithm from the textbook based on the MinCost version of the problem.
min_cost_results = min_cost(k_instances)
print("\n\nMIN COST ALGORITHM")
print("*************************************")
print(str(min_cost_results))

p2_e = Totals(numpy.divide(min_cost_results.efficacy.eff,
                           optimal_dynamic_programming_results.efficacy.eff))

p2_rt = Totals(numpy.divide(min_cost_results.running_time.eff,
                            optimal_dynamic_programming_results.running_time.eff))

print("\nQuality of Solutions")
print("*************************************")
print(p2_e.print_results())

print("\nQuality of Running Time")
print("*************************************")
print(p2_rt.print_results())

# The greedy 2-approximation from the textbook.
greedy_two_approximation_results = greedy_two_approximation(k_instances)
print("\n\nGREEDY TWO APPROXIMATION ALGORITHM")
print("*************************************")
print(str(greedy_two_approximation_results))

p3_e = Totals(numpy.divide(greedy_two_approximation_results.efficacy.eff,
                           greedy_two_approximation_results.efficacy.eff))

p3_rt = Totals(numpy.divide(greedy_two_approximation_results.running_time.eff,
                            greedy_two_approximation_results.running_time.eff))

print("\nQuality of Solutions")
print("*************************************")
print(p3_e.print_results())

print("\nQuality of Running Time")
print("*************************************")
print(p3_rt.print_results())

# The FPTAS based on scaling with the optimal dynamic programming algorithm from (2) above.
fptas_results = fptas(k_instances)
print("\n\nFPTAS ALGORITHM")
print("*************************************")
print(str(fptas_results))

p4_e = Totals(numpy.divide(fptas_results.efficacy.eff,
                           fptas_results.efficacy.eff))

p4_rt = Totals(numpy.divide(fptas_results.running_time.eff,
                            fptas_results.running_time.eff))

print("\nQuality of Solutions")
print("*************************************")
print(p4_e.print_results())

print("\nQuality of Running Time")
print("*************************************")
print(p4_rt.print_results())
