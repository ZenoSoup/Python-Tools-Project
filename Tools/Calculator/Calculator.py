import math
from Global import Global


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
                print("Calculator".center(Global.HeaderFormatConstant, "="))
                print('Type "exit" to get back to the main menu')
                expression = input("Enter Expression: ")

                if expression.lower() == "exit":
                    return

                result = self.Calculate(expression)
                print(f"{"Result":{Global.TextFormatConstant}}: {result:.2f}")

            except Exception as e:
                print(f"{"error":{Global.TextFormatConstant}}: {e}")

    def Calculate(self, userInput):
        return eval(userInput, {"__builtins__": None}, self.allowed_names)
