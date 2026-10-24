from Global import Global
from Helper import Helper
import math


class Circle:
    def __init__(self):
        # Change this to set the decimal digit precision
        self.precision = 3

    def Start(self):
        while True:
            print("Circle".center(Global.HeaderFormatConstant, "="))
            diameter = Helper.inputFloat(
                f"{"Enter the Diameter of the Circle":<{Global.TextFormatConstant}}: ",
                min_val=0.000001,
            )

            radius = diameter / 2
            perimeter = self.CalculatePerimeter(radius)
            area = self.CalculateArea(radius)

            print("=" * Global.HeaderFormatConstant)

            print(
                f"{"The perimeter of the Circle is":<{Global.TextFormatConstant}}: {perimeter}"
            )
            print(f"{"The Area of the Circle is":<{Global.TextFormatConstant}}: {area}")

            if not Helper.inputConfirmation(
                f"{"Calculate again? (Y/N)":<{Global.TextFormatConstant}}: "
            ):
                return

    def CalculatePerimeter(self, radius):
        return round((2 * math.pi * radius), self.precision)

    def CalculateArea(self, radius):
        return round(math.pi * (radius**2), self.precision)
