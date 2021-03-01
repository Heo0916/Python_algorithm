from collections import deque

balanced_parentheses_string = "()))((()"
# 균형잡힌 괄호 문자열 -> 올바른 괄호 문자열

def is_correct_parenthesis(string): #올바른 괄호 문자열인지 확인
    stack = []
    for s in string:
        if s == "(":
            stack.append(s)
        elif stack:
            stack.pop()
    return len(stack) == 0
#1. 입력이 빈 문자열인 경우, 빈 문자열 반환
def reverse_parenthesis(string):
    reversed_string = ""
    for char in string[1:-1]:
        if char == '(':
            reversed_string += ')'
        else:
            reversed_string += '('
    return reversed_string

def separate_to_u_v(string):
    queue = deque(string)
    left, right = 0, 0
    u, v = "", ""
    while queue:
        char = queue.popleft()
        u += char
        if char == '(':
            left += 1
        else:
            right += 1
        if left == right:
            break

    v = ''.join(list(queue))
    return u, v

def change_to_correct_parenthesis(string):
    if string == "":
        return ""
    # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, b로 분리.
    # 단, u는 "균형잡힌 괄호 문자열로" 더 이상 분리할 수 없어야 하며
    # v는 빈 문자열이 될 수 있습니다.
    # ( ) 개수 가 같아야 한다.
    u, v = separate_to_u_v(string)

    #3. 문자열 u 가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행한다.
    # -> change_to_correct_parenthesis 다시 수행
    # 3-1 수행한 결과 문자열을 u에 이어붙인 뒤 반환
    if is_correct_parenthesis(u):
        return u + change_to_correct_parenthesis(v)
    # 4. 문자열 u가 올바른 괄호 문자열이 아니라면 아래 과정을 수행합니다.
    # 4-1. 빈 문자열에 첫 번째 문자로 (를 붙입니다.
    # 4-2 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
    # 4-3 )를 다시 붙입니다.
    # 4-4. u의 첫번째 문자와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집에서 뒤에 붙입니다.
    else:
      return "(" + change_to_correct_parenthesis(v) + ")" + reverse_parenthesis(u[1:-1])

def get_correct_parentheses(balanced_parentheses_string):
    if is_correct_parenthesis(balanced_parentheses_string):
        return balanced_parentheses_string
    else:
       return change_to_correct_parenthesis(balanced_parentheses_string)

print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!
