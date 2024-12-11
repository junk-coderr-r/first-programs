#basic countdown script, first thing i've ever made.

import time

x = int(input("Give a countdown number! "))

if x <= 0:
    print("Countdown non-compatable with 0 or negative numbers.")
    exit()

while x > 0:
    print(x)
    x-=1
    time.sleep(.1) #keeps countdowns from being near instant
else:
    print("Done!")
