def is_odd_number(num):
    if num % 2 != 0:
        return True
    return False

print(is_odd_number(4))
print(is_odd_number(9))



def count_dollar_signs(word):
    count = 0
    for char in word:
        if char == '$':
            count += 2
        return count

print(count_dollar_signs("$"))