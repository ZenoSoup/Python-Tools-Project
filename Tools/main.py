from Calculator.Calculator import Calculator
from UnitConverter.UnitConverter import Converter
from Security.Security import Security
from Global import Global


def main():
    while True:
        print("Tools".center(Global.HeaderFormatConstant, "="))
        print("1. Calculator")
        print("2. Unit Converter")
        print("3. Security")
        print("0. Exit")
        print("=" * Global.HeaderFormatConstant)
        choice = input(f"{"Choice":{Global.TextFormatConstant}}: ")

        if choice == "1":
            calc = Calculator()
            calc.Start()
        elif choice == "2":
            conv = Converter()
            conv.Start()
        elif choice == "3":
            sec = Security()
            sec.Start()
        elif choice == "0":
            return
        else:
            print("Choice Invalid")


if __name__ == "__main__":
    main()
