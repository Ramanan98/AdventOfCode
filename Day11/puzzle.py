# https://adventofcode.com/2024/day/11

from collections import defaultdict

def read_stones():
    stones = []
    with open('input.txt', 'r') as f:
        stones = f.read().split(' ')
        stones = [int(x) for x in stones]
    f.close()
    return stones

def split_number(num):
    num_str = str(num)
    mid = len(num_str) // 2
    left_half = num_str[:mid].lstrip('0')
    right_half = num_str[mid:].lstrip('0')
    left_half = int(left_half) if left_half else 0
    right_half = int(right_half) if right_half else 0
    return (left_half, right_half)

def blink(hash_map):
    hash_map_copy = defaultdict(int)
    for key in list(hash_map.keys()):
        if key == 0:
            hash_map_copy[1] += hash_map[key]
        elif len(str(key)) % 2 == 0:
            left, right = split_number(key)
            hash_map_copy[left] += hash_map[key]
            hash_map_copy[right] += hash_map[key]
        else:
            hash_map_copy[key * 2024] += hash_map[key]
    return hash_map_copy

def blink_n_times(hash_map, n):
    for _ in range(n):
        hash_map = blink(hash_map)
    count = sum(hash_map.values())
    return count

def main():
    hash_map = defaultdict(int)
    stones = read_stones()
    for stone in stones:
        hash_map[stone] += 1
    print(blink_n_times(hash_map, 25)) # Part 1
    print(blink_n_times(hash_map, 75)) # Part 2

if __name__ == "__main__":
    main()