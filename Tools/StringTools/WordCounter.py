from Global import Global
from Helper import Helper


class WordCounter:
    def Start(self):
        while True:
            print("Word Counter".center(Global.HeaderFormatConstant, "="))
            print("Enter a sentence or text below")
            print("=" * Global.HeaderFormatConstant)

            sentence = input(f"{"Sentence":<{Global.TextFormatConstant}}: ")

            count = self.calculateWord(sentence)
            char_count = len(sentence)
            char_no_spaces = len(sentence.replace(" ", ""))

            print("-" * Global.HeaderFormatConstant)
            print(f"{"Total Words":<{Global.TextFormatConstant}}: {count}")
            print(f"{"Total Characters":<{Global.TextFormatConstant}}: {char_count}")
            print(f"{"Characters (no spaces)":<{Global.TextFormatConstant}}: {char_no_spaces}")

            if not Helper.inputConfirmation(
                f"{"Count another text? (Y/N)":<{Global.TextFormatConstant}}: "
            ):
                return

    def calculateWord(self, sentence: str):
        return len(sentence.split())
