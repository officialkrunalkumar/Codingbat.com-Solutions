'''
Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.


end_other('Hiabc', 'abc') → True
end_other('AbC', 'HiaBc') → True
end_other('abc', 'abXabc') → True
'''
def end_other(s1, s2):
    s1_lower = s1.lower()
    s2_lower = s2.lower()
    return s1_lower.endswith(s2_lower) or s2_lower.endswith(s1_lower)
