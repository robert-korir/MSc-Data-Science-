import math
x = 1
#print(math.sin(x))
#print(math.sin(math.pi/2))
#print(0x42)
#print(len('Hello\n'))
#print(0b01110000)

"""
Create a flowchart OR structogram for the following task.

1. The program input is the current time in hours. Input format examples: 2, 12, 16, 19. (24 hour format)
2. The greetings change depending on the time of the day.
“Good morning” is used from 5:00 a.m. (5) to 12:00 p.m. (12) whereas
“Good afternoon” time is from 12:00 p.m. to 6:00 p.m. (18)
“Good evening” is often used after 6 p.m. (18).
3. The output of the program is a greeting according to the time. Output format: GOOD MORNING, GOOD AFTERNOON, GOOD EVENING.

If you are writing code (not a requirement), upload it as well.
"""
current_time = int(input("input the time in hours:"))
if (current_time < 12 and current_time >= 5):
    print('Good morning')
elif(current_time >= 12 and current_time <18):
    print('Good afternoon')
else:
    print('Good evening')
        