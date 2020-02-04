lines = []
number = input()

sum_number = 0
count = 0
for num in range(int(number)):
    line = input()
    lines.append(line)

for line in lines:
    for ox in range(len(line)):
        if line[ox] == 'O':
            count += 1
            sum_number += count
        elif line[ox] == 'X':
            count = 0
    print(sum_number)
    count = 0
    sum_number = 0

