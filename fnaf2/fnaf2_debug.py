import keyboard
import time
import pyautogui as pag
from PIL import Image, ImageDraw
import cv2
import numpy as np
import screeninfo
import asyncio


# Configurações da tela
screen_id = 0
screen = screeninfo.get_monitors()[screen_id]

window_name = 'Live'
cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
cv2.moveWindow(window_name, screen.x - 1, screen.y - 1)
cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN,
                      cv2.WINDOW_FULLSCREEN)


def locate_on_screen(image, confidence=0.6):
    # captura a tela
    screenshot = np.array(pag.screenshot())
    # converte a imagem para escala de cinza
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    
    # carrega a imagem de busca
    template = cv2.imread(image, 0)

    # realiza a correspondência de modelo na imagem
    res = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
    
    # localiza os locais onde a correspondência excede o limiar de confiança
    loc = np.where(res >= confidence)
    
    # se encontrarmos um match, retornamos as coordenadas do primeiro ponto
    if len(loc[0]) > 0:
        return (loc[1][0], loc[0][0])
    
    # se não encontrarmos um match, retornamos None
    return None

def draw_rectangle(screenshot, location, animatronic):
    if location is not None and animatronic == 'foxy':
        cv2.rectangle(screenshot, (location[0], location[1]), (location[0] + 100, location[1] + 100), (0, 255, 0), 2)
    elif location is not None and animatronic == 'default':
        cv2.rectangle(screenshot, (location[0], location[1]), (location[0] + 200, location[1] + 200), (0, 255, 0), 2)

def check_anims(img, name, confidence=0.6, animatronic='default'):
    screenshot = np.array(pag.screenshot())
    location = locate_on_screen(img, confidence)
    draw_rectangle(screenshot, location, animatronic)
    print(f'{name}: ', location)
    cv2.imshow('Live', screenshot)
    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        exit()
    return location is not None

# o resto do código permanece o mesmo...


def toggleCam():
    pag.moveTo(1348, 930)
    pag.moveTo(1348, 1002, 0.01)
    pag.moveTo(1348, 930, 0.01)

def moveToPuppet():
    pag.moveTo(1779, 657)
    pag.click()

def doMusicBox():
    pag.moveTo(791, 848)
    pag.mouseDown()
    # time.sleep(3)
    # durante 3 segundos, mantem checando a room, se tiver alguem lá, usa a máscara
    for i in range(3):
        if checkRoom():
            useMask()
            time.sleep(7)
            useMask()
            toggleCam()
            time.sleep(0.5)
            doMusicBox()
            break
        time.sleep(0.1)
    pag.mouseUp()

def leftLight():
    pag.moveTo(285, 605)
    time.sleep(0.4)
    pag.mouseDown()
    toy_chica = check_anims('ChicaInTheVent.png', 'toy_chica')
    time.sleep(0.6)
    ballon_boy = check_anims('BallonBoyInTheVent.png', 'ballon_boy')
    pag.mouseUp()
    return toy_chica or ballon_boy

def rightLight():
    pag.moveTo(1622, 605)
    time.sleep(0.4)
    pag.mouseDown()
    toy_bonnie = check_anims('BonnieInTheVent.png', 'toy_bonnie')
    mangle = check_anims('MangleInTheVent.png', 'mangle')
    time.sleep(0.6)
    pag.mouseUp()
    return toy_bonnie or mangle

def useMask():
    pag.moveTo(555, 930)
    pag.moveTo(555, 1005, 0.01)
    pag.moveTo(555, 930, 0.01)

def lightFoxy():
    pag.keyDown('ctrl')
    foxy = check_anims('foxyInTheHallway.png', 'foxy', animatronic='foxy')
    time.sleep(0.5)
    pag.keyUp('ctrl')
    return foxy

def removeFoxy():
    # press ctrl 20 times each 0.1 seconds
    for i in range(20):
        keyboard.press('ctrl')
        time.sleep(0.05)
        keyboard.release('ctrl')
        time.sleep(0.05)

def checkRoom():
    withereds = check_anims('BonnieInTheRoom.png', 'withereds', confidence=0.64)
    if withereds:
        return True
    toy_freedy = check_anims('ToyFreedyInTheRoom.png', 'toy_freedy')
    if toy_freedy:
        return True
    # withered_freedy = check_anims('FreedyInTheRoom.png', 'withered_freedy')
    # if withered_freedy:
    #     return True
    # withered_chica = check_anims('ChicaInTheRoom.png', 'withered_chica')
    # if withered_chica:
    #     return True
    return False


# zona de testes
# while True:
#     if keyboard.is_pressed('p'):
#         toggleCam()
#     if keyboard.is_pressed('o'):
#         moveToPuppet()
#     if keyboard.is_pressed('m'):
#         doMusicBox()
#     if keyboard.is_pressed('l'):
#         leftLight()
#         rightLight()
#     if keyboard.is_pressed('k'):
#         useMask()
#     if keyboard.is_pressed('f'):
#         lightFoxy()
#     if keyboard.is_pressed('r'):
#         removeFoxy()
#     if keyboard.is_pressed('q'):
#         break


# inicializador
inicio = True
camera = False
time.sleep(10)
while keyboard.is_pressed('x') is False:
    toggleCam()
    camera = not camera
    if inicio:
        moveToPuppet()
        inicio = False
    doMusicBox()
    toggleCam()
    camera = not camera
    if checkRoom():
        useMask()
        time.sleep(7)
        useMask()
    if leftLight():
        useMask()
        time.sleep(6.5)
        useMask()
    if rightLight():
        # time.sleep(2)
        useMask()
        time.sleep(6.5)
        useMask()
    if lightFoxy():
        removeFoxy()
    game_over = pag.locateOnScreen('game_over.png', grayscale=True, confidence=0.6)
    if game_over is not None:
        print('game over')
        break

