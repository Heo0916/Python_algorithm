input = "abcba"


def is_palindrome(string):
    long = len(string)
    for i in range(long):
        if string[i] == string[long-i-1]:
            continue
        else:
            return False
    return True

print(is_palindrome(input))
