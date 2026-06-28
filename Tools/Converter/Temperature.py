from .Helper import Helper


class Temperature:
    def __init__(self):
        self.tempKey = {"1": "Celcius", "2": "Fahrenheit", "3": "Kelvin"}

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
            print("Temperature".center(25, "="))
            print("1. Celcius")
            print("2. Fahrenheit")
            print("3. Kelvin")
            originNum = input("Enter The Origin Unit: ")
            convertNum = input("Enter The Convert Unit: ")

            if originNum == "0" or convertNum == "0":
                return

            if originNum not in self.tempKey or convertNum not in self.tempKey:
                print("Input Invalid")
                continue

            value = Helper.inputFloat("Input The Current Temperature: ")

            originUnit = self.tempKey[originNum]
            convertUnit = self.tempKey[convertNum]

            celciusValue = self.tempToCelcius[originUnit](value)
            resultValue = self.tempFromCelcius[convertUnit](celciusValue)

            print(f"Origin Temperature    : {value} {originUnit}")
            print(f"Converted Temperature : {resultValue} {convertUnit}")
