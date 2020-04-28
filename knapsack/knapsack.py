from random import randint
from knapsack.item import Item
import random


class Knapsack:
    def __init__(self):
        self.capacity = randint(3000, 4000)
        self.target = randint(3000, 4000)
        self.items = []

        for x in range(500):
            val = randint(1, 50)
            wei = randint(1, 50)
            self.items.append(Item(val, wei))

    def greedy_sort_items(self):
        self.items = sorted(self.items, key=lambda item: item.value / item.weight, reverse=True)

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

    def __str__(self):
        return "Capacity: {}, Items: {}".format(self.capacity, self.items)

    def __repr__(self):
        return "Capacity: {}, Items: {}".format(self.capacity, self.items)
