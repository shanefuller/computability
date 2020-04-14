from random import seed
from random import randint
from item import Item


class Knapsack:
    def __init__(self):
        self.capacity = randint(3000, 4000)
        self.items = []

    def add_items(self):
        for x in range(500):
            val = randint(1, 50)
            wei = randint(1, 50)
            self.items.append(Item(val, wei))

    def greedy_sort_items(self):
        self.items = sorted(self.items, key=lambda item: item.value / item.weight, reverse=True)

    def __str__(self):
        return "Capacity: {}, Items: {}".format(self.capacity, self.items)
