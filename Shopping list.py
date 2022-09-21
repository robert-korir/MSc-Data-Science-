
# Python3 Program to calculate speed,
# distance and time

# Function to calculate speed
def cal_speed(dist, time):
	print(" Distance(km) :", dist);
	print(" Time(hr) :", time);
	return dist / time;

# Function to calculate distance traveled
def cal_dis(speed, time):
	print(" Time(hr) :", time) ;
	print(" Speed(km / hr) :", speed);
	return speed * time;

# Function to calculate time taken
def cal_time(dist, speed):
	print(" Distance(km) :", dist);
	print(" Speed(km / hr) :", speed);
	return dist / speed;

# Driver Code

# Calling function cal_speed()
print(" The calculated Speed(km / hr) is :",cal_speed(118, 89 ));
print("");

# Calling function cal_dis()
print(" The calculated Distance(km) :",cal_dis(75, 90));
print("");

# Calling function cal_time()
print(" The calculated Time(hr) :",cal_time(50, 40));

# This code is contributed
# by mits
