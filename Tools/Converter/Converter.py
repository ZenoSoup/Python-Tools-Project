from .Weight import Weight
from .Temperature import Temperature
from .Length import Length
from Global import Global


class Converter:
    def Start(self):
        while True:
            print("Converter".center(Global.HeaderFormatConstant, "="))
            print("1. Weight")
            print("2. Temperature")
            print("3. Length")
            print("0. Exit")
            print("=" * Global.HeaderFormatConstant)
            choice = input(f"{"Choice":<{Global.TextFormatConstant}}: ")
            if choice == "0":
                return

            elif choice == "1":
                weight = Weight()
                weight.Start()

            elif choice == "2":
                temp = Temperature()
                temp.Start()

            elif choice == "3":
                length = Length()
                length.Start()

            else:
                print("Choice Invalid")
