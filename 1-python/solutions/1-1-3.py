# Code Challenge 1-1-3¶

'''
a presssure sensor determines whether or not to open a door

When the pressure is larger than 10 we want the door open

otherwise we want it closed

write code to simulate this
'''



# Check if the pressure is greater than 10.
sensor_value = float(input("Enter the pressure sensor value: "))
if sensor_value > 10:
    print(f"Pressure is {sensor_value:.2f}. Door is Open")
else:
    print(f"Pressure is {sensor_value:.2f}. Door is Closed")