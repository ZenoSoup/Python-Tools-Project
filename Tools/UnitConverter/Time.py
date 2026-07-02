from Global import Global
from Helper import Helper

class Time:
    def __init__(self):
        self.timeKeys = {
            "1": "Seconds",
            "2": "Minutes",
            "3": "Hours",
            "4": "Days",
            "5": "Weeks",
            "6": "Months"
        }

        self.timeToSeconds = {
            "Seconds": lambda x: x * 1,
            "Minutes": lambda x: x * 60,
            "Hours": lambda x: x * (60 * 60),
            "Days": lambda x: x * (24 * 60 * 60),
            "Weeks": lambda x: x * (7 * 24 * 60 * 60),
            "Months": lambda x: x * (30 * 24 * 60 * 60)
        }

        self.timeFromSeconds = {
            "Seconds": lambda x: x / 1,
            "Minutes": lambda x: x / 60,
            "Hours": lambda x: x / (60 * 60),
            "Days": lambda x: x / (24 * 60 * 60),
            "Weeks": lambda x: x / (7 * 24 * 60 * 60),
            "Months": lambda x: x / (30 * 24 * 60 * 60)
        }
    def Start(self):
        while True:
            print("Time Converter".center(Global.HeaderFormatConstant, "="))
            
            for key, value in self.timeKeys.items():
                print(f"{key}. {value}")

            print("0. Exit")

            originNum = input(f"{"Origin Unit":<{Global.TextFormatConstant}}: ")

            if originNum == "0":
                return
            
            if originNum not in self.timeKeys:
                print("Choice Invalid")
                continue

            convertNum = input(f"{"Convert Unit":<{Global.TextFormatConstant}}: ")

            if convertNum == "0":
                return
            
            if convertNum not in self.timeKeys:
                print("Choice Invalid")
                continue

            print("=" * Global.HeaderFormatConstant)

            timeValue = Helper.inputFloat(f"{"Enter the origin time value":<{Global.TextFormatConstant}}: ")

            originUnit = self.timeKeys[originNum]
            convertUnit = self.timeKeys[convertNum]

            inSeconds = self.timeToSeconds[originUnit](timeValue)
            
            result = self.timeFromSeconds[convertUnit](inSeconds)

            print(f"{"Origin Time":<{Global.TextFormatConstant}}: {timeValue} {originUnit}")
            print(f"{"Converted Time":<{Global.TextFormatConstant}}: {result} {convertUnit}")