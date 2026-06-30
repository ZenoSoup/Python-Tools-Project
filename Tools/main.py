from Calculator.Calculator import Calculator
from Converter.Converter import Converter
from GeometryCalculator.GeometryCalculator import GeometryCalculator
from Security.Security import Security
from Global import Global


def main():
    while True:
        print("Tools".center(Global.HeaderFormatConstant, "="))
        print("1. Calculator")
        print("2. Geometry Calculator")
        print("3. Conversion")
        print("4. Security")
        print("0. Exit")
        print("=" * Global.HeaderFormatConstant)
        choice = input(f"{"Choice":{Global.TextFormatConstant}}: ")

        if choice == "1":
            calc = Calculator()
            calc.Start()
        elif choice == "2":
            geoCalc = GeometryCalculator()
            geoCalc.start()
        elif choice == "3":
            conv = Converter()
            conv.Start()
        elif choice == "4":
            sec = Security()
            sec.Start()
        elif choice == "0":
            return
        else:
            print("Choice Invalid")


if __name__ == "__main__":
    main()
