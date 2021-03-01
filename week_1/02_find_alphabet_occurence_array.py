def find_alphabet_occurrence_array(string):
    alphabet_occurence_array = [0] * 26
    # 이 부분을 채워보세요!

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurence_array[arr_index] += 1

    return alphabet_occurence_array

result = find_alphabet_occurrence_array("hello my name is sparta")

print(result)
