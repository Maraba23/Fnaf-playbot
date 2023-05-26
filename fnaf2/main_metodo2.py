import cv2
import numpy as np
import keyboard
import time
import pyautogui as pag
from PIL import Image, ImageDraw

orb = cv2.ORB_create()
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

def locate_on_screen(image, dist_threshold=30):
    # captura a tela
    screenshot = np.array(pag.screenshot())
    # converte a imagem para escala de cinza
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    
    # carrega a imagem de busca
    template = cv2.imread(image, 0)
    
    # calcula os pontos-chave e descritores para ambos a captura de tela e a imagem do template
    kp_screenshot, des_screenshot = orb.detectAndCompute(screenshot_gray, None)
    kp_template, des_template = orb.detectAndCompute(template, None)

    # realiza a correspondência dos descritores
    matches = bf.match(des_template, des_screenshot)

    # ordena os matches pela distância
    matches = sorted(matches, key = lambda x: x.distance)

    # se encontrarmos um match e a distância for abaixo do limiar, retornamos as coordenadas do primeiro ponto
    if len(matches) > 0 and matches[0].distance < dist_threshold:
        return kp_screenshot[matches[0].trainIdx].pt

    # se não encontrarmos um match, retornamos None
    return None


def toggleCam():
    pag.moveTo(1348, 930)
    pag.moveTo(1348, 1002, 0.1)
    pag.moveTo(1348, 930, 0.1)

def moveToPuppet():
    pag.moveTo(1779, 657)
    pag.click()

def doMusicBox():
    pag.moveTo(791, 848)
    pag.mouseDown()
    time.sleep(3)
    pag.mouseUp()

def leftLight():
    pag.moveTo(285, 605)
    time.sleep(0.4)
    pag.mouseDown()
    toy_chica = locate_on_screen('ChicaInTheVent.png', dist_threshold=10)
    time.sleep(1)
    print('toy_chica: ', toy_chica)
    ballon_boy = locate_on_screen('BallonBoyInTheVent.png', dist_threshold=10)
    print('ballon_boy', ballon_boy)
    # time.sleep(1)
    pag.mouseUp()
    return toy_chica is not None or ballon_boy is not None

def rightLight():
    pag.moveTo(1622, 605)
    time.sleep(0.4)
    pag.mouseDown()
    toy_bonnie = locate_on_screen('BonnieInTheVent.png', dist_threshold=10)
    print('toy_bonnie: ', toy_bonnie)
    mangle = locate_on_screen('MangleInTheVent.png', dist_threshold=10)
    print('mangle: ', mangle)
    time.sleep(0.6)
    pag.mouseUp()
    return toy_bonnie is not None or mangle is not None

def useMask():
    pag.moveTo(555, 930)
    pag.moveTo(555, 1005, 0.1)
    pag.moveTo(555, 930, 0.1)

def lightFoxy():
    pag.keyDown('ctrl')
    foxy = locate_on_screen('foxyInTheHallway.png', dist_threshold=280)
    time.sleep(0.5)
    pag.keyUp('ctrl')
    print('foxy: ', foxy)
    return foxy is not None

def removeFoxy():
    # press ctrl 20 times each 0.1 seconds
    for i in range(20):
        keyboard.press('ctrl')
        time.sleep(0.01)
        keyboard.release('ctrl')
        time.sleep(0.01)

def checkRoom():
    toy_freedy = locate_on_screen('ToyFreedyInTheRoom.png', dist_threshold=10)
    withered_freedy = locate_on_screen('FreedyInTheRoom.png', dist_threshold=10)
    withered_bonnie = locate_on_screen('BonnieInTheRoom.png', dist_threshold=10)
    withered_chica = locate_on_screen('ChicaInTheRoom.png', dist_threshold=10)
    print('toy_freedy: ', toy_freedy)
    print('withered_freedy: ', withered_freedy)
    print('withered_bonnie: ', withered_bonnie)
    print('withered_chica: ', withered_chica)
    # se qualquer um dos 4 estiver na sala retorna True
    return toy_freedy is not None or withered_freedy is not None or withered_bonnie is not None or withered_chica is not None

# inicializador
inicio = True
time.sleep(10)
while keyboard.is_pressed('x') is False:
    toggleCam()
    if inicio:
        moveToPuppet()
        inicio = False
    doMusicBox()
    toggleCam()
    if checkRoom():
        useMask()
        time.sleep(7)
        useMask()
    if leftLight():
        useMask()
        time.sleep(6)
        useMask()
    if rightLight():
        useMask()
        time.sleep(6)
        useMask()
    if lightFoxy():
        removeFoxy()

    game_over = locate_on_screen('game_over.png')
    if game_over is not None:
        print('game over')
        break
