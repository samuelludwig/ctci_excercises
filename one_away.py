"""
    There are three types of edits that can be performed on strings: insert a character,
    remove a character, or replace a character. Given two strings, write a function to 
    determine if they are one (or zero) edits away from each other.

    Example:
    pale -> ple == true
    pale -> bake == false
"""

def is_one_away(string1, string2):
    descrepencies_found = 0
    string1 = list(string1)
    string2 = list(string2)
    if string1.__len__() == string2.__len__(): # replacements
        for i in range(string1.__len__()):
            if (string1[i] != string2[i]) and (descrepencies_found > 0):
                return False
            elif (string1[i] != string2[i]):
                descrepencies_found += 1
        return True
    elif (string1.__len__() != string2.__len__()) and (abs(string1.__len__() - string2.__len__()) == 1): # inserts/deletes
        # compare str1[i] to str2[i], if a descrepency is found, shift smaller string over one, and continue comparing
        if (string1.__len__() > string2.__len__()):
            string2.append(" ")
            for c in range(string1.__len__()):
                if (string1[c] != string2[c]) and (descrepencies_found > 0):
                    return False
                elif (string1[c] != string2[c]):
                    descrepencies_found += 1
                    for i in range(string2.__len__()-1, c, -1):
                        string2[i] = string2[i-1]
            return True
        elif (string1.__len__() < string2.__len__()):
            string1.append(" ")
            for c in range(string2.__len__()):
                if (string1[c] != string2[c]) and (descrepencies_found > 0):
                    return False
                elif (string1[c] != string2[c]):
                    descrepencies_found += 1
                    for i in range(string1.__len__()-1, c, -1):
                        string1[i] = string1[i-1]
            return True
    else:
        return 0

""" TEST METHODS """

def rets_true_when_ins_needed():
    if is_one_away("pale", "ple") == True:
        return 1
    else:
        return 0 

def rets_true_when_del_needed():
    if is_one_away("pale", "pales") == True:
        return 1
    else:
        return 0 

def rets_true_when_rep_needed():
    if is_one_away("pale", "bale") == True:
        return 1
    else:
        return 0

def rets_true_when_equal():
    if is_one_away("pale", "pale") == True:
        return 1
    else:
        return 0

def rets_false_when_more_needed():
    if is_one_away("pale", "bake") == False:
        return 1
    else:
        return 0

if __name__ == "__main__":
    print(rets_true_when_ins_needed())
    print(rets_true_when_del_needed())
    print(rets_true_when_rep_needed())
    print(rets_true_when_equal())
    print(rets_false_when_more_needed())