from Global import Global
from Helper import Helper
from string import ascii_uppercase, ascii_lowercase, punctuation, digits
import secrets


class PasswordGenerator:
    def Start(self):
        while True:
            print("Password Generator".center(Global.HeaderFormatConstant, "="))
            passwordLength = Helper.inputInt(
                f"{"Total Password Length (minimum 8)":<{Global.TextFormatConstant}}: ",
                min_val=8,
            )

            useDigits = Helper.inputConfirmation(
                f"{"Include Numbers? (Y/N)":<{Global.TextFormatConstant}}: "
            )
            useSymbol = Helper.inputConfirmation(
                f"{"Include Symbols? (Y/N)":<{Global.TextFormatConstant}}: "
            )

            characters = ascii_uppercase + ascii_lowercase
            password = [
                secrets.choice(ascii_uppercase),
                secrets.choice(ascii_lowercase),
            ]

            if useDigits:
                characters += digits
                password.append(secrets.choice(digits))

            if useSymbol:
                characters += punctuation
                password.append(secrets.choice(punctuation))

            remaining_length = passwordLength - len(password)
            for _ in range(remaining_length):
                password.append(secrets.choice(characters))

            secrets.SystemRandom().shuffle(password)
            finalPassword = "".join(password)

            print("=" * Global.HeaderFormatConstant)
            print(f"{"Final Password":<{Global.TextFormatConstant}}: {finalPassword}")

            if not Helper.inputConfirmation(
                f"{"Generate another password? (Y/N)":<{Global.TextFormatConstant}}: "
            ):
                return
