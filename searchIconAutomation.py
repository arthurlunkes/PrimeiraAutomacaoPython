import pyautogui
from time import sleep

icon_location = pyautogui.locateAllOnScreen('icon.png')

sleep(1)

if icon_location != None:
    y = icon_location
    print(f'O ícone foi encontrado nas coordenadas y={y}.')
else:
    print('O ícone não foi encontrado na tela.')