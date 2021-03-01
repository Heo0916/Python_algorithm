#python
input = [3, 5, 6, 1, 2, 4]

Max = 0
def find_max_num(array):
    Max = max(array)
    return Max

result = find_max_num(input)
print(result)

'''
방법 1:
    for num in array:
        for compare_num in array:
            if num < compare_num:
                break
        else:
            return num      
'''
