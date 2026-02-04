def spy_game(lst):
    string = '007'
    pointer_to_list = 0
    pointer_to_string = 0
    while pointer_to_list < len(lst):
        if lst[pointer_to_list] == int(string[pointer_to_string]):
            pointer_to_string += 1
            if pointer_to_string == len(string):
                return True
        pointer_to_list += 1
    return False

print(spy_game([1, 2, 4, 0, 3, 0, 7])) # True
print(spy_game([1, 2, 5, 0, 3, 1, 7])) # False