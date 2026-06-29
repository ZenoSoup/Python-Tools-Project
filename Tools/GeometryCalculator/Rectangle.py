from Global import Global
from Helper import Helper


class Rectangle:
    def Start(self):
        print("Square".center(Global.HeaderFormatConstant, "="))
        length = Helper.inputFloat(
            f"{"Enter the length of the Rectangle":<{Global.TextFormatConstant}}: "
        )
        height = Helper.inputFloat(
            f"{"Enter the height of the Rectangle":<{Global.TextFormatConstant}}: "
        )

        perimeter = self.CalculatePerimeter(length, height)
        area = self.CalculateArea(length, height)

        print("=" * Global.HeaderFormatConstant)

        print(
            f"{"The perimeter of the Rectangle is":<{Global.TextFormatConstant}}: {perimeter}"
        )
        print(f"{"The Area of the Rectangle is":<{Global.TextFormatConstant}}: {area}")

    def CalculatePerimeter(self, length, height):
        return 2 * (length + height)

    def CalculateArea(self, length, height):
        return length * height
