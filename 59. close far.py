'''
Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), while the other is "far", differing from both other values by 2 or more. Note: abs(num) computes the absolute value of a number.


close_far(1, 2, 10) → True
close_far(1, 2, 3) → False
close_far(4, 1, 3) → True
'''
def close_far(a, b, c):
    def is_close(x, y):
        return abs(x - y) <= 1
    
    def is_far(x, y):
        return abs(x - y) >= 2
    
    return (is_close(a, b) and is_far(a, c) and is_far(b, c)) or \
           (is_close(a, c) and is_far(a, b) and is_far(b, c))
