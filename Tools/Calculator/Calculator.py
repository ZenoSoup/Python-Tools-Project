from Global import Global
from .ExpressionCalculator.ExpressionCalculator import ExpressionCalculator
from .GeometryCalculator.GeometryCalculator import GeometryCalculator
from .GradeCalculator.GradeCalculator import GradeCalculator
from .AgeCalculator.AgeCalculator import AgeCalculator

class Calculator:
    def __init__(self):
        self.choices = {
            "1": "Expression Calculator",
            "2": "Geometry Calculator",
            "3": "Grade Calculator",
            "4": "Age Calculator"
        }

        self.startChoice = {
            "Expression Calculator": lambda: ExpressionCalculator().Start(),
            "Geometry Calculator": lambda: GeometryCalculator().Start(),
            "Grade Calculator": lambda: GradeCalculator().Start(),
            "Age Calculator": lambda: AgeCalculator().Start()
        }

    def Start(self):
        while True:
            print("Calculator".center(Global.HeaderFormatConstant, "="))

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