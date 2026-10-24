from Helper import Helper
from Global import Global


class Length:
    def __init__(self):
        self.lengthKey = {
            "1": "Meter",
            "2": "Kilometer",
            "3": "Centimeter",
            "4": "Millimeter",
            "5": "Mile",
            "6": "Foot",
            "7": "Inch",
        }

        self.lengthToMeter = {
            "Meter": lambda x: x * 1.0,
            "Kilometer": lambda x: x * 1000.0,
            "Centimeter": lambda x: x / 100.0,
            "Millimeter": lambda x: x / 1000.0,
            "Mile": lambda x: x * 1609.344,
            "Foot": lambda x: x * 0.3048,
            "Inch": lambda x: x * 0.0254,
        }

        self.lengthFromMeter = {
            "Meter": lambda x: x / 1.0,
            "Kilometer": lambda x: x / 1000.0,
            "Centimeter": lambda x: x * 100.0,
            "Millimeter": lambda x: x * 1000.0,
            "Mile": lambda x: x / 1609.344,
            "Foot": lambda x: x / 0.3048,
            "Inch": lambda x: x / 0.0254,
        }

    def Start(self):
        while True:
            print("Length Converter".center(Global.HeaderFormatConstant, "="))

            for key, value in self.lengthKey.items():
                print(f"{key}. {value}")

            print("0. Exit")
            print("=" * Global.HeaderFormatConstant)
            originNum = input(f"{"Origin Unit":<{Global.TextFormatConstant}}: ")

            if originNum == "0":
                return

            if originNum not in self.lengthKey:
                print("Input Invalid")
                continue

            convertNum = input(f"{"Convert Unit":<{Global.TextFormatConstant}}: ")

            if convertNum == "0":
                return

            if convertNum not in self.lengthKey:
                print("Input Invalid")
                continue

            value = Helper.inputFloat(
                f"{"Input The Origin Length":<{Global.TextFormatConstant}}: ",
                min_val=0.0,
            )

            originUnit = self.lengthKey[originNum]
            convertUnit = self.lengthKey[convertNum]

            meterValue = self.lengthToMeter[originUnit](value)
            convertValue = self.lengthFromMeter[convertUnit](meterValue)

            print("=" * Global.HeaderFormatConstant)
            print(
                f"{"Origin Length":<{Global.TextFormatConstant}}: {value} {originUnit}"
            )
            print(
                f"{"Converted Length":<{Global.TextFormatConstant}}: {convertValue:g} {convertUnit}"
            )

            if not Helper.inputConfirmation(
                f"{"Convert another length? (Y/N)":<{Global.TextFormatConstant}}: "
            ):
                return
