from Global import Global
from Helper import Helper
from string import punctuation, digits, ascii_lowercase, ascii_uppercase


class PasswordSafety:
    def Start(self):
        while True:
            print("Password Safety Checker".center(Global.HeaderFormatConstant, "="))
            password = input(
                f"{"Please insert your password":<{Global.TextFormatConstant}}: "
            )

            length = len(password)
            contains_lower = any(c in ascii_lowercase for c in password)
            contains_upper = any(c in ascii_uppercase for c in password)
            contains_number = any(c in digits for c in password)
            contains_symbol = any(c in punctuation for c in password)

            points = 0
            if length >= 8:
                points += 1
            if length >= 12:
                points += 1
            if contains_lower:
                points += 1
            if contains_upper:
                points += 1
            if contains_number:
                points += 1
            if contains_symbol:
                points += 1

            print("=" * Global.HeaderFormatConstant)
            print(f"{"Password Length":<{Global.TextFormatConstant}}: {length}")
            print(f"{"Contains Lowercase":<{Global.TextFormatConstant}}: {contains_lower}")
            print(f"{"Contains Uppercase":<{Global.TextFormatConstant}}: {contains_upper}")
            print(f"{"Contains Number":<{Global.TextFormatConstant}}: {contains_number}")
            print(f"{"Contains Symbol":<{Global.TextFormatConstant}}: {contains_symbol}")
            print("-" * Global.HeaderFormatConstant)

            if points >= 6:
                strength = "Very Strong"
            elif points >= 4:
                strength = "Strong"
            elif points >= 3:
                strength = "Moderate"
            else:
                strength = "Weak - change it now!"

            print(f"{"Password Strength":<{Global.TextFormatConstant}}: {strength} ({points}/6)")

            if not Helper.inputConfirmation(
                f"{"Check another password? (Y/N)":<{Global.TextFormatConstant}}: "
            ):
                return
