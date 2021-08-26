import pyautogui
from time import sleep


print('''
 _   _             _          _  ______    _                _  ______                           _   
| | | |           (_)        | | |  ___|  (_)              | | | ___ \                         | |  
| |_| |_   _ _ __  ___  _____| | | |_ _ __ _  ___ _ __   __| | | |_/ /___  __ _ _   _  ___  ___| |_ 
|  _  | | | | '_ \| \ \/ / _ \ | |  _| '__| |/ _ \ '_ \ / _` | |    // _ \/ _` | | | |/ _ \/ __| __|
| | | | |_| | |_) | |>  <  __/ | | | | |  | |  __/ | | | (_| | | |\ \  __/ (_| | |_| |  __/\__ \ |_ 
\_| |_/\__, | .__/|_/_/\_\___|_| \_| |_|  |_|\___|_| |_|\__,_| \_| \_\___|\__, |\__,_|\___||___/\__|
        __/ | |                                                              | |                    
       |___/|_|                                                              |_|                    
''')
print("this is the first version")
ign = input("what is the ign: ")
print("sending in...")
print("5")
sleep(1)
print("4")
sleep(1)
print("3")
sleep(1)
print("2")
sleep(1)
print("1")


while True:
        pyautogui.press('enter')
        pyautogui.typewrite("/f " + ign)
        pyautogui.press('enter')
        print("Friend request sent to " + ign)
        sleep(60)
        print("4 min till next request")
        sleep(60)
        print("3 min till next request")
        sleep(60)
        print("2 min till next request")
        sleep(60)
        print("1 min till next request")
        sleep(60)
