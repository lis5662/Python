#with open("haiku.txt", "a") as file:
#    file.seek(0)
#    file.write(":)\n")

with open("haiku.txt", "r+") as file:
    file.write(":)")
    file.seek(10)
    file.write(":(")