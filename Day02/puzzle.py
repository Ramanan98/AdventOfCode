# https://adventofcode.com/2024/day/2

def check(array):
    length = len(array)
    inc_count = 0
    dec_count = 0
    diff_count = 0
    for i in range(0,length-1):
        if array[i]>array[i+1]:
            dec_count = dec_count + 1
        elif array[i]<array[i+1]:
            inc_count = inc_count + 1
        else:
            return False
        absolute_difference = abs(array[i] - array[i+1])
        if absolute_difference >=1 and absolute_difference <=3:
            diff_count = diff_count + 1
    inc_dec = (dec_count == 0 and inc_count == length - 1) or (inc_count == 0 and dec_count == length - 1)
    return inc_dec and (diff_count == length - 1)

def problem_dampener(array):
    array_copy = array
    for i in range(0,len(array_copy)):
        index_to_remove = i
        removed_element = array.pop(index_to_remove)
        if check(array):
            return True
        array.insert(index_to_remove,removed_element)
    return False

def count_safe_reports():
    safe_reports = 0
    with open('input.txt','r') as f:
        for line in f:
            array = line.split(' ')
            array = [int(element) for element in array]
            if(check(array)):
                safe_reports = safe_reports + 1
    f.close()
    return safe_reports

def count_safe_reports_with_dampener():
    safe_reports = 0
    with open('input.txt','r') as f:
        for line in f:
            array = line.split(' ')
            array = [int(element) for element in array]
            if(problem_dampener(array)):
                safe_reports = safe_reports + 1
    f.close()
    return safe_reports

def main():
    safe_reports = count_safe_reports()
    print(safe_reports)
    safe_reports_with_dampener = count_safe_reports_with_dampener()
    print(safe_reports_with_dampener)

if __name__ == "__main__":
    main()
