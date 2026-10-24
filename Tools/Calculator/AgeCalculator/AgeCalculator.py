from Global import Global
from Helper import Helper
from datetime import datetime
import calendar


class AgeCalculator:
    def Start(self):
        while True:
            print("Age Calculator".center(Global.HeaderFormatConstant, "="))

            currentTime = datetime.now()

            day = Helper.inputInt(
                f"{"Enter the day you were born (1-31)":<{Global.TextFormatConstant}}: ",
                min_val=1,
                max_val=31,
            )
            month = Helper.inputInt(
                f"{"Enter the month you were born (1-12)":<{Global.TextFormatConstant}}: ",
                min_val=1,
                max_val=12,
            )
            year = Helper.inputInt(
                f"{"Enter the year you were born":<{Global.TextFormatConstant}}: ",
                min_val=1,
                max_val=currentTime.year,
            )

            try:
                birthDate = datetime(year, month, day)
            except ValueError as e:
                print(f"{"Error":<{Global.TextFormatConstant}}: {e}")
                continue

            if birthDate > currentTime:
                print(f"{"Error":<{Global.TextFormatConstant}}: Birth date cannot be in the future.")
                continue

            yearAge = currentTime.year - birthDate.year
            monthAge = currentTime.month - birthDate.month
            dayAge = currentTime.day - birthDate.day

            if dayAge < 0:
                prevMonth = currentTime.month - 1 if currentTime.month > 1 else 12
                prevYear = currentTime.year if currentTime.month > 1 else currentTime.year - 1
                _, daysInPrevMonth = calendar.monthrange(prevYear, prevMonth)

                dayAge += daysInPrevMonth
                monthAge -= 1

            if monthAge < 0:
                monthAge += 12
                yearAge -= 1

            print("=" * Global.HeaderFormatConstant)
            print(
                f"{"You were born on":<{Global.TextFormatConstant}}: {birthDate.strftime('%A, %d-%m-%Y')}"
            )
            print(
                f"{"Today's date is":<{Global.TextFormatConstant}}: {currentTime.strftime('%A, %d-%m-%Y')}"
            )
            print(
                f"{"You are":<{Global.TextFormatConstant}}: {yearAge} years, {monthAge} months, {dayAge} days old!"
            )

            if not Helper.inputConfirmation(
                f"{"Calculate again? (Y/N)":<{Global.TextFormatConstant}}: "
            ):
                return
