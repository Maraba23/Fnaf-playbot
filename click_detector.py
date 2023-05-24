import keyboard
import pyautogui

while True:
    if keyboard.is_pressed('p'):  # se a tecla 'p' for pressionada.
        pos = pyautogui.position()  # obtém a posição do cursor.
        print('Posição do mouse: (', pos.x, ', ', pos.y, ')')
        while keyboard.is_pressed('p'):  # Espera 'p' ser solto
            pass
