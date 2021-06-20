import pyautogui, time

a = input("Digite a palavra:\n")
b = int(input("Quantas vezes devo spammar?:\n"))

time.sleep(3)

while b > 0:
    b = b - 1
    pyautogui.typewrite(a)
    pyautogui.press('enter')

else:
    print("O Spawn acabou")
    time.sleep(2)