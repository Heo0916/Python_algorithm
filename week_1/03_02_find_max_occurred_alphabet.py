
input = "hello my name is sparta"

def find_max_occurred_alphabet(string):
    alphabet_occurence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurence_array[arr_index] += 1

    max_occurrence = 0
    max_alphabet_index = 0
    for index in range(len(alphabet_occurence_array)):
        # index 0 -> alphabet_occurrence 3
        alphabet_occurence = alphabet_occurence_array[index]

        if alphabet_occurence > max_occurrence:
            max_alphabet_index = index
            max_occurrence = alphabet_occurence

    return chr(max_alphabet_index + ord("a"))
    # a -> 0
    # a -> ord(a) -> 97 - ord(a) = 0
result = find_max_occurred_alphabet(input)
print(result)
