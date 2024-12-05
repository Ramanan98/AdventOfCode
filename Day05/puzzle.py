# https://adventofcode.com/2024/day/5

import re

updates = []
pattern = r"^(.*?),(.*)$"
orders = []

# Modified merge sort for sorting based on ordering rules
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(arr, left, right)

def merge(arr, left, right):
    sorted_arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if check_two_elements(arr, left[i], right[j]):
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    
    return sorted_arr

# Get index of elements and elements as a dictionary
def get_index_dict(lst):
    index_dict = {}
    for i in range(0, len(lst)):
        index_dict[lst[i]] = i
    return index_dict

# Checks two elements of a list against the ordering rules
def check_two_elements(update, a, b):
    for order in orders:
        if a not in [order[0],order[1]] or b not in [order[0],order[1]]:
            continue
        else:
            if a == order[0] and b == order[1]:
                if update.index(a) > update.index(b):
                    return False
            else:
                if update.index(a) < update.index(b):
                    return False
    return True

# Checks whether a list is a valid ordering according to the ordering rules
def check_valid(update, index_dict):
    for order in orders:
        if order[0] not in update or order[1] not in update:
            continue
        else:
            if index_dict[order[0]] > index_dict[order[1]]:
                return False
    return True

# Get sum of middle elements of a list of lists
def get_sum_of_middle_elements(lists):
    sum = 0
    for lst in lists:
        sum = sum + int(lst[len(lst) // 2])
    return sum

def main():
    valid_lists = []
    violating_lists = []
    corrected_lists = []

    # Read ordering rules and lists from input text file
    with open('input.txt','r') as f:
        input = f.readlines()
        for update in input:
            if ('|') in update:
                ordering = update.split('|')
                ordering[1] = ordering[1][:-1]
                orders.append(ordering)
            if(re.match(pattern,update)):
                updates.append(update)
    f.close()

    for update in updates:
        index_dict = {}
        update = update[:-1]
        elements = update.split(',')
        index_dict = get_index_dict(elements)
        if(check_valid(elements, index_dict)):
            valid_lists.append(elements)
        else:
            violating_lists.append(elements)
    # Part 1
    print(get_sum_of_middle_elements(valid_lists))

    # Part 2
    # Sort all violating lists based on ordering rules
    for violating_list in violating_lists:
        sorted_list = merge_sort(violating_list)
        corrected_lists.append(sorted_list)
    print(get_sum_of_middle_elements(corrected_lists))

if __name__ == "__main__":
    main()