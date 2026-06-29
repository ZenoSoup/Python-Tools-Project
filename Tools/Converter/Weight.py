from .Helper import Helper
from Global import Global


class Weight:
    def __init__(self):
        self.weightKey = {
            "1": "Kilogram",
            "2": "Gram",
            "3": "Miligram",
            "4": "Ounce",
            "5": "Metric Ton",
        }

        self.weightToKilogram = {
            "Kilogram": lambda x: x * 1,
            "Gram": lambda x: x / 1000,
            "Miligram": lambda x: x / 1e-6,
            "Ounce": lambda x: x / 35274,
            "Metric Ton": lambda x: x * 1000,
        }

        self.weightFromKilogram = {
            "Kilogram": lambda x: x / 1,
            "Gram": lambda x: x * 1000,
            "Miligram": lambda x: x * 1e6,
            "Ounce": lambda x: x * 35274,
            "Metric Ton": lambda x: x / 1000,
        }

    def Start(self):
        while True:
            print("Weight".center(Global.HeaderFormatConstant, "="))
            print("1. Kilogram")
            print("2. Gram")
            print("3. Miligram")
            print("4. Ounce")
            print("5. Metric Ton")
            print("0. Exit")
            print("=" * Global.HeaderFormatConstant)
            originNum = input(f"{"Origin Unit":<{Global.TextFormatConstant}}: ")
            convertNum = input(f"{'Convert Unit':<{Global.TextFormatConstant}}: ")

            if originNum == "0" or convertNum == "0":
                return

            elif originNum not in self.weightKey or convertNum not in self.weightKey:
                print("Invalid Unit Input")
                continue

            weight = Helper.inputFloat(
                f"{"Enter The Weight":<{Global.TextFormatConstant}}: "
            )

            currentUnit = self.weightKey[originNum]
            convertUnit = self.weightKey[convertNum]

            kilogramValue = self.weightToKilogram[currentUnit](weight)
            convertedValue = self.weightFromKilogram[convertUnit](kilogramValue)

            print()
            print(
                f"{"Original Weight":<{Global.TextFormatConstant}}: {weight:,} {currentUnit}"
            )
            print(
                f"{"Converted Weight":<{Global.TextFormatConstant}}: {convertedValue:,} {convertUnit}"
            )
            print()
