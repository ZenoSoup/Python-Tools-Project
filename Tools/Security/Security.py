from Global import Global
from .PasswordGenerator import PasswordGenerator

"""
    Genuinely don't know what else to put in here other than Password Generator
"""
class Security:
    def __init__(self):
        self.choices = {
            "1": "Password Generator"
        }

        self.startChoice = {
            "Password Generator": lambda: PasswordGenerator().Start()
        }
    def Start(self):
        while True:
            print("Security".center(Global.HeaderFormatConstant, "="))

            for key, value in self.choices.items():
                print(f"{key}. {value}")
                
            print("0. Exit")
            print("=" * Global.HeaderFormatConstant)

            choiceNum = input(f"{"Choice":<{Global.TextFormatConstant}}: ")

            if choiceNum == "0":
                return
            
            if choiceNum not in self.choices:
                print("Invalid Input")
                continue
            
            choice = self.choices[choiceNum]
            self.startChoice[choice]()