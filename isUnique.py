"""Implement an algorithm to determine if a string has all unique characters."""
def preprocess(string):
    if string == "":
        print("Error: Invalid String")
        return "ERROR"
    else:
        return sorted(string.lower())

def is_unique(string):
    s = preprocess(string)
    for i in range(s.__len__()-1):
        if s[i] == s[i+1]:
            return False
    return True

"""TESTS"""
def returns_error_when_string_is_invalid():
    if is_unique("") == False:
        return 1
    else:
        return 0

def preprocess_formats_output_correctly():
    if preprocess("ApPlE") == ["a", "e", "l", "p", "p"]:
        return 1
    else:
        return 0

def is_unique_returns_false_when_nonunique_char_found():
    if is_unique("door") == False:
        return 1
    else:
        return 0

def is_unique_returns_true_when_chars_all_unique():
    if is_unique("grey") == True:
        return 1
    else:
        return 0

def test_is_unique():
    print(returns_error_when_string_is_invalid())
    print(preprocess_formats_output_correctly())
    print(is_unique_returns_false_when_nonunique_char_found())
    print(is_unique_returns_true_when_chars_all_unique())

test_is_unique()
