def calculateTime(keyboard, string):
    key_indices = {char: index for index, char in enumerate(keyboard)}
    total_time = 0
    current_index = 0
    for char in string:
        target_index = key_indices[char]
        time_taken = abs(target_index-current_index)
        total_time += time_taken
        current_index = target_index
    return total_time


print(calculateTime("abcdefghijklmnopqrstuvwxyz", "cba"))
