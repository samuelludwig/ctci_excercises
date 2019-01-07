"""Check if two strings are permutations of one another
"""

def preprocess(string):
    return sorted(string.lower())

def check_permutation(string1, string2):
    s1 = ''.join(preprocess(string1))
    s2 = ''.join(preprocess(string2))

    if s1 == s2:
        return True
    else:
        return False

"""TESTS"""

def returns_false_if_not_permutations():
    if check_permutation("door", "racecar") == False:
        return 1
    else:
        return 0

def returns_true_if_permutations():
    if check_permutation("door", "odor") == True:
        return 1
    else:
        return 0
    
def test_check_permutation():
    print(returns_false_if_not_permutations())
    print(returns_true_if_permutations())

test_check_permutation()