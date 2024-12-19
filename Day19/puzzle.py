# https://adventofcode.com/2024/day/19

def parse_input():
    with open('input.txt','r') as f:
        content = f.read().strip()
        patterns = content.split('\n\n')[0].split(', ')
        designs = content.split('\n\n')[1].split('\n')
    f.close()
    return patterns, designs

def can_form_design(design, patterns):
    n = len(design)
    memo = [False] * (n + 1)
    memo[0] = True
    max_len = max(map(len ,patterns))
    for i in range(1, n + 1):
        for j in range(i - 1, max(i - max_len - 1, -1), -1):
            if memo[j] and design[j:i] in patterns:
                memo[i] = True
                break
    return memo[n]

def count_ways_to_form_design(design, patterns):
    n = len(design)
    memo = [0] * (n + 1)
    memo[0] = 1
    max_len = max(map(len, patterns))
    for i in range(1, n + 1):
        for j in range(i - 1, max(i - max_len - 1, -1), -1):
            if design[j:i] in patterns:
                memo[i] += memo[j]
    return memo[n]

def main():
    patterns, designs = parse_input()
    counter_1 = 0
    counter_2 = 0
    for design in designs:
        counter_1 += can_form_design(design, patterns)
    print(counter_1)
    for design in designs:
        counter_2 += count_ways_to_form_design(design, patterns)
    print(counter_2)

if __name__ == "__main__":
    main()