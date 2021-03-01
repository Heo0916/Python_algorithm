
finding_target = 3
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

def is_exist_target_number_binary(target, numbers):
    numbers.sort()
    min_num = 0
    max_num = len(numbers)-1
    find_number = (min_num + max_num) // 2

    while min_num <= max_num:
        if numbers[find_number] == target:
            return True
        elif numbers[find_number] < target:
            min_num = find_number + 1
        else:
            max_num = find_number - 1
        find_number = (min_num + max_num) // 2

    return False

result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)
