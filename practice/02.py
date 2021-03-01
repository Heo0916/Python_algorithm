
input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    zero_count = 0
    one_count = 0

    if string[0] == '0':
        one_count += 1
    else:
        zero_count += 1
    for i in range(len(string)-1):
        if string[i] != string[i+1]:
            if string[i+1] == 0:
                one_count += 1
            else:
                zero_count += 1





    return min(one_count, zero_count)

result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)
