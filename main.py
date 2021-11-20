import time, pyautogui

#this is the countdown to get to the window you want before typing
def countdown():
    print("you have 5 seconds to click where you want it to spam")
    time.sleep(1)
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
#DO NOT TUCH THE ANCIENT CODE
def spam():
    for x in range(int(ti)):
        pyautogui.typewrite("@" + answer)
        pyautogui.press('space')
        time.sleep(int(si))
        pyautogui.press('enter')
    pyautogui.typewrite("Thank you for using spambot 9000")

#this asks for the user name of the spam reseiver
answer = input("Who would you like to spam?\nYou don't need to put the @ symbol\n")

#this asks how meny times to spam
ti = input("How manny times would you like to spam\n")

si = input("please chose how much delay you would like the program to use\nit will default to 0.75 if nothing is typed\n")
if si is None:
    si = 0.75

countdown()

spam()