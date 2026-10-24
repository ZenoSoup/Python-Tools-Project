from Global import Global
from Helper import Helper


class Rectangle:
    def Start(self):
        while True:
            print("Rectangle".center(Global.HeaderFormatConstant, "="))
            length = Helper.inputFloat(
                f"{"Enter the length of the Rectangle":<{Global.TextFormatConstant}}: ",
                min_val=0.000001,
            )
            height = Helper.inputFloat(
                f"{"Enter the height of the Rectangle":<{Global.TextFormatConstant}}: ",
                min_val=0.000001,
            )

            perimeter = self.CalculatePerimeter(length, height)
            area = self.CalculateArea(length, height)

            print("=" * Global.HeaderFormatConstant)

            print(
                f"{"The perimeter of the Rectangle is":<{Global.TextFormatConstant}}: {perimeter}"
            )
            print(f"{"The Area of the Rectangle is":<{Global.TextFormatConstant}}: {area}")

            if not Helper.inputConfirmation(
                f"{"Calculate again? (Y/N)":<{Global.TextFormatConstant}}: "
            ):
                return

    def CalculatePerimeter(self, length, height):
        return 2 * (length + height)

    def CalculateArea(self, length, height):
        return length * height
