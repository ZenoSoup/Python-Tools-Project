from Global import Global
from .WordCounter import WordCounter
from .TextCaseConverter import TextCaseConverter

class StringTools:
    def __init__(self):
        self.choices = {
            "1": "Word Counter",
            "2": "Text Case Converter"
        }

        self.startChoice = {
            "Word Counter": lambda: WordCounter().Start(),
            "Text Case Converter": lambda: TextCaseConverter().Start()
        }
    
    def Start(self):
        while True:
            print("String Tools".center(Global.HeaderFormatConstant, "="))

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

            choice = self.choices[choiceNum]
            self.startChoice[choice]()