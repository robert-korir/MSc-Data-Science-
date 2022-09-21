'''
Consider 3 vehicles travelling to different locations. Journey details are given below:

Car A - 118 km at 89 kph
Car B - 75 miles at 90 kph
Car C - 50 km at 40 miles an hour

Required:
Create a single function that takes in inputs of distance and speed and returns the time taken in hours.

Hint: Your function should consider the units of the input.

Time = Distance / Speed

1 mile = 1.609 km
1 MPH = 0.621 KPH
'''


def time(distance, speed, km = True, kph = True):
    if (km != True):
        distance = distance * 1.609
    
    if (kph != True):
        speed = speed * 1.609

    time = distance/speed
    hours = int(time)
    minutes = int((time - hours)*60)
    print('{}hrs {}mins'.format(hours, minutes))

time(118, 89)
time(75,90,km=False)
time(50,40,kph=False)