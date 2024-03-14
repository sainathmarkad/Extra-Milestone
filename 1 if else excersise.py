
import time
t = time.strftime('%H:%M:%S')
print(t)
hour = int(time.strftime('%H'))
minute = int(time.strftime('%M'))
second = int(time.strftime('%S'))

if(3 < hour <= 12):
    print("Good Morning")
elif(12 < hour <= 16):
    print("Good Afternoon")
elif(17 < hour <= 19):
    print("Good Evening")
else:
    print("Good Night")
