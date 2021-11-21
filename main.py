import time, pyautogui

# Countdown Function. Used for giving a countdown before starting the spam.
def countdown():
    print("you have 5 seconds to click where you want it to spam")
    time.sleep(0.8)
    print("5")
    time.sleep(1)
    print("4")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)

# this repeats the spam code
#DO NOT TOUCH THE ANCIENT CODE
def spam(ti, si, answer, message):
    for x in range(int(ti)):
        pyautogui.typewrite(f'@{answer} {message}')
        pyautogui.press('space')
        time.sleep(float(si))
        pyautogui.press('enter')
    pyautogui.typewrite("Thank you for using spambot 9000")

def main():
    #this asks for the user name of the spam reseiver
    answer = input("Who would you like to spam?\n(You don't need the @ symbol)\n")

    message = input("Please imput a message to go with the spam\nif you leave this blank it will do nothing\n")
    if message is "":
        print("Ok nothing will be sent with this spam\n")
    else:
        print("ok this will be sent with the spam\n")


    # This asks how meny times to spam
    ti = input("How many times would you like to spam?\n")
    # Catches errors
    try:
        int(ti)
    except ValueError:
        print("That is not a valid number.")
        main()

    si = input("Please choose a delay between messages. (Default: 0.75 seconds)\n")
    # Catches errors
    try:
        float(si)
    except ValueError:
        print("Defaulting to 0.75 seconds")
        si = 0.75

    # Runs the countdown
    countdown()

    # Runs the spam function (Parameters needed since this code is in a function).
    spam(ti, si, answer, message)

main()