input = "abadabac"

def find_not_repeating_first_character(string):
    alphabet_occurence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurence_array[arr_index] += 1

    not_repeating_character_array = []

    for index in range(len(alphabet_occurence_array)):
        alphabet_occurence = alphabet_occurence_array[index]
        if alphabet_occurence == 1:
            not_repeating_character_array.append(chr(index + ord('a')))



    for char in string:
        if char in not_repeating_character_array:
            return char
    return "-"


result = find_not_repeating_first_character(input)
print(result)
