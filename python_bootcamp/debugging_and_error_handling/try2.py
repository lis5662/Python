# try:
# except:
# else:
# finally:


while True:
    try:
        num = int(input("please enter a number: "))
    except ValueError:
        print("That's not a number!")
    else:
        print("Good job you entered a number!")
        break
    finally:
        print("Runs no matter what!")
print("REST OF GAME LOGIC RUNS!")



# try:
#    num = int(input("please enter a number: "))
# except:
#    print("That's not a number!")
# else:
#    print("I'm in the else!")
# finally:
#    print("Runs no matter what!")