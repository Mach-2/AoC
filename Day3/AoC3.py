# Each bit in the gamma rate can be determined by finding the most common bit in the corresponding position of all
# numbers in the diagnostic report.

# function for most common bit
def common_bit(position, diagnostic):
    zero = 0
    one = 0
    for x in range(len(diagnostic)):
        if diagnostic[x][position] == '0':
            zero += 1
        else:
            one += 1
    if zero > one:
        return 0
    else:
        return 1


# Read in file
with open('input.txt', 'r') as f:
    diagnostic = [line.strip() for line in f]

# #Determine gamma and epsilon rates (epsilon is just gonna be the inverse of gamma)
gamma = ''
epsilon = ''
for p in range(len(diagnostic[0])):
    bit = common_bit(p, diagnostic)
    if bit == 1:
        gamma += str(1)
        epsilon += str(0)
    else:
        gamma += str(0)
        epsilon += str(1)


# calculate power
power = int(gamma,2) * int(epsilon,2)
print(power)

#
# ### Part 2
#
# # Life support = oxygen * CO2 scrubber
#
# # To find oxygen generator rating, determine the most common value (0 or 1) in the current bit position,
# # and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values
# # with a 1 in the position being considered.

# Calculate oxygen generator rating
OGR = diagnostic
for p in range(len(gamma)):
    if len(OGR) == 1:
        break
    blacklist = []
    for x in range(len(OGR)):
        bit = str(common_bit(p, OGR))
        if OGR[x][p] != bit:
            blacklist.append(x)
    # Make a new OGR list with only binaries that have the most common bit in position p
    OGR = [v for i, v in enumerate(OGR) if i not in blacklist]

# Find CO2 scrubber rating
CSR = diagnostic
for p in range(len(gamma)):
    if len(CSR) == 1:
        break
    blacklist = []
    for x in range(len(CSR)):
        bit = common_bit(p, CSR)
        if bit == 1: # Need inverse of most common bit
            bit = '0'
        else: bit = '1'
        if CSR[x][p] != bit:
            blacklist.append(x)
    # Make a new CSR list with only binaries that have the most common bit in position p
    CSR = [v for i, v in enumerate(CSR) if i not in blacklist]

# Calculate life support
lifesupport = int(OGR[0],2) * int(CSR[0],2)
print(lifesupport)
