# Difficulty: Easy
# Tags: Tuples, Data Types, Built-ins

def old_tuple_hash(t):
    
    x = 0x345678
    mult = 1000003
    length = len(t)
    
    for y in t:
        length -= 1
        x = (x ^ hash(y)) * mult
        x &= 0xFFFFFFFFFFFFFFFF 
        
        mult += 82520 + length * 2
        mult &= 0xFFFFFFFFFFFFFFFF
    
    x += 97531
    x &= 0xFFFFFFFFFFFFFFFF
    
    
    if x >= 0x8000000000000000:
        x -= 0x10000000000000000
        
    if x == -1:
        x = -2
        
    return x

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
    t = tuple(integer_list)
    
    
    print(old_tuple_hash(t))