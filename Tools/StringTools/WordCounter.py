from Global import Global

class WordCounter:
    def Start(self):
        print("Word Counter".center(Global.HeaderFormatConstant))
        print("Enter a sentence below")
        print("=" * Global.HeaderFormatConstant)

        sentence = input(f"{"Sentence":<{Global.TextFormatConstant}}: ")

        count = self.calculateWord(sentence)

        print(f"{"Total words":<{Global.TextFormatConstant}}: {count}")
        
    def calculateWord(self, sentence: str):
        splitted = sentence.split(' ')
        count = len(splitted)
        return count