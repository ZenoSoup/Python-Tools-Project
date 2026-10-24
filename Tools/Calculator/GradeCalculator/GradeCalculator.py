from Global import Global
from Helper import Helper


class GradeCalculator:
    def Start(self):
        while True:
            print("Grade Calculator".center(Global.HeaderFormatConstant, "="))

            grades = []

            print("Please enter the subject name and your grade")
            print('Enter "exit" in subject name to finish')
            print("=" * Global.HeaderFormatConstant)

            i = 1
            while True:
                subject = input(f"{f'Subject name no-{i}':<{Global.TextFormatConstant}}: ").strip()

                if subject.lower() == "exit":
                    break

                if not subject:
                    print("Subject name cannot be empty.")
                    continue

                grade = Helper.inputFloat(f"{'Grade':<{Global.TextFormatConstant}}: ", min_val=0.0)
                grades.append((subject, grade))
                i += 1

            if not grades:
                print("No grades were entered.")
            else:
                total = sum(g for _, g in grades)
                average = total / len(grades)

                print("=" * Global.HeaderFormatConstant)
                for idx, (subject, grade) in enumerate(grades, start=1):
                    print(f"{f'{idx}. {subject}':<{Global.TextFormatConstant}}: {grade}")

                print(f"{'Total':<{Global.TextFormatConstant}}: {total:.2f}")
                print(f"{'Average':<{Global.TextFormatConstant}}: {average:.2f}")

            if not Helper.inputConfirmation(f"{'Calculate again? (Y/N)':<{Global.TextFormatConstant}}: "):
                return
