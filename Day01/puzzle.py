# https://adventofcode.com/2024/day/1

first_array = []
second_array = []

with open('input.txt','r') as f:
    for line in f:
        parts = line.strip().split('   ')
        if len(parts) == 2:
            first_array.append(int(parts[0]))
            second_array.append(int(parts[1]))
f.close()

first_array.sort()
second_array.sort()

similarity = 0

for number in first_array:
    similarity = similarity + number * second_array.count(number)

print(similarity)


