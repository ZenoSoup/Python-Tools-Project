from Global import Global
from string import punctuation, digits

class PasswordSafety:
    def Start(self):
        print("Password Safety Checker".center(Global.HeaderFormatConstant, "="))
        password = input(f"{"Please insert your password":<{Global.TextFormatConstant}}: ")
        
        isLong = False
        containsNumber = False
        containsSymbol = False
        
        for char in password:
            if char in punctuation:
                containsSymbol = True
            
            if char in digits:
                containsNumber = True

        points = 1

        if containsNumber:
            points += 1

        if containsSymbol:
            points += 1

        length = len(password)

        if length >= 8:
            isLong = True

        if isLong:
            points += 1
        
        print("=" * Global.HeaderFormatConstant)

        print(f"{"Password Length":<{Global.TextFormatConstant}}: {length}")
        print(f"{"Contains Number":<{Global.TextFormatConstant}}: {containsNumber}")
        print(f"{"Contains Symbol":<{Global.TextFormatConstant}}: {containsSymbol}")
        print("-" * Global.HeaderFormatConstant)

        if points == 4:
            print("Your password is very strong")
        
        elif points >= 2:
            print("Your password is moderately decent")

        elif points == 1:
            print("Your password is weak, change it now!!")

        