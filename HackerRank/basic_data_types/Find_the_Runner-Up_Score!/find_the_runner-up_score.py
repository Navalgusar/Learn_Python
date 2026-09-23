# Difficulty: Easy
# Tags: Sets, Sorting

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    unique_scores = set(arr)
    
    sorted_scores = sorted(unique_scores, reverse=True)
    
    print(sorted_scores[1])