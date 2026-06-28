from Helper import Helper


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
            print("Weight".center(25, "="))
            print("1. Kilogram")
            print("2. Gram")
            print("3. Miligram")
            print("4. Ounce")
            print("5. Metric Ton")
            print("0. Exit")
            currentNum = input("Origin Unit  : ")
            convertNum = input("Convert Unit : ")

            if currentNum not in self.weightKey or convertNum not in self.weightKey:
                print("Invalid Unit Input")
                continue

            elif convertNum == "0":
                return

            weight = Helper.inputFloat("Enter The Weight: ")

            currentUnit = self.weightKey[currentNum]
            convertUnit = self.weightKey[convertNum]

            kilogramValue = self.weightToKilogram[currentUnit](weight)
            convertedValue = self.weightFromKilogram[convertUnit](kilogramValue)

            print()
            print(f"Original Weight  : {weight:,} {currentUnit}")
            print(f"Converted Weight : {convertedValue:,} {convertUnit}")
            print()
