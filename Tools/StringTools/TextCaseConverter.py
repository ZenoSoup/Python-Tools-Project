from Global import Global

class TextCaseConverter:
    def __init__(self):
        self.choices = {
            "1": "All Uppercase",
            "2": "All Lowercase",
            "3": "Capitalize First Word",
            "4": "Capitalize Every Word",
            "5": "Capitalization"
        }

        self.getResult = {
            "All Uppercase": lambda x: self.Uppercase(x),
            "All Lowercase": lambda x: self.Lowercase(x),
            "Capitalize First Word": lambda x: self.capitalizeFirst(x),
            "Capitalize Every Word": lambda x: self.capitalizeAll(x),
            "Capitalization": lambda x: self.capitalization(x)
        }

    def Start(self):
        while True:
            print("Text Case Converter".center(Global.HeaderFormatConstant, "="))

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
            
            text = input(f"{"Enter the text":<{Global.TextFormatConstant}}: ")

            choice = self.choices[choiceNum]
            result = self.getResult[choice](text)

            print(f"{"Result":<{Global.TextFormatConstant}}: {result}")

    def Uppercase(self, text: str):
        return text.upper()
    
    def Lowercase(self, text: str):
        return text.lower()
    
    def capitalizeFirst(self, text: str):
        return text.capitalize()
    
    def capitalizeAll(self, text: str):
        return text.title()
    
    def capitalization(self, text: str):
        splitted = text.split('. ')
        finalTextList = []

        for sentence in splitted:
            finalTextList.append(sentence.capitalize())
        
        finalText = '. '.join(finalTextList)
        return finalText
