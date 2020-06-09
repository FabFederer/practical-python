# bounce.py
#
# Exercise 1.5
# A rubber ball is dropped from a height of 100 meters and each time it hits the ground,
# it bounces back up to 3/5 the height it fell.
# Write a program bounce.py that prints a table showing the height of the first 10 bounces
bounces = 0
bounce_ratio = 3/5
height = 100

while bounces < 10:
    height = round(height * bounce_ratio, 4)
    bounces = bounces + 1
    print("Bounce:", bounces, " Height:", height)
