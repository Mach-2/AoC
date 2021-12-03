# Calculate the horizontal position and depth you would have after following the planned course
# What do you get if you multiply your final horizontal position by your final depth?

depth = 0
horiz = 0

def mover(instruction):
    global depth
    global horiz
    direction = instruction[0]
    magnitude = int(instruction[1])
    if direction == 'forward':
        horiz += magnitude
    elif direction == 'down':
        depth += magnitude
    elif direction == 'up':
        depth -= magnitude


with open('Day2.txt','r') as f:
    lines = f.readlines()


for line in lines:
    movement = line.strip().split(' ')
    mover(movement)

print(depth * horiz)
