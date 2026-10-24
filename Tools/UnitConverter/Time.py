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
            "6": "Months (30 days)",
            "7": "Years (365 days)",
        }

        self.timeToSeconds = {
            "Seconds": lambda x: x * 1.0,
            "Minutes": lambda x: x * 60.0,
            "Hours": lambda x: x * 3600.0,
            "Days": lambda x: x * 86400.0,
            "Weeks": lambda x: x * 604800.0,
            "Months (30 days)": lambda x: x * 2592000.0,
            "Years (365 days)": lambda x: x * 31536000.0,
        }

        self.timeFromSeconds = {
            "Seconds": lambda x: x / 1.0,
            "Minutes": lambda x: x / 60.0,
            "Hours": lambda x: x / 3600.0,
            "Days": lambda x: x / 86400.0,
            "Weeks": lambda x: x / 604800.0,
            "Months (30 days)": lambda x: x / 2592000.0,
            "Years (365 days)": lambda x: x / 31536000.0,
        }

    def Start(self):
        while True:
            print("Time Converter".center(Global.HeaderFormatConstant, "="))

            for key, value in self.timeKeys.items():
                print(f"{key}. {value}")

            print("0. Exit")
            print("=" * Global.HeaderFormatConstant)

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

            timeValue = Helper.inputFloat(
                f"{"Enter the origin time value":<{Global.TextFormatConstant}}: ",
                min_val=0.0,
            )

            originUnit = self.timeKeys[originNum]
            convertUnit = self.timeKeys[convertNum]

            inSeconds = self.timeToSeconds[originUnit](timeValue)
            result = self.timeFromSeconds[convertUnit](inSeconds)

            print("=" * Global.HeaderFormatConstant)
            print(
                f"{"Origin Time":<{Global.TextFormatConstant}}: {timeValue:g} {originUnit}"
            )
            print(
                f"{"Converted Time":<{Global.TextFormatConstant}}: {result:g} {convertUnit}"
            )

            if not Helper.inputConfirmation(
                f"{"Convert another time? (Y/N)":<{Global.TextFormatConstant}}: "
            ):
                return
