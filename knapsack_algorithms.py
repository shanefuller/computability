from knapsack.knapsack import Knapsack
from results.results import Results
from results.totals import Totals
import time
import numpy


def optimal_dynamic_programming(knapsack_instances):
    totals = []
    running_times = []

    # running algorithm on all instances of knapsack
    for j in knapsack_instances:

        # start timer for individual run
        start = time.time()

        # create array to store values, initialize to 0
        arr = numpy.empty((len(j.items) + 1, j.capacity + 1))

        # set value of taking items with no capacity to 0
        for b in range((len(j.items) + 1)):
            arr[b][0] = 0

        # set value of no more items left equal to 0
        for v in range(j.capacity + 1):
            arr[(len(j.items))][v] = 0

        # initialize value for loop
        val = (len(j.items) - 1)

        # begin dynamic programming algorithm from CS305
        for w in range(val, -1, -1):
            for z in range(j.capacity + 1):
                if j.items[w].weight <= z:
                    arr[w, z] = max(arr[(w + 1)][(z - j.items[w].weight)]+j.items[w].value, arr[(w + 1)][z])
                else:
                    arr[w, z] = arr[(w + 1)][z]

        # end timer for individual run
        end = time.time()

        # add totals and running times to arrays
        totals.append(arr[0, j.capacity])
        running_times.append((end - start))

    # return arrays of all efficacy and corresponding running times
    return Results(Totals(totals), Totals(running_times))


def min_cost(knapsack_instances):
    totals = []
    running_times = []

    # running algorithm on all instances of knapsack
    for j in knapsack_instances:

        # start timer for individual run
        start = time.time()

        # create variables
        a_max = j.max_value()

        # create array to store values, initialize to 0
        min_arr = numpy.empty((len(j.items), (len(j.items)*a_max)))

        # set value of taking items with no capacity to 0
        for b in range((len(j.items))):
            min_arr[b][0] = 0

        # set value of no more items left equal to 0
        for v in range(j.capacity):
            min_arr[(len(j.items))][v] = 0

        # initialize value for loop
        val = (len(j.items) - 1)

        # begin dynamic programming algorithm from CS305
        for w in range(val, -1, -1):
            for z in range(j.capacity)+1:
                if j.items[w].weight <= z:
                    min_arr[w, z] = max(min_arr[(w + 1)][(z - j.items[w].weight)] + j.items[w].value, min_arr[(w + 1)][z])
                else:
                    min_arr[w, z] = min_arr[(w + 1)][z]

        # end timer for individual run
        end = time.time()

        # add totals and running times to arrays
        totals.append(min_arr[0, j.capacity])
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

        # sort items in knapsack
        j.greedy_sort_items()

        # create variables for what is taken, and sum of values taken
        taken = []
        left = j.capacity
        total = 0

        # start greedy two approximation algorithm
        for a in j.items:
            if left > 0:
                if a.weight <= left:
                    taken.append(a)
                    left = left - a.weight
                    total = total + a.value
                else:
                    pass
            else:
                pass

        # end timer for individual run
        end = time.time()

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

        # unsort items from greedy two approximation
        j.unsort_items()

        # start timer for individual run
        start = time.time()

        # create variables for what is taken, and sum of values taken
        taken = []
        left = j.capacity
        total = 0

        # start greedy two approximation algorithm
        for a in j.items:
            if left > 0:
                if a.weight <= left:
                    taken.append(a)
                    left = left - a.weight
                    total = total + a.value
                else:
                    pass
            else:
                pass

        # end timer for individual run
        end = time.time()

        # add totals and running times to arrays
        totals.append(total)
        running_times.append((end - start))

    # return arrays of all efficacy and corresponding running times
    return Results(Totals(totals), Totals(running_times))


# creating array to hold knapsack instances
k_instances = []

# filling array with 1000 knapsack instances
for x in range(3):
    cx = Knapsack()
    k_instances.append(cx)

# The O(nW) dynamic programming algorithm that we discussed in CS305.
optimal_dynamic_programming_results = optimal_dynamic_programming(k_instances)
print("OPTIMAL DYNAMIC PROGRAMMING ALGORITHM")
print("*************************************")
print(str(optimal_dynamic_programming_results))

# p1_e = Totals(numpy.divide(optimal_dynamic_programming_results.efficacy.eff,
# #                            optimal_dynamic_programming_results.efficacy.eff))
# #
# # p1_rt = Totals(numpy.divide(optimal_dynamic_programming_results.running_time.eff,
# #                             optimal_dynamic_programming_results.running_time.eff))

p1_e = Totals(optimal_dynamic_programming_results.efficacy.eff)
p1_rt = Totals(optimal_dynamic_programming_results.running_time.eff)

print("\nQuality of Solutions")
print("*************************************")
print(p1_e.print_results())

print("\nQuality of Running Time")
print("*************************************")
print(p1_rt.print_results())

# # The O(n·v(amax)) dynamic programming algorithm from the textbook based on the MinCost version of the problem.
# min_cost_results = min_cost(k_instances)
# print("\n\nMIN COST ALGORITHM")
# print("*************************************")
# print(str(min_cost_results))
#
# # p2_e = Totals(numpy.divide(min_cost_results.efficacy.eff,
# #                            optimal_dynamic_programming_results.efficacy.eff))
# #
# # p2_rt = Totals(numpy.divide(min_cost_results.running_time.eff,
# #                             optimal_dynamic_programming_results.running_time.eff))
#
# p2_e = Totals(min_cost_results.efficacy.eff)
# p2_rt = Totals(min_cost_results.running_time.eff)
#
# print("\nQuality of Solutions")
# print("*************************************")
# print(p2_e.print_results())
#
# print("\nQuality of Running Time")
# print("*************************************")
# print(p2_rt.print_results())



# The greedy 2-approximation from the textbook.
greedy_two_approximation_results = greedy_two_approximation(k_instances)
print("\n\nGREEDY TWO APPROXIMATION ALGORITHM")
print("*************************************")
print(str(greedy_two_approximation_results))

# p3_e = Totals(numpy.divide(optimal_dynamic_programming_results.efficacy.eff,
#                            greedy_two_approximation_results.efficacy.eff))
#
# p3_rt = Totals(numpy.divide(optimal_dynamic_programming_results.running_time.eff,
#                             greedy_two_approximation_results.running_time.eff))

p3_e = Totals(greedy_two_approximation_results.efficacy.eff)
p3_rt = Totals(greedy_two_approximation_results.running_time.eff)

print("\nQuality of Solutions")
print("*************************************")
print(p3_e.print_results())

print("\nQuality of Running Time")
print("*************************************")
print(p3_rt.print_results())



# # The FPTAS based on scaling with the optimal dynamic programming algorithm from (2) above.
# fptas_results = fptas(k_instances)
# print("\n\nFPTAS ALGORITHM")
# print("*************************************")
# print(str(fptas_results))
#
# p4_e = Totals(numpy.divide(fptas_results.efficacy.eff,
#                            optimal_dynamic_programming_results.efficacy.eff))
#
# p4_rt = Totals(numpy.divide(fptas_results.running_time.eff,
#                             optimal_dynamic_programming_results.running_time.eff))
#
# print("\nQuality of Solutions")
# print("*************************************")
# print(p4_e.print_results())
#
# print("\nQuality of Running Time")
# print("*************************************")
# print(p4_rt.print_results())
