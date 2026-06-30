from Global import Global
from Helper import Helper


class Square:
    def Start(self):
        print("Rectangle".center(Global.HeaderFormatConstant, "="))
        side = Helper.inputFloat(
            f"{"Enter the side of the Square":<{Global.TextFormatConstant}}: "
        )

        perimeter = self.CalculatePerimeter(side)
        area = self.CalculateArea(side)

        print("=" * Global.HeaderFormatConstant)

        print(
            f"{"The perimeter of the Square is":<{Global.TextFormatConstant}}: {perimeter}"
        )
        print(f"{"The Area of the Square is":<{Global.TextFormatConstant}}: {area}")

    def CalculatePerimeter(self, side):
        return side * 4

    def CalculateArea(self, side):
        return side**2
