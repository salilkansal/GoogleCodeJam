input_file = open('small-input.in')
# input_file = open('B-small-practice.in')
n = int(input_file.readline())
print n
direction = {'north': 1, 'east': 2, 'south': 4, 'west': 8}
for a in range(0, n):
    input_data = input_file.readline().split()
    forward = input_data[0]
    backward = input_data[1]
    print forward
    print backward
