class Totals:
    def __init__(self, e):
        self.eff = e
        self.average = (sum(e) / len(e))
        self.minimum = min(e)
        self.set_median()
        self.maximum = max(e)

    # printing out totals for efficacy table
    def print_results(self):
        print("Average: " + str(self.average))
        print("Minimum: " + str(self.minimum))
        print("Median: " + str(self.median))
        print("Maximum: " + str(self.maximum))
        return " "

    # finding median
    def set_median(self):
        self.eff.sort()
        if len(self.eff) % 2 == 0:
            median1 = self.eff[len(self.eff) // 2]
            median2 = self.eff[len(self.eff) // 2 - 1]
            self.median = (median1 + median2) / 2
        else:
            self.median = self.eff[len(self.eff) // 2]

    def __str__(self):
        return "{}".format(self.eff)

    def __repr__(self):
        return "{}".format(self.eff)
