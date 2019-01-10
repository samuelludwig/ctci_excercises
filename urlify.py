"""
    Write a method to replace all spaces in a string with '%20'. 
    You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given
    the true length of the string.
"""

def urlify(string, length):
    for i in range(string.__len__()):
        if string[i] == ' ':
            for x in range(string.__len__()-i, 0, -1):
                string[x] = string[x-3]
        string[i] = '%'
        string[i+1] = '2'
        string[i+2] = '3'

"""TESTS"""

def is_returning_same_string_if_no_spaces():
    if urlify("carrot", 6) == "carrot":
        return 1
    else:
        return 0

def is_returning_urlified_string():
    if urlify("who am i    ", 12) == "who%20am%20i%20":
        return 1
    else:
        return 0

def test_urlify():
    print(is_returning_same_string_if_no_spaces())
    print(is_returning_urlified_string())

test_urlify()