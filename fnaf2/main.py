import keyboard
import time
import pyautogui as pag

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
    toy_chica = pag.locateOnScreen('ChicaInTheVent.png', grayscale=True, confidence=0.6)
    time.sleep(0.5)
    print('toy_chica: ', toy_chica)
    ballon_boy = pag.locateOnScreen('BallonBoyInTheVent.png', grayscale=True, confidence=0.6)
    print('ballon_boy', ballon_boy)
    time.sleep(0.5)
    pag.mouseUp()
    return toy_chica is not None or ballon_boy is not None

def rightLight():
    pag.moveTo(1622, 605)
    time.sleep(0.4)
    pag.mouseDown()
    toy_bonnie = pag.locateOnScreen('BonnieInTheVent.png', grayscale=True, confidence=0.6)
    print('toy_bonnie: ', toy_bonnie)
    mangle = pag.locateOnScreen('MangleInTheVent.png', grayscale=True, confidence=0.6)
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
    foxy = pag.locateOnScreen('foxyInTheHallway.png', grayscale=True, confidence=0.6)
    time.sleep(0.5)
    pag.keyUp('ctrl')
    print('foxy: ', foxy)
    return foxy is not None

def removeFoxy():
    # press ctrl 20 times each 0.1 seconds
    for i in range(20):
        keyboard.press('ctrl')
        time.sleep(0.1)
        keyboard.release('ctrl')
        time.sleep(0.1)

def checkRoom():
    toy_freedy = pag.locateOnScreen('ToyFreedyInTheRoom.png', grayscale=True, confidence=0.6)
    withered_freedy = pag.locateOnScreen('FreedyInTheRoom.png', grayscale=True, confidence=0.6)
    withered_bonnie = pag.locateOnScreen('BonnieInTheRoom.png', grayscale=True, confidence=0.8)
    withered_chica = pag.locateOnScreen('ChicaInTheRoom.png', grayscale=True, confidence=0.6)
    print('toy_freedy: ', toy_freedy)
    print('withered_freedy: ', withered_freedy)
    print('withered_bonnie: ', withered_bonnie)
    print('withered_chica: ', withered_chica)
    # se qualquer um dos 4 estiver na sala retorna True
    return toy_freedy is not None or withered_freedy is not None or withered_bonnie is not None or withered_chica is not None


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
        time.sleep(6)
        useMask()
    if lightFoxy():
        removeFoxy()
    if leftLight():
        useMask()
        time.sleep(6)
        useMask()
    if rightLight():
        useMask()
        time.sleep(6)
        useMask()
