from gui import initialize_gui
from input_monitor import start_key_and_mouse_monitoring
from settings import load_settings_from_json

def main():
    load_settings_from_json()
    initialize_gui()
    start_key_and_mouse_monitoring()

if __name__ == "__main__":
    main()
