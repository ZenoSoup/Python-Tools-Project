from Calculator.Calculator import Calculator
from Converter.Converter import Converter
from Global import Global


def main():
    while True:
        print("Tools".center(Global.HeaderFormatConstant, "="))
        print("1. Calculator")
        print("2. Conversion")
        print("0. Exit")
        print("=" * Global.HeaderFormatConstant)
        choice = input(f"{"Choice":{Global.TextFormatConstant}}: ")

        if choice == "1":
            calc = Calculator()
            calc.Start()
        elif choice == "2":
            conv = Converter()
            conv.Start()
        elif choice == "0":
            return
        else:
            print("Choice Invalid")


if __name__ == "__main__":
    main()
