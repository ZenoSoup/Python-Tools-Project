class Helper:
    @staticmethod
    def inputInt(prompt: str, min_val: int = None, max_val: int = None):
        while True:
            try:
                val = int(input(prompt))
                if min_val is not None and val < min_val:
                    print(f"Value must be at least {min_val}")
                    continue
                if max_val is not None and val > max_val:
                    print(f"Value must be at most {max_val}")
                    continue
                return val
            except ValueError:
                print("Please only enter an integer value")

    @staticmethod
    def inputFloat(prompt: str, min_val: float = None, max_val: float = None):
        while True:
            try:
                val = float(input(prompt))
                if min_val is not None and val < min_val:
                    print(f"Value must be at least {min_val}")
                    continue
                if max_val is not None and val > max_val:
                    print(f"Value must be at most {max_val}")
                    continue
                return val
            except ValueError:
                print("Please only enter a float value")

    @staticmethod
    def inputConfirmation(prompt: str):
        while True:
            confirmation = input(prompt).strip().upper()

            if confirmation == "Y":
                return True

            elif confirmation == "N":
                return False

            else:
                print("Please only enter Y/N")
                continue
