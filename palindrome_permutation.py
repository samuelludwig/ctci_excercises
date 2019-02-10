"""Given a string, write a function to determine if it is a permutation of a palindrome
"""
# A permutation of a palindrome would be something where:
# - If there is an even number of letters, 
#   each letter should appear an even number of times
# - If there is an odd number on letters,
#   each letter *except one* should appear an even amount of times

def preprocess(string):
    string = "".join(string.split()).lower()
    pro_string = "".join(sorted(list(string)))
    return str(pro_string)

def is_palindrome(string):
    s = preprocess(string)
    if (s.__len__() % 2) == 0:
        for i in range(0, s.__len__()-1, 2):
            if (s[i] != s[i+1]):
                return False
        return True
    else:
        # If there is an odd number...
        unpaireds_found = 0
        i = 0
        for c in range(0, s.__len__()-1, 2):
            if (s[i] != s[i+1] and unpaireds_found > 0):
                return False
            elif(s[i] != s[i+1]):
                unpaireds_found += 1
                i += 1
            else:
                i += 2
        return True


"""TEST METHODS"""

def returns_true_when_pal_odd():
    if is_palindrome("atco cta") == True:
        return 1
    else:
        return 0

def returns_true_when_pal_even():
    if is_palindrome("car cra") == True:
        return 1
    else:
        return 0

def returns_false_when_not_pal_odd():
    if is_palindrome("arbor bear") == False:
        return 1
    else:
        return 0

def returns_false_when_not_pal_even():
    if is_palindrome("dog bug") == False:
        return 1
    else:
        return 0

def preprocess_works_correctly():
    if preprocess("  a rbO R beA     r  ") == "aabbeorrr":
        return 1
    else:
        return 0

def run_tests():
    print(returns_true_when_pal_odd())
    print(returns_true_when_pal_even())
    print(returns_false_when_not_pal_odd())
    print(returns_false_when_not_pal_even())
    print(preprocess_works_correctly())

if __name__ == "__main__":
    run_tests()

