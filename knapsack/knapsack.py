import math
from random import randint
from knapsack.item import Item
import random


class Knapsack:
    def __init__(self):
        self.capacity = randint(3000, 4000)
        # self.capacity = randint(25, 100)
        self.items = []

        # for x in range(3):
        for x in range(500):
            val = randint(1, 100)
            wei = randint(1, 50)
            self.items.append(Item(val, wei))

    def greedy_sort_items(self):
        return sorted(self.items, key=lambda item: item.value / item.weight, reverse=True)

    def unsort_items(self):
        random.shuffle(self.items)

    def max_value(self):
        mx = 0
        for t in self.items:
            if t.value >= mx:
                mx = t.value
            else:
                pass
        return mx

    def fptas_scaling(self, max, epsilon):
        for q in self.items:
            q.value = q.value/max
            q.value = q.value*len(self.items)
            q.value = q.value/epsilon
            q.value = math.floor(q.value)

    def __str__(self):
        return "Capacity: {}, Items: {}".format(self.capacity, self.items)

    def __repr__(self):
        return "Capacity: {}, Items: {}".format(self.capacity, self.items)
