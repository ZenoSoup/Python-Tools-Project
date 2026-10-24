import re
from Global import Global


class TextCaseConverter:
    def __init__(self):
        self.choices = {
            "1": "All Uppercase",
            "2": "All Lowercase",
            "3": "Capitalize First Word",
            "4": "Capitalize Every Word",
            "5": "Sentence Case",
        }

        self.getResult = {
            "All Uppercase": self.Uppercase,
            "All Lowercase": self.Lowercase,
            "Capitalize First Word": self.capitalizeFirst,
            "Capitalize Every Word": self.capitalizeAll,
            "Sentence Case": self.sentenceCase,
        }

    def Start(self):
        while True:
            print("Text Case Converter".center(Global.HeaderFormatConstant, "="))

            for key, value in self.choices.items():
                print(f"{key}. {value}")

            print("0. Exit")
            print("=" * Global.HeaderFormatConstant)

            choiceNum = input(f"{"Choice":<{Global.TextFormatConstant}}: ")

            if choiceNum == "0":
                return

            if choiceNum not in self.choices:
                print("Choice Invalid")
                continue

            text = input(f"{"Enter the text":<{Global.TextFormatConstant}}: ")

            choice = self.choices[choiceNum]
            result = self.getResult[choice](text)

            print(f"{"Result":<{Global.TextFormatConstant}}: {result}")

    def Uppercase(self, text: str):
        return text.upper()

    def Lowercase(self, text: str):
        return text.lower()

    def capitalizeFirst(self, text: str):
        return text.capitalize()

    def capitalizeAll(self, text: str):
        return text.title()

    def sentenceCase(self, text: str):
        return re.sub(
            r"(?:^|[.!?]\s+)([a-z])", lambda m: m.group(0).upper(), text
        )
