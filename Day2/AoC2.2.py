# down X increases your aim by X units.
# up X decreases your aim by X units.
# forward X does two things:
#    It increases your horizontal position by X units.
#    It increases your depth by your aim multiplied by X

# Calculate the horizontal position and depth you would have after following the planned course
# What do you get if you multiply your final horizontal position by your final depth?

depth = 0
horiz = 0
aim = 0

def mover(instruction):
    global depth
    global horiz
    global aim
    direction = instruction[0]
    magnitude = int(instruction[1])
    if direction == 'forward':
        horiz += magnitude
        depth += aim*magnitude
    elif direction == 'down':
        aim += magnitude
    elif direction == 'up':
        aim -= magnitude


with open('input.txt', 'r') as f:
    lines = f.readlines()


for line in lines:
    movement = line.strip().split(' ')
    mover(movement)

print(depth * horiz)
