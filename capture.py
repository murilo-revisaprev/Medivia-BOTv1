import pyautogui
import keyboard
from settings import settings

def capturar_cor(x, y):
    screenshot = pyautogui.screenshot()
    return screenshot.getpixel((x, y))

def verificar_cor(cor_alvo, x, y):
    cor = capturar_cor(x, y)
    if cor == tuple(cor_alvo):
        keyboard.send(settings['botao_mana'])
    else:
        keyboard.send(settings['botao_runa'])

def iniciar_leitura(cor_alvo, x, y, condition):
    while condition():
        verificar_cor(cor_alvo, x, y)
