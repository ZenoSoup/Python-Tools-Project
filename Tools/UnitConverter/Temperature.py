from Helper import Helper
from Global import Global


class Temperature:
    def __init__(self):
        self.tempKey = {
            "1": "Celsius",
            "2": "Fahrenheit",
            "3": "Kelvin",
        }

        self.tempToCelsius = {
            "Celsius": lambda x: x * 1.0,
            "Fahrenheit": lambda x: (x - 32.0) * 5.0 / 9.0,
            "Kelvin": lambda x: x - 273.15,
        }

        self.tempFromCelsius = {
            "Celsius": lambda x: x / 1.0,
            "Fahrenheit": lambda x: (x * 9.0 / 5.0) + 32.0,
            "Kelvin": lambda x: x + 273.15,
        }

    def Start(self):
        while True:
            print("Temperature Converter".center(Global.HeaderFormatConstant, "="))

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

            celsiusValue = self.tempToCelsius[originUnit](value)
            if celsiusValue < -273.15:
                print("Warning: Temperature is below absolute zero (-273.15 C / 0 K).")

            resultValue = self.tempFromCelsius[convertUnit](celsiusValue)

            print("=" * Global.HeaderFormatConstant)
            print(
                f"{"Origin Temperature":<{Global.TextFormatConstant}}: {value} {originUnit}"
            )
            print(
                f"{"Converted Temperature":<{Global.TextFormatConstant}}: {resultValue:.2f} {convertUnit}"
            )

            if not Helper.inputConfirmation(
                f"{"Convert another temperature? (Y/N)":<{Global.TextFormatConstant}}: "
            ):
                return
