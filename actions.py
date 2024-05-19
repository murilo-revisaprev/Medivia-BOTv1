from pynput import mouse
from settings import settings, save_settings_to_json
from capture import capturar_cor, iniciar_leitura
import threading
import pyautogui

listener = None
update_label_function = None

def set_update_label_function(func):
    global update_label_function
    update_label_function = func

def start_configuration():
    global listener
    settings['captura_ativa'] = True
    if update_label_function:
        update_label_function("Modo de configuração ativado\nClique em um ponto na barra de mana")
    listener = mouse.Listener(on_click=on_click)
    listener.start()

def on_click(x, y, button, pressed):
    if pressed:
        if update_label_function:
            update_label_function('Configuração concluída')
        settings['cor_alvo'] = capturar_cor(x, y)
        settings['last_captured_location'] = (x, y)
        save_settings_to_json()
        settings['captura_ativa'] = False
        listener.stop()

def toggle_leitura():
    if settings['leitura_ativa']:
        settings['leitura_ativa'] = False
        if update_label_function:
            update_label_function('Parou de Runar')
    else:
        settings['leitura_ativa'] = True
        threading.Thread(target=iniciar_leitura, args=(
            settings['cor_alvo'], 
            settings['last_captured_location'][0], 
            settings['last_captured_location'][1], 
            lambda: settings['leitura_ativa'] and settings['captura_ativa']
        )).start()
        if update_label_function:
            update_label_function('Runando')

def fechar_programa():
    global listener
    settings['captura_ativa'] = False
    if listener:
        listener.stop()
    from gui import root
    root.destroy()

def update_mana_button(event, entry):
    settings['botao_mana'] = entry.get()
    save_settings_to_json()

def update_runa_button(event, entry):
    settings['botao_runa'] = entry.get()
    save_settings_to_json()

def drop_on_ground(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.mouseDown()
    screen_width, screen_height = pyautogui.size()
    pyautogui.moveTo(screen_width // 2, screen_height // 2)
    pyautogui.mouseUp()

def loot_it(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.mouseDown()
    target_x, target_y = 100, 200  # Defina o local alvo aqui
    pyautogui.moveTo(target_x, target_y)
    pyautogui.mouseUp()
