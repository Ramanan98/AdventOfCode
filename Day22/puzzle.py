# https://adventofcode.com/2024/day/22

def read_input():
    start = []
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            start.append(int(line))
    return start

def get_secret_number(num):
    num = num ^ (num * 64) % 16777216
    num = num ^ (num // 32) % 16777216
    num = num ^ (num * 2048) % 16777216
    return num

def get_secret_number_extra(num):
    num = num ^ (num * 64) % 16777216
    num = num ^ (num // 32) % 16777216
    num = num ^ (num * 2048) % 16777216
    return num, num % 10

def get_2000th_secret_number(num):
    for _ in range(2000):
        num = get_secret_number(num)
    return num

def get_sequence(lst, indices):
    start = indices[0]
    end = indices[1]
    sequence = []
    for i in range(start + 1, end + 1):
        sequence.append(lst[i] - lst[i - 1])
    return sequence

def get_bananas(sequence, numbers_info):
    total_bananas = 0
    for num, info in numbers_info.items():
        lst = numbers_info[num][1]
        seq_len = len(sequence)
        idx = -1
        for i in range(len(lst) - seq_len + 1):
            if lst[i:i + seq_len] == sequence:
                idx = i + seq_len - 1
                break
        if idx != -1:
            bananas = numbers_info[num][0][idx]
            total_bananas += bananas
        else:
            pass
    return total_bananas

def find_sequences_with_max(nums):
    max_value = max(nums)
    max_indexes = [i for i, num in enumerate(nums) if num == max_value]
    result = []
    for i in max_indexes:
        if i >= 4:  # Check if the index is greater than or equal to 3
            sequence = [i-3, i-2, i-1, i]
            result.append(sequence) 
    return result

def main():
    start = read_input()
    result = 0
    for num in start:
        result += get_2000th_secret_number(num)
    print(result) # Part 1

    numbers_info = {}
    for input_num in start:
        num = input_num
        ones_array = []
        ones_array.append(num % 10)
        differences = []
        differences.append(None)
        for _ in range(1999):
            num, ones = get_secret_number_extra(num)
            ones_array.append(ones)
        for i in range(1, len(ones_array)):
            differences.append(ones_array[i] - ones_array[i - 1])
        numbers_info[input_num] = ones_array, differences

    max_bananas = 0
    for num, info in numbers_info.items():
        sequence_pos = find_sequences_with_max(numbers_info[num][0])
        if sequence_pos:
            for index in sequence_pos:
                start = index[0]
                sequence = numbers_info[num][1][start:start+4]
                bananas = get_bananas(sequence, numbers_info)
                if bananas > max_bananas:
                    max_bananas = bananas
    print(max_bananas)

if __name__ == "__main__":
    main()