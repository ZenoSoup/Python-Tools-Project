from Global import Global
from Helper import Helper


class Square:
    def Start(self):
        while True:
            print("Square".center(Global.HeaderFormatConstant, "="))
            side = Helper.inputFloat(
                f"{"Enter the side of the Square":<{Global.TextFormatConstant}}: ",
                min_val=0.000001,
            )

            perimeter = self.CalculatePerimeter(side)
            area = self.CalculateArea(side)

            print("=" * Global.HeaderFormatConstant)

            print(
                f"{"The perimeter of the Square is":<{Global.TextFormatConstant}}: {perimeter}"
            )
            print(f"{"The Area of the Square is":<{Global.TextFormatConstant}}: {area}")

            if not Helper.inputConfirmation(
                f"{"Calculate again? (Y/N)":<{Global.TextFormatConstant}}: "
            ):
                return

    def CalculatePerimeter(self, side):
        return side * 4

    def CalculateArea(self, side):
        return side**2
