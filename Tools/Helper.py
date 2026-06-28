class Helper:
    def inputInt(prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Please only enter an integer value")

    def inputFloat(prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Please only enter a float value")
