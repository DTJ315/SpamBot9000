import time, pyautogui
DISCLAIMER_README = "DISCLAIMER: Please only use this for joking around with your friends or sending in spam channels with permmision from the server owner.\nUse of this to send hate speech, illegal content or anything that breaks the discord ToS / ToU is PROHIBITED."


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
        pyautogui.press('enter')
        time.sleep(float(si))
    pyautogui.typewrite("Thank you for using spambot 9000")

def main():
    # Default Delay
    delayDefault = 0.75
    
    # This asks for the user name of the spam receiver
    personInput = input("Who would you like to spam?\n(You don't need the @ symbol)\n")

    messageInput = input("Please imput a message to go with the spam.\nIf you leave this blank it will have no message\n")
    if messageInput == "":
        print("Ok nothing will be sent with this spam\n")
    else:
        print("ok this will be sent with the spam\n")


    # This asks how meny times to spam
    timesInput = input("How many times would you like to spam?\n")
    # Catches errors
    try:
        int(timesInput)
    except ValueError:
        print("That is not a valid number.")
        main()

    delayInput = input(f'Please choose a delay between messages. (Default: {delayDefault} seconds)\n')
    # Catches errors
    try:
        float(delayInput)
    except ValueError:
        print(f'Defaulting to {delayDefault} seconds')
        delayInput = delayDefault

    # Runs the countdown
    countdown()

    # Runs the spam function (Parameters needed since this code is in a function).
    spam(timesInput, delayInput, personInput, messageInput)

main()