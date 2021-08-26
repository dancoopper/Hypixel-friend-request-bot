import pyautogui
from time import sleep


ign = input("what is the ign: ")

conferm = input(ign + " is that right? ")

anser = ["yes", "Yes", "YES"]

if conferm == anser:
    print(5)
    sleep(1)
    print(4)
    sleep(1)
    print(3)
    sleep(1)
    print(2)
    sleep(1)
    print(1)
    pass
else:
    ign = input("what is the right ign: ")

sleep(4)


while True:
        pyautogui.press('enter')
        pyautogui.typewrite("/f " + ign)
        pyautogui.press('enter')
        print("Friend request sent to " + ign)
        sleep(4)
        print("one min down")
        sleep(4)
        print("two min down")
        sleep(4)
        print("thee min down")
        sleep(4)
        print("4 min down")
        sleep(4)
