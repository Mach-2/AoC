# Task: count the number of times a depth measurement increases from the previous measurement

# variables for current and previous measurements
curr = 0
prev = 0

# inc tracks number of increases
inc = 0

# begin reading in lines from file
file = open("input.txt", 'r')

# Read first line
curr = file.readline()

while True:
    prev = curr
    curr = file.readline()

    if not curr:
        break;

    if int(curr) > int(prev):
        inc += 1

file.close()

print(inc)
