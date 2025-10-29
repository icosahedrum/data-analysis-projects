# 1. Declare and assign the variables here:
name = 'Determination'
speed_mph = 17500
distance_to_mars_km = 225000000
distance_to_moon_km = 384400
miles_per_km = .621

# 2. Use print() to print the 'type' each variable. Print one item per line.
print(type(name))
print(type(speed_mph))
print(type(distance_to_mars_km))
print(type(distance_to_moon_km))
print(type(miles_per_km))

# Code your solution to exercises 3 and 4 here:
distance_to_mars_miles = distance_to_mars_km * miles_per_km
time_to_mars_in_hours = distance_to_mars_miles/speed_mph
time_to_mars_in_days = time_to_mars_in_hours/24

print(f'{name} will take {time_to_mars_in_days} days to reach Mars')

# Code your solution to exercise 5 here
distance_to_moon_miles = distance_to_moon_km * miles_per_km
time_to_moon_in_hours = distance_to_moon_miles/speed_mph
time_to_moon_in_days = time_to_moon_in_hours/24

print(f'{name} will take {time_to_moon_in_days} days to reach the Moon')
