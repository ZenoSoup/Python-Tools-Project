from Global import Global
from Helper import Helper


class Triangle:
    def Start(self):
        print("Triangle".center(Global.HeaderFormatConstant, "="))
        height = Helper.inputFloat(
            f"{"Enter the Height of the Triangle":<{Global.TextFormatConstant}}: "
        )
        base = Helper.inputFloat(
            f"{"Enter the Base of the Triangle":<{Global.TextFormatConstant}}: "
        )
        side1 = Helper.inputFloat(
            f"{"Enter the Bottom Side Length of the Triangle":<{Global.TextFormatConstant}}: "
        )
        side2 = Helper.inputFloat(
            f"{"Enter the Left Side Length of the Triangle":<{Global.TextFormatConstant}}: "
        )
        side3 = Helper.inputFloat(
            f"{"Enter the Right Side Length of the Triangle":<{Global.TextFormatConstant}}: "
        )

        perimeter = self.CalculatePerimeter(side1, side2, side3)
        area = self.CalculateArea(height, base)

        print("=" * Global.HeaderFormatConstant)

        print(
            f"{"The perimeter of the Triangle is":<{Global.TextFormatConstant}}: {perimeter}"
        )
        print(f"{"The Area of the Triangle is":<{Global.TextFormatConstant}}: {area}")

    def CalculatePerimeter(self, side1, side2, side3):
        return side1 + side2 + side3

    def CalculateArea(self, height, base):
        return (height * base) * 1 / 2
