"""
    Implement a method to perform basic string compression using the counts of repeated characters.
    Ex: aabcccccaaa -> a2b1c5a3
    If the "compressed" string would not end up being smaller than the original string, return the original.
    Assume all characters encountered are lowercase letters (a-z).
"""

def compress_str(string):
    # compression_loop
    lstring = list(string)
    pressed_string = []
    current_let = lstring[0]
    let_count = 0
    for i in range(0, lstring.__len__(), 1):
        if (current_let != lstring[i]):
            pressed_string.append(current_let)
            pressed_string.append(let_count)
            current_let = lstring[i]
            let_count = 1
        else:
            let_count += 1
    pressed_string.append(current_let)
    pressed_string.append(let_count)
    
    if pressed_string.__len__() >= string.__len__():
        return string
    return "".join(map(str, pressed_string))

""" TEST METHODS """

def rets_compressed_corr():
    if(compress_str("aabcccccaaa") == "a2b1c5a3"):
        return 1
    else:
        return 0

def rets_uncompressed_corr():
    if(compress_str("aabcca") == "aabcca"):
        return 1
    else:
        return 0

if __name__ == "__main__":
    print(rets_compressed_corr())
    print(rets_uncompressed_corr())