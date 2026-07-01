from Global import Global
from Helper import Helper
from datetime import datetime
import calendar

class AgeCalculator:
    def Start(self):
        while True:
            print("Age Calculator".center(Global.HeaderFormatConstant, "="))

            day = Helper.inputInt(f"{"Enter the day you were born (as date)":<{Global.TextFormatConstant}}: ")
            month = Helper.inputInt(f"{"Enter the month you were born (as number)":<{Global.TextFormatConstant}}: ")
            year = Helper.inputInt(f"{"Enter the year you were born":<{Global.TextFormatConstant}}: ")

            try:
                dateBorned = datetime.strptime(f"{day}-{month}-{year}", "%d-%m-%Y")
            except Exception as e:
                print(f"{"Error":<{Global.TextFormatConstant}}: {e}")
                continue
            
            currentTime = datetime.now()

            yearAge = currentTime.year - dateBorned.year
            monthAge = currentTime.month - dateBorned.month
            dayAge = currentTime.day - dateBorned.day

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
            print(f"{"You were born in":<{Global.TextFormatConstant}}: {dateBorned.strftime("%A, %d-%m-%Y")}")
            print(f"{"Today date is":<{Global.TextFormatConstant}}: {currentTime.strftime("%A, %d-%m-%Y")}")
            print(f"{"You are":<{Global.TextFormatConstant}}: {yearAge} years, {monthAge} months, {dayAge} days old!")

            if not Helper.inputConfirmation(f"{"Calculate again? (Y/N)":<{Global.TextFormatConstant}}: "):
                return