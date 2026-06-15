import time
import datetime
from notifypy import Notify
import chime

print("Hello,This is a Recoder timer \n-----------ADD TIMER-----------\n")

Timer = float(input("Enter a time in minute: "))
Category = input("Enter why you want to set timer?: ")

Start_timer = time.time()
print("\n--------Timer started!--------\n")

time.sleep(Timer * 60)
End_timer = time.time()
Set_time = End_timer - Start_timer

#
notifiction = Notify()
notifiction.title = "Times up !"
notifiction.message = f"You time of {Timer*60.0} min is over"
notifiction.send()


now = datetime.datetime.now()
chime.info()

with open("time_sheet.txt", "a") as file:
    file.write(
        f"\n{Set_time:.2f}\t\t{Category}\t\t{now.strftime("%H:%M")}\t\t{now.date()} "
    )
