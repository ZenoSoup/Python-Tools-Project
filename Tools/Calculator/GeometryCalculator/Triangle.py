from Global import Global
from Helper import Helper


class Triangle:
    def Start(self):
        while True:
            print("Triangle".center(Global.HeaderFormatConstant, "="))
            height = Helper.inputFloat(
                f"{"Enter the Height of the Triangle":<{Global.TextFormatConstant}}: ",
                min_val=0.000001,
            )
            base = Helper.inputFloat(
                f"{"Enter the Base (Bottom Side) Length":<{Global.TextFormatConstant}}: ",
                min_val=0.000001,
            )
            side_left = Helper.inputFloat(
                f"{"Enter the Left Side Length of the Triangle":<{Global.TextFormatConstant}}: ",
                min_val=0.000001,
            )
            side_right = Helper.inputFloat(
                f"{"Enter the Right Side Length of the Triangle":<{Global.TextFormatConstant}}: ",
                min_val=0.000001,
            )

            perimeter = self.CalculatePerimeter(base, side_left, side_right)
            area = self.CalculateArea(height, base)

            print("=" * Global.HeaderFormatConstant)

            print(
                f"{"The perimeter of the Triangle is":<{Global.TextFormatConstant}}: {perimeter}"
            )
            print(f"{"The Area of the Triangle is":<{Global.TextFormatConstant}}: {area}")

            if not Helper.inputConfirmation(
                f"{"Calculate again? (Y/N)":<{Global.TextFormatConstant}}: "
            ):
                return

    def CalculatePerimeter(self, side1, side2, side3):
        return side1 + side2 + side3

    def CalculateArea(self, height, base):
        return (height * base) * 0.5
