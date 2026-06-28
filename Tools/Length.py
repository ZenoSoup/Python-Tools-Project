from Helper import Helper


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
            print("Length".center(25, "="))
            print("1. Meter")
            print("2. Kilometer")
            print("3. Centimeter")
            print("4. Milimeter")
            originNum = input("Origin Unit: ")
            convertNum = input("Convert Unit: ")

            if originNum not in self.lengthKey or convertNum not in self.lengthKey:
                print("Input Invalid")
                continue

            if originNum == "0" or convertNum == "0":
                return

            value = Helper.inputFloat("Input The Origin Length: ")

            originUnit = self.lengthKey[originNum]
            convertUnit = self.lengthKey[convertNum]

            meterValue = self.lengthToMeter[originUnit](value)
            convertValue = self.lengthFromMeter[convertUnit](meterValue)

            print(f"Origin Length  : {value} {originUnit}")
            print(f"Convert Length : {convertValue} {convertUnit}")
