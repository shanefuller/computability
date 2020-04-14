from knapsack import Knapsack

knapsack_instances = []

for x in range(100):
    cx = Knapsack()
    cx.add_items()
    knapsack_instances.append(cx)

for t in knapsack_instances:
    print(str(t))
