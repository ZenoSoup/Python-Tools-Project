from Global import Global
from Helper import Helper
from string import ascii_uppercase, ascii_lowercase, punctuation, digits
import random, secrets

class PasswordGenerator:
    def Start(self):
        while True:
            print("Password Generator".center(Global.HeaderFormatConstant, "="))
            passwordLength = Helper.inputInt(f"{"Total Password Length (minimum 8)":<{Global.TextFormatConstant}}: ")

            if passwordLength < 8:
                print("Password length must not be below 8")
                continue

            useDigits = Helper.inputConfirmation(f"{"Include Numbers? (Y/N)":<{Global.TextFormatConstant}}: ")
            useSymbol = Helper.inputConfirmation(f"{"Include Symbols? (Y/N)":<{Global.TextFormatConstant}}: ")

            characters = ascii_uppercase + ascii_lowercase

            password = [
                secrets.choice(ascii_uppercase),
                secrets.choice(ascii_lowercase)
            ]

            if useDigits:
                characters += digits
                password.append(secrets.choice(digits))
            
            else:
                passwordLength += 1

            if useSymbol:
                characters += punctuation
                password.append(secrets.choice(punctuation))

            else:
                passwordLength += 1

            for _ in range(passwordLength - 4):
                password.append(secrets.choice(characters))
            
            random.shuffle(password)
            finalPassword = "".join(password)

            print(f"{"Final Password":<{Global.TextFormatConstant}}: {finalPassword}", end="")
            input()

            return

            

        