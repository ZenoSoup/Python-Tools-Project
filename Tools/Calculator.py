import math


class Calculator:
    def __init__(self):
        self.allowed_names = {
            "sqrt": math.sqrt,
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "pi": math.pi,
            "e": math.e,
        }

    def Start(self):
        while True:
            try:
                print('Type "Return" to get back to the main menu')
                Masukan = input("Enter Expression: ")

                if Masukan.lower() == "exit":
                    return

                self.Calculate(Masukan)

            except Exception as e:
                print(f"error: {e}")

    def Calculate(self, userInput):
        result = eval(userInput, {"__builtins__": None}, self.allowed_names)
        print(f"Result: {result:.2f}")
