from .Helper import Helper
from Global import Global


class Length:
    def __init__(self):
        self.lengthKey = {
            "1": "Meter",
            "2": "Kilometer",
            "3": "Centimeter",
            "4": "Milimeter",
        }

        self.lengthToMeter = {
            "Meter": lambda x: x * 1,
            "Kilometer": lambda x: x * 1000,
            "Centimeter": lambda x: x / 100,
            "Milimeter": lambda x: x / 1000,
        }

        self.lengthFromMeter = {
            "Meter": lambda x: x / 1,
            "Kilometer": lambda x: x / 1000,
            "Centimeter": lambda x: x * 100,
            "Milimeter": lambda x: x * 1000,
        }

    def Start(self):
        while True:
            print("Length".center(Global.HeaderFormatConstant, "="))
            print("1. Meter")
            print("2. Kilometer")
            print("3. Centimeter")
            print("4. Milimeter")
            print("0. Exit")
            print("=" * Global.HeaderFormatConstant)
            originNum = input(f"{"Origin Unit":<{Global.TextFormatConstant}}: ")
            convertNum = input(f"{"Convert Unit":<{Global.TextFormatConstant}}: ")

            if originNum == "0" or convertNum == "0":
                return

            if originNum not in self.lengthKey or convertNum not in self.lengthKey:
                print("Input Invalid")
                continue

            value = Helper.inputFloat(
                f"{"Input The Origin Length":<{Global.TextFormatConstant}}: "
            )

            originUnit = self.lengthKey[originNum]
            convertUnit = self.lengthKey[convertNum]

            meterValue = self.lengthToMeter[originUnit](value)
            convertValue = self.lengthFromMeter[convertUnit](meterValue)

            print(
                f"{"Origin Length":<{Global.TextFormatConstant}}: {value} {originUnit}"
            )
            print(
                f"{"Convert Length":<{Global.TextFormatConstant}}: {convertValue} {convertUnit}"
            )
