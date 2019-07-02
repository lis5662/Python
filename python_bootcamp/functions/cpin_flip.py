from random import random
# 1
def flip_coin():
    # generate random number 0-1
    r = random()
    if r > 0.5:
        return "Heads"
    else:
        return "Tails"
print(flip_coin())

# 2
def flip_coin():
    if random() > 0.5:
        return "HEADS"
    else:
        return "TAILS"

print(flip_coin())



def generate_evens():
    result = []
    for x in range(1,50):
        if x % 2 == 0:
            result.append(x)
    return result