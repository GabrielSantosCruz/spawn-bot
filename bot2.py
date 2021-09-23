import pyautogui, time
print('''  
  ####    #####      ##     ##   ##  ##  ##            #####     ####    ######
 ##  ##   ##  ##    ####    ##   ##  ### ##            ##  ##   ##  ##     ##
 ##       ##  ##   ##  ##   ##   ##  ######            ##  ##   ##  ##     ##
  ####    #####    ######   ## # ##  ######            #####    ##  ##     ##
     ##   ##       ##  ##   #######  ## ###            ##  ##   ##  ##     ##
 ##  ##   ##       ##  ##   ### ###  ##  ##            ##  ##   ##  ##     ##
  ####    ##       ##  ##   ##   ##  ##  ##            #####     ####      ##''')

a = input("Digite a palavra:\n")
b = int(input("Quantas vezes devo spammar?:\n"))

time.sleep(3)

for i in range(b):

    pyautogui.typewrite(a)
    pyautogui.press('enter')

else:
    print("O Spawn acabou")
    time.sleep(2)