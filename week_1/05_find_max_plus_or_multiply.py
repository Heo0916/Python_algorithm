
input = [0, 3, 5, 6, 1, 2, 4]

def find_max_plus_or_multiply(array):
    multiply_sum = 0
    for number in array:
        if number <= 1 or multiply_sum <= 1:
            multiply_sum += number
        else:
            multiply_sum *= number
    return  multiply_sum




    '''
    내 풀이
     max = array[0]
     for i in array:
         if max == 0 or i == 1 or i == 0:
             max += i
         else:
             max *= i
     
     return max
    '''
result = find_max_plus_or_multiply(input)
print(result)
