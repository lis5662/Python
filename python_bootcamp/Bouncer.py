# ask for age
age = input("How old are you: ")
if age:
    age = int(age)
    if age >= 21:
        # 21 + drink, nirmal entry
        print("You are good to enter and can drink!")
    elif age >= 18:
        # 18-21 wristband
        print("You can enter, but need a wristband!")
    else:
        # too young, sorry
        print("You can't come in, little one! :(")
else:
    print("Please enter an age!")

