from Calculator.Calculator import Calculator
from UnitConverter.UnitConverter import Converter
from Security.Security import Security
from StringTools.StringTools import StringTools
from Global import Global

choices = {
    "1": "Calculator",
    "2": "Unit Converter",
    "3": "Security",
    "4": "String Tools"
}

executeChoice = {
    "Calculator": lambda: Calculator().Start(),
    "Unit Converter": lambda: Converter().Start(),
    "Security": lambda: Security().Start(),
    "String Tools": lambda: Security.Start()
}

def main():
    while True:
        print("Tools".center(Global.HeaderFormatConstant, "="))
        
        for key, value in choices.items():
            print(f"{key}. {value}")

        print("0. Exit")
        print("=" * Global.HeaderFormatConstant)
        choiceNum = input(f"{"Choice":{Global.TextFormatConstant}}: ")

        if choiceNum == "0":
            return
        
        if choiceNum not in choices:
            print("Invalid Choice")
            continue
        
        choice = choices[choiceNum]
        executeChoice[choice]

if __name__ == "__main__":
    main()
