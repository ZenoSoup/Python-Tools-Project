from Global import Global
from Helper import Helper

class GradeCalculator:
    def Start(self):
        print("Grade Calculator".center(Global.HeaderFormatConstant, "="))
        
        grades = {}

        print("Please enter the subject name and your grade")
        print("Enter \"exit\" in subject name to finish")

        print("=" * Global.HeaderFormatConstant)

        i = 1

        while True:
            subject = input(f"{f"Subject name no-{i}":<{Global.TextFormatConstant}}: ")
            
            if subject.lower() == "exit":
                break

            grade = Helper.inputFloat(f"{"Grade":<{Global.TextFormatConstant}}: ")
            grades[subject] = grade
            i += 1

        total = 0

        for grade in grades.values():
            total += grade

        average = total / len(grades)

        print("=" * Global.HeaderFormatConstant)

        for i, (subject, grade) in enumerate(grades.items()):
            print(f"{f"{i}. {subject}":<{Global.TextFormatConstant}}: {grade}")

        print(f"{"Total":<{Global.TextFormatConstant}}: {total}")
        print(f"{"Average":<{Global.TextFormatConstant}}: {average}")