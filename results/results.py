class Results:
    def __init__(self, e, rt):
        self.efficacy = e
        self.running_time = rt

    def print_results(self):
        print("\n\nEFFICACY VALUES")
        print("*********************")
        print(self.efficacy.print_results())
        print("\n")
        print("RUNNING TIME VALUES")
        print("*******************")
        print(self.running_time.print_results())

    def __str__(self):
        return "Efficacy: {}\nRunning Time: {}".format(self.efficacy, self.running_time)
