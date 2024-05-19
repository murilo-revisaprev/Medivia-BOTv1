from pynput import mouse, keyboard
from actions import toggle_leitura

def on_key_press(key):
    try:
        if key.char == 'esc':
            toggle_leitura()
    except AttributeError:
        pass

def on_click(x, y, button, pressed):
    if pressed:
        if button == mouse.Button.left:            
            print("Botão esquerdo pressionado em ({0}, {1})".format(x, y))
        elif button == mouse.Button.right:
            print("Botão direito pressionado em ({0}, {1})".format(x, y))

def start_key_and_mouse_monitoring():
    with keyboard.Listener(on_press=on_key_press) as key_listener, \
            mouse.Listener(on_click=on_click) as mouse_listener:
        key_listener.join()
        mouse_listener.join()
