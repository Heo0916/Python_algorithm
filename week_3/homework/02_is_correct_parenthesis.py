
s = "(())()"
'''
1. ( 괄호가 열림  # stack = [(]
2. ( ( 괄호가 또 열림 stack = ["(","("]
3. ) 괄호가 닫힘 그럼 아까 열린것 중 현재 열린 괄호는 ( ["("]
4. ) 괄호가 닫혔다! 열린 괄호 X []
5. ( 괄호가 열림 ["("]
6. ) 괄호가 닫힘. 열린 괄호 X -> 올바른 괄호 쌍. []
바로 직전에 조회한 괄호를 저장 -> Stack 자료구조 최적
'''

def is_correct_parenthesis(string):
    stack = []

    for i in range(len(string)):
        if string[i] == "(":
            stack.append(i) # 어떤 값이 들어가도 상관 X (저장 여부 확인
        elif string[i] == ")":
            if len(stack) == 0:
                return False
            else:
                stack.pop()

    if len(stack) != 0:
        return False
    else:
        return True

    # n = len(string)
    # count_01 = 0
    # count_02 = 0
    # if string[0] != '(':
    #     return False
    #
    # for i in range(n):
    #     if string[i] == '(':
    #         count_01 += 1
    #     else:
    #         count_02 += 1
    #
    #     if count_02 > count_01:
    #         return False
    #
    # if count_01 != count_02:
    #     return False
    #
    #
    # return True

print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!
