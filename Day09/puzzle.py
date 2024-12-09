def read_file():
    with open('input.txt','r') as f:
        data = f.read()
    f.close()
    return data

def parse_input(data):
    numbers = [int(i) for i in data]
    return numbers

def build_file_system(numbers):
    file_system = []
    file_id = 0
    for i in range(0, len(numbers)):
        if i % 2 == 0:
            file_system.extend([file_id] * numbers[i])
            file_id += 1
        else:
            file_system.extend([-1] * numbers[i])
    return file_system

def compact(file_system):
    while True:
        free_space_index = -1
        for i in range(len(file_system)):
            if file_system[i] == -1:
                free_space_index = i
                break
                
        if free_space_index == -1:
            break
            
        rightmost_file_index = -1
        for i in range(len(file_system)-1, free_space_index, -1):
            if file_system[i] != -1:
                rightmost_file_index = i
                break
                
        if rightmost_file_index == -1:
            break

        file_system[free_space_index] = file_system[rightmost_file_index]
        file_system[rightmost_file_index] = -1           
    return file_system

def compact_whole(file_system):
    max_file_id = max(x for x in file_system if x != -1)
    
    for file_id in range(max_file_id, -1, -1):
        file_blocks = [i for i, x in enumerate(file_system) if x == file_id]
        if not file_blocks:
            continue
            
        file_size = len(file_blocks)
        current_start = file_blocks[0]
        
        best_position = None
        consecutive_free = 0
        for i in range(current_start):
            if file_system[i] == -1:
                consecutive_free += 1
                if consecutive_free >= file_size:
                    best_position = i - file_size + 1
                    break
            else:
                consecutive_free = 0
                
        if best_position is not None:
            for pos in file_blocks:
                file_system[pos] = -1
            for i in range(file_size):
                file_system[best_position + i] = file_id
                
    return file_system

def get_checksum_part1():
    data = read_file()
    numbers = parse_input(data)
    file_system = build_file_system(numbers)
    compacted_file_system = compact(file_system)
    checksum = 0
    for index, block in enumerate(compacted_file_system):
        if block != -1:
            checksum += index * block
    return checksum

def get_checksum_part2():
    data = read_file()
    numbers = parse_input(data)
    file_system = build_file_system(numbers)
    compacted_file_system = compact_whole(file_system)
    checksum = 0
    for index, block in enumerate(compacted_file_system):
        if block != -1:
            checksum += index * block
    return checksum

def main():
    print(get_checksum_part1())
    print(get_checksum_part2())

if __name__ == "__main__":
    main()