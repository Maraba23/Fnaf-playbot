import cv2
import numpy as np
import keyboard
import time
import pyautogui as pag
from PIL import Image, ImageDraw

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

'''
Posição do mouse: ( 1245 ,  942 )
Posição do mouse: ( 1646 ,  914 )
Posição do mouse: ( 1813 ,  847 )
Posição do mouse: ( 1782 ,  761 )
Posição do mouse: ( 1503 ,  794 )
Posição do mouse: ( 1217 ,  803 )
Posição do mouse: ( 1241 ,  695 )
Posição do mouse: ( 1422 ,  674 )
Posição do mouse: ( 1554 ,  610 )
Posição do mouse: ( 1759 ,  671 )
Posição do mouse: ( 1239 ,  580 )
Posição do mouse: ( 1359 ,  741 )
Posição do mouse: ( 1529 ,  822 )
Posição do mouse: ( 1682 ,  701 )
Posição do mouse: ( 1747 ,  899 )
'''

camera_dict = {
    1 : (1245, 942),
    2 : (1646, 914),
    3 : (1813, 847),
    4 : (1782, 761),
    5 : (1503, 794),
    6 : (1217, 803),
    7 : (1241, 695),
    8 : (1422, 674),
    9 : (1554, 610),
    10 : (1759, 671),
    11 : (1239, 580),
    12 : (1359, 741),
    13 : (1529, 822),
    14 : (1682, 701),
    15 : (1747, 899),
}

# a partir da 11 eh tubulação
correlaçoes_camera_tubulação = {
    10:14,
    9:11,
    8:13,
    7:12,
    2:15,
}

locais = {
    'springtrap_10_1' : locate_on_screen('camera_10_1.png', confidence=0.6),
    'springtrap_10_2' : locate_on_screen('camera_10_2.png', confidence=0.6),
    'springtrap_9_1' : locate_on_screen('camera_9_1.png', confidence=0.6),
    'springtrap_9_2' : locate_on_screen('camera_9_2.png', confidence=0.6),
    'springtrap_8_1' : locate_on_screen('camera_8_1.png', confidence=0.6),
    'springtrap_8_2' : locate_on_screen('camera_8_2.png', confidence=0.6),
    'springtrap_7_1' : locate_on_screen('camera_7_1.png', confidence=0.6),
    'springtrap_7_2' : locate_on_screen('camera_7_2.png', confidence=0.6),
    'springtrap_6_1' : locate_on_screen('camera_6_1.png', confidence=0.6),
    'springtrap_6_2' : locate_on_screen('camera_6_2.png', confidence=0.6),
    'springtrap_5_1' : locate_on_screen('camera_5_1.png', confidence=0.6),
    'springtrap_5_2' : locate_on_screen('camera_5_2.png', confidence=0.6),
    'springtrap_4_1' : locate_on_screen('camera_4_1.png', confidence=0.6),
    'springtrap_4_2' : locate_on_screen('camera_4_2.png', confidence=0.6),
    'springtrap_3_1' : locate_on_screen('camera_3_1.png', confidence=0.6),
    'springtrap_3_2' : locate_on_screen('camera_3_2.png', confidence=0.6),
    'springtrap_2_1' : locate_on_screen('camera_2_1.png', confidence=0.6),
    'springtrap_2_2' : locate_on_screen('camera_2_2.png', confidence=0.6),
    # 'springtrap_1_1' : locate_on_screen('camera_1_1.png', confidence=0.6),
    # 'springtrap_1_2' : locate_on_screen('camera_1_2.png', confidence=0.6),
}



def toggleCam():
    pag.moveTo(1751, 335)
    # click
    pag.mouseDown()
    time.sleep(0.1)
    pag.mouseUp()

def seeAllCameras():
    for i in range(1, 11):
        pag.moveTo(camera_dict[i][0], camera_dict[i][1])
        time.sleep(0.1)
        pag.mouseDown()
        time.sleep(0.1)
        pag.mouseUp()
        if checkSpringtrap(i, 1):
            time.sleep(0.4)
            print(f'springtrap encontrado na camera {i}')
            continue
        else:
            print(f'springtrap não encontrado na camera {i}')
        time.sleep(1)
    changeToVentOrCamera()
    for i in range(11, 16):
        pag.moveTo(camera_dict[i][0], camera_dict[i][1])
        time.sleep(0.1)
        pag.mouseDown()
        time.sleep(0.1)
        pag.mouseUp()
        time.sleep(0.4)
    changeToVentOrCamera()

def checkSpringtrap(i, j):
    if i != 1:
        if locais[f'springtrap_{i}_{j}'] is not None:
            return True
    return False


def changeToVentOrCamera():
    pag.moveTo(1048, 916)
    pag.mouseDown()
    time.sleep(0.1)
    pag.mouseUp()

def moveMouseToCamera():
    pag.moveTo(1751, 335)
    time.sleep(1)

def playAudio():
    pag.moveTo(999, 806)
    pag.mouseDown()
    time.sleep(0.1)
    pag.mouseUp()

def painelDeReparo():
    pag.moveTo(693, 1018)
    pag.mouseDown()
    time.sleep(0.1)
    pag.mouseUp()

def sairDoPainelDeReparo():
    pag.moveTo(483, 902)
    pag.mouseDown()
    time.sleep(0.1)
    pag.mouseUp()

def repararErroAudio():
    pag.moveTo(498, 541)
    pag.mouseDown()
    time.sleep(0.1)
    pag.mouseUp()
    time.sleep(8)

def repararErroCamera():
    pag.moveTo(515, 615)
    pag.mouseDown()
    time.sleep(0.1)
    pag.mouseUp()
    time.sleep(8)

def repararErroVentilacao():
    pag.moveTo(539, 694)
    pag.mouseDown()
    time.sleep(0.1)
    pag.mouseUp()
    time.sleep(8)

# zona de testes
while True:
    if keyboard.is_pressed('p'):
        moveMouseToCamera()
        toggleCam()
        seeAllCameras()
        toggleCam()
        print('-----------------------------------')
    if keyboard.is_pressed('o'):
        moveMouseToCamera()
        toggleCam()
        playAudio()
        toggleCam()
    if keyboard.is_pressed('i'):
        painelDeReparo()
        repararErroAudio()
        repararErroCamera()
        repararErroVentilacao()
        sairDoPainelDeReparo()