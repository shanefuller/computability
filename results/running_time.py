class RunningTime:
    def __init__(self, rt):
        self.running = rt
        self.average = (sum(rt) / len(rt))
        self.minimum = min(rt)
        self.median = 0
        self.maximum = max(rt)

    # printing out totals for running time table
    def print_results(self):
        print("Average: " + str(self.average))
        print("Minimum: " + str(self.minimum))
        print("Median: " + str(self.median))
        print("Maximum: " + str(self.maximum))

    # finding median
    def set_median(self):
        self.running.sort()
        if len(self.running) % 2 == 0:
            median1 = self.running[len(self.running) // 2]
            median2 = self.running[len(self.running) // 2 - 1]
            self.median = (median1 + median2) / 2
        else:
            self.median = self.running[len(self.running) // 2]

    def __str__(self):
        return "{}".format(self.running)

    def __repr__(self):
        return "{}".format(self.running)
