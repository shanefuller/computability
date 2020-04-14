from knapsack import Knapsack

knapsack_instances = []
knap = Knapsack()
knap.add_items()

knapSort = sorted(knap.items, key=lambda item: item.value/item.weight, reverse=True)
knap.add_sort_items(knapSort)

taken = []
left = knap.capacity
sums = 0

print(str(knap))
print("Taken: " + str(taken))
print("L: " + str(left))
print("Sum: " + str(sums))

for a in knap.items:
    if left > 0:
        if a.weight <= left:
            taken.append(a)
            left = left-a.weight
            sums = sums+a.value
        else:
            print(str(a.weight) + " is greater than " + str(left))
    else:
        print(str(left) + " is less than 0")


print("Taken: " + str(taken))
print("L: " + str(left))
print("Sum: " + str(sums))



# for x in range(100):
#     cx = Knapsack()
#     cx.add_items()
#     knapsack_instances.append(cx)

# for t in knapsack_instances:
#     print(str(t))


