import time
import pyautogui

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
def spam():
    for x in range(ti):
        pyautogui.typewrite("@" + answer)
        pyautogui.press('space')
        time.sleep(0.50)
        pyautogui.press('enter')
    pyautogui.typewrite("Thank you for using spambot 9000")
    pyautogui.press('enter')

#this asks for the user name of the spam reseiver
print("Who would you like to spam?\nYou don't need to put the @ symbol")
answer = input()

#this asks how meny times to spam
print("How manny times would you like to spam")
ti = int(input())

countdown()

spam()
