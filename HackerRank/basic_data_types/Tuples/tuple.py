# Note: HackerRank's test cases for this problem expect the legacy hashing 
# algorithm used in Python 3.7 and earlier. If you get a "Wrong Answer" 
# in the Python 3 environment, switch the language dropdown to PyPy3 or 
# use the custom hashing workaround.

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