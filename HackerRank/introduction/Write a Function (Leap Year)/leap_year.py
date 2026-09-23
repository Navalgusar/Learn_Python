# Difficulty: Easy
# Tags: Print Function, Unpacking Operator

if __name__ == '__main__':
    n = int(input())
    
    print(*range(1, n + 1), sep='')