import time

timestamp = time.strftime("%H:%M:%S")
print("Current time: ", timestamp)
hour = int(time.strftime("%H"))

if 5 < hour < 12:
    print("Gm")
elif 12 <= hour < 17:
    print("Ga")
else:
    print("Gn")