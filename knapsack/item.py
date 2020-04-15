class Item:
    def __init__(self, v, w):
        self.value = v
        self.weight = w

    def __str__(self):
        return "Value : {}, Weight : {}".format(self.value, self.weight)

    def __repr__(self):
        return "Value : {}, Weight : {}".format(self.value, self.weight)
