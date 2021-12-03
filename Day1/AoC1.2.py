# count the number of times the sum of measurements in this sliding window increases from the previous sum

# Read data into list
depths = []
inc = 0
with open('input.txt', 'r') as file:
    for line in file:
        depths.append(int(line.rstrip()))


def slide(pos, depthList):  # sliding window of three from the start position
    return depthList[pos] + depthList[pos + 1] + depthList[pos + 2]

for i in range(0,len(depths)-3):
    if slide(i,depths) < slide(i+1,depths):
        inc+=1

print(inc)
