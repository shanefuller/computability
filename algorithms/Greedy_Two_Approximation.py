from knapsack.knapsack import Knapsack

# creating array to hold knapsack instances and value totals
knapsack_instances = []
totals = []
capacity_total = 0

# filling array with 1000 knapsack instances
for x in range(1000):
    cx = Knapsack()
    cx.add_items()
    cx.greedy_sort_items()
    knapsack_instances.append(cx)

# running algorithm on all 1000 instances of knapsack
for j in knapsack_instances:
    taken = []
    left = j.capacity
    total = 0

    print(str(j))
    print("Taken: " + str(taken))
    print("L: " + str(left))
    print("Total Value: " + str(total))

    for a in j.items:
        if left > 0:
            if a.weight <= left:
                taken.append(a)
                left = left-a.weight
                total = total+a.value
            else:
                print(str(a.weight) + " is greater than " + str(left))
        else:
            print(str(left) + " is less than 0")

    print(str(j))
    print("Taken: " + str(taken))
    print("L: " + str(left))
    print("Total Value: " + str(total))
    totals.append(total)
    capacity_total = capacity_total+j.capacity
    print("\n\n\n**********************")


# finding median
totals.sort()
if len(totals) % 2 == 0:
    median1 = totals[len(totals)//2]
    median2 = totals[len(totals)//2 - 1]
    median = (median1 + median2)/2
else:
    median = totals[len(totals)//2]

# printing out totals for efficacy in maximizing value
print("\n\n\n**********************")
print("Totals: " + str(totals))
print("Average: " + str(sum(totals)/len(totals)))
print("Minimum: " + str(min(totals)))
print("Median: " + str(median))
print("Maximum: " + str(max(totals)))
print("Sum of Totals: " + str(sum(totals)))
print("Sum of Capacity: " + str(capacity_total))
print("Average to Capacity: " + str(sum(totals)/capacity_total))


