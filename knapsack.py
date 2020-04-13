class Knapsack:
  def __init__(self, c):
    self.capacity = c

  def __str__(self):
    return "Capacity : {}".format(self.capacity)

c1 = Knapsack(74)
print(str(c1))
