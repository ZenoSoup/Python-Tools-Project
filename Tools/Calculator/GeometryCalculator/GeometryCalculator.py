from Global import Global
from .Square import Square
from .Rectangle import Rectangle
from .Triangle import Triangle
from .Circle import Circle


class GeometryCalculator:
    def __init__(self):
        self.shapes = {"1": "Square", "2": "Rectangle", "3": "Circle", "4": "Triangle"}

        self.shapesStart = {
            "Square": lambda: Square().Start(),
            "Rectangle": lambda: Rectangle().Start(),
            "Circle": lambda: Circle().Start(),
            "Triangle": lambda: Triangle().Start(),
        }

    def Start(self):
        while True:
            print("Geometry Calculator".center(Global.HeaderFormatConstant, "="))

            for key, value in self.shapes.items():
                print(f"{key}. {value}")

            print("0. Exit")
            print("=" * Global.HeaderFormatConstant)
            choiceNum = input(f"{"Choice":<{Global.TextFormatConstant}}: ")

            if choiceNum == "0":
                return

            if choiceNum not in self.shapes:
                print("Input Invalid")

            choice = self.shapes[choiceNum]
            self.shapesStart[choice]()
