from .Weight import Weight
from .Temperature import Temperature
from .Length import Length
from Global import Global


class Converter:
    def __init__(self):
        self.choices = {
            "1": "Weight",
            "2": "Temperature",
            "3": "Length"
        }

        self.startChoice = {
            "Weight": lambda: Weight().Start(),
            "Temperature": lambda: Temperature().Start(),
            "Length": lambda: Length().Start()
        }
    def Start(self):
        while True:
            print("Converter".center(Global.HeaderFormatConstant, "="))
            
            for key, value in self.choices.items():
                print(f"{key}. {value}")

            print("0. Exit")
            print("=" * Global.HeaderFormatConstant)
            choiceNum = input(f"{"Choice":<{Global.TextFormatConstant}}: ")
            if choiceNum == "0":
                return
            
            if choiceNum not in self.choices:
                print("Choice Invalid")
                continue
            
            choice = self.choices[choiceNum]
            self.startChoice[choice]()