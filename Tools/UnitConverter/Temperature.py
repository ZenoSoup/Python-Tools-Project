from Helper import Helper
from Global import Global


class Temperature:
    def __init__(self):
        self.tempKey = {
            "1": "Celcius", 
            "2": "Fahrenheit", 
            "3": "Kelvin"
        }

        self.tempToCelcius = {
            "Celcius": lambda x: x * 1,
            "Fahrenheit": lambda x: (x - 32) * 5 / 9,
            "Kelvin": lambda x: x - 273.15,
        }

        self.tempFromCelcius = {
            "Celcius": lambda x: x / 1,
            "Fahrenheit": lambda x: (x * 9 / 5) + 32,
            "Kelvin": lambda x: x + 273.15,
        }

    def Start(self):
        while True:
            print("Temperature".center(Global.HeaderFormatConstant, "="))

            for key, value in self.tempKey.items():
                print(f"{key}. {value}")

            print("0. Exit")
            print("=" * Global.HeaderFormatConstant)
            originNum = input(
                f"{"Enter The Origin Unit":<{Global.TextFormatConstant}}: "
            )

            if originNum == "0":
                return
            
            if originNum not in self.tempKey:
                print("Invalid Input")
                continue

            convertNum = input(
                f"{"Enter The Convert Unit":<{Global.TextFormatConstant}}: "
            )

            if convertNum == "0":
                return

            if convertNum not in self.tempKey:
                print("Input Invalid")
                continue

            value = Helper.inputFloat(
                f"{"Input The Current Temperature":<{Global.TextFormatConstant}}: "
            )

            originUnit = self.tempKey[originNum]
            convertUnit = self.tempKey[convertNum]

            celciusValue = self.tempToCelcius[originUnit](value)
            resultValue = self.tempFromCelcius[convertUnit](celciusValue)

            print(
                f"{"Origin Temperature":<{Global.TextFormatConstant}}: {value} {originUnit}"
            )
            print(
                f"{"Converted Temperature":<{Global.TextFormatConstant}}: {resultValue} {convertUnit}"
            )
