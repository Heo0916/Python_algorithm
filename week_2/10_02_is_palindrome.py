input = "소주만병만주소"

#소주만병만주소
#is_palindrome(string) = 맨 앞뒤 검사를 했다면 is_palindrome[1:-1]

def is_palindrome(string):
    if string[0] != string[-1]:
        return False
    if len(string) <= 1:
        return True
    return is_palindrome(string[1:-1])

print(is_palindrome(input))
