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

    def inputConfirmation(prompt):
        while True:
            confirmation = input(prompt).upper()

            if confirmation == "Y":
                return True

            elif confirmation == "N":
                return False
            
            else:
                print("Please only enter Y/N")
                continue
