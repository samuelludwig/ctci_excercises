"""
    Write a method to replace all spaces in a string with '%20'. 
    You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given
    the true length of the string.
"""
def preprocess(string):
    preprocessed_string = ''.join(string.strip())
    return preprocessed_string

def get_space_locations(string):
    list_of_space_locations = []
    for i in range(string.__len__()):
        if string[i] == ' ':
            list_of_space_locations.append(i)
    return list_of_space_locations

def urlify(string, length):
    ps = ''.join(preprocess(string))
    sp_loc = get_space_locations(ps)
    url = []
    char_position = 0
    for char in ps:
        if char_position in sp_loc:
            url.append("%20")
        else:
            url.append(char)
        char_position += 1
    built_url = ''.join(url)
    return built_url

"""TESTS"""

def is_returning_same_string_if_no_spaces():
    if urlify("carrot", 6) == "carrot":
        return 1
    else:
        return 0

def is_returning_urlified_string():
    if urlify("who am i    ", 12) == "who%20am%20i":
        return 1
    else:
        return 0

def preprocess_returns_stripped_string():
    if preprocess("    i am you      ") == "i am you":
        return 1
    else:
        return 0

def get_space_locations_returns_list_of_locations():
    if get_space_locations("that is nonsense") == [4, 7]:
        return 1
    else:
        return 0

def test_urlify():
    print(is_returning_same_string_if_no_spaces())
    print(is_returning_urlified_string())
    print(preprocess_returns_stripped_string())
    print(get_space_locations_returns_list_of_locations())

test_urlify()