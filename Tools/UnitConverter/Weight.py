from Helper import Helper
from Global import Global


class Weight:
    def __init__(self):
        self.weightKey = {
            "1": "Kilogram",
            "2": "Gram",
            "3": "Milligram",
            "4": "Ounce",
            "5": "Pound",
            "6": "Metric Ton",
        }

        self.weightToKilogram = {
            "Kilogram": lambda x: x * 1.0,
            "Gram": lambda x: x / 1000.0,
            "Milligram": lambda x: x / 1_000_000.0,
            "Ounce": lambda x: x * 0.028349523125,
            "Pound": lambda x: x * 0.45359237,
            "Metric Ton": lambda x: x * 1000.0,
        }

        self.weightFromKilogram = {
            "Kilogram": lambda x: x / 1.0,
            "Gram": lambda x: x * 1000.0,
            "Milligram": lambda x: x * 1_000_000.0,
            "Ounce": lambda x: x / 0.028349523125,
            "Pound": lambda x: x / 0.45359237,
            "Metric Ton": lambda x: x / 1000.0,
        }

    def Start(self):
        while True:
            print("Weight Converter".center(Global.HeaderFormatConstant, "="))

            for key, value in self.weightKey.items():
                print(f"{key}. {value}")

            print("0. Exit")
            print("=" * Global.HeaderFormatConstant)
            originNum = input(f"{"Origin Unit":<{Global.TextFormatConstant}}: ")

            if originNum == "0":
                return

            if originNum not in self.weightKey:
                print("Input Invalid")
                continue

            convertNum = input(f"{"Convert Unit":<{Global.TextFormatConstant}}: ")

            if convertNum == "0":
                return

            if convertNum not in self.weightKey:
                print("Invalid Unit Input")
                continue

            weight = Helper.inputFloat(
                f"{"Enter The Weight":<{Global.TextFormatConstant}}: ",
                min_val=0.0,
            )

            currentUnit = self.weightKey[originNum]
            convertUnit = self.weightKey[convertNum]

            kilogramValue = self.weightToKilogram[currentUnit](weight)
            convertedValue = self.weightFromKilogram[convertUnit](kilogramValue)

            print("=" * Global.HeaderFormatConstant)
            print(
                f"{"Original Weight":<{Global.TextFormatConstant}}: {weight:g} {currentUnit}"
            )
            print(
                f"{"Converted Weight":<{Global.TextFormatConstant}}: {convertedValue:g} {convertUnit}"
            )

            if not Helper.inputConfirmation(
                f"{"Convert another weight? (Y/N)":<{Global.TextFormatConstant}}: "
            ):
                return
