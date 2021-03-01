input_str = "acccdeee"


def summarize_string(target_str):
# 이 부분을 채워보세요!
    n = len(target_str)
    count = 1
    result_str = ''
    for i in range(n-1):
        if target_str[i] == target_str[i+1]:
            count += 1
        else:
            result_str += target_str[i] + str(count) + '/'
            count = 1

    result_str += target_str[n-1] + str(count)
    return result_str

print(summarize_string(input_str))

'''
def summarize_string(target_string):
    # 이 부분을 채워보세요!
    n = len(target_string)
    count = 0
    result_str = ''

    for i in range(n - 1):
        if target_string[i] == target_string[i + 1]:
            count += 1
        else:
            result_str += target_string[i] + str(count + 1) + '/'
            count = 0

    result_str += target_string[n - 1] + str(count + 1)

    return result_str

input_str = "acccdeee"

print(summarize_string(input_str))
'''