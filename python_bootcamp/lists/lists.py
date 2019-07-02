colors = ["purple", "teal", "magenta"]

for color in colors:
    print(color)


numbers = [4, 6, 2, 7, 9, 10]
for num in numbers:
    print(num * num)


colors = ["purple", "teal", "magenta", "crimson", "emerald"]

index = 0
while index < len(colors):
    print(f"{index}: {colors[index]}")
    index += 1



# Create a list called instructors
instructors = []

# Add the following strings to the instructors list
    # "Colt"
    # "Blue"
    # "Lisa"
instructors.extend(["Colt", "Blue", "Lisa"])
# Remove the last value in the list
instructors.pop()
# Remove the first value in the list
instructors.pop(0)
# Add the string "Done" to the beginning of the list
instructors.append("Done") # .insert(0, "Done")
instructors.reverse()
# Run the tests to make sure you've done this correctly!
print(instructors)