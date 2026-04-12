import time
import datetime
import notifypy
import chime

print("Hello,This is a Recoder timer \n-----------ADD TIMER-----------\n")

Timer = float(input("Enter a time in minute: "))
Category = input("Enter why you want to set timer?: ")

Start_timer = time.time()
print("\n--------Timer started!--------\n")

time.sleep(Timer * 60)
End_timer = time.time()
Set_time = End_timer - Start_timer

notification = notifypy.Notify()
notification.title = "Time over !!"
notification.message = f"Timer seted for {Set_time:.2f} is over!"
notification.send()

now = datetime.datetime.now()
chime.info()

with open("time_sheet.txt", "a") as file:
    file.write(
        f"\n{Set_time:.2f}\t\t{Category}\t\t{now.strftime("%H:%M")}\t\t{now.date()} "
    )
