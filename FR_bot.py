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

print("4 sec till start")
sleep(1)
print("3 sec till start")
sleep(1)
print("2 sec till start")
sleep(1)
print("1 sec till start")


while True:
        pyautogui.press('enter')
        pyautogui.typewrite("/f " + ign)
        pyautogui.press('enter')
        print("Friend request sent to " + ign)
        sleep(60)
        print("1 min down")
        sleep(60)
        print("2 min down")
        sleep(60)
        print("3 min down")
        sleep(60)
        print("4 min down")
        sleep(60)
