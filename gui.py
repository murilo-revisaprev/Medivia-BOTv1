import tkinter as tk
from settings import settings, save_settings_to_json, load_settings_from_json
from actions import start_configuration, toggle_leitura, fechar_programa, update_mana_button, update_runa_button, set_update_label_function

def create_gui():
    global root, label, mana_entry, runa_entry
    root = tk.Tk()
    root.title('Runador')
    root.attributes('-toolwindow', 1)

    root.geometry("250x300+0+550")
    root.attributes('-topmost', True)
    root.resizable(False, False)
    root.geometry("+20-30")
    label = tk.Label(root, text="Bem vindo Bunda-Mole.", wraplength=200)
    label.pack(fill="both", expand=True)

    entry_frame = tk.Frame(root)
    entry_frame.pack(pady=10)

    # Campo de entrada para o botão "Runa"
    runa_label = tk.Label(entry_frame, text="Botão Mana:")
    runa_label.grid(row=0, column=0, sticky="e")
    runa_entry = tk.Entry(entry_frame, width=5)
    runa_entry.insert(0, settings['botao_runa'])
    runa_entry.grid(row=0, column=1, padx=5)

    # Campo de entrada para o botão "Mana"
    mana_label = tk.Label(entry_frame, text="Botão Runar:")
    mana_label.grid(row=1, column=0, sticky="e")
    mana_entry = tk.Entry(entry_frame, width=5)
    mana_entry.insert(0, settings['botao_mana'])
    mana_entry.grid(row=1, column=1, padx=5)

    mana_entry.bind("<KeyRelease>", lambda event: update_mana_button(event, mana_entry))
    runa_entry.bind("<KeyRelease>", lambda event: update_runa_button(event, runa_entry))

    button = tk.Button(root, text="Configurar", command=start_configuration)
    button.pack(pady=10)

    root.protocol("WM_DELETE_WINDOW", fechar_programa)

    root.mainloop()

def initialize_gui():
    load_settings_from_json()
    create_gui()

def update_label(text):
    global label
    if label:
        label.config(text=text)

def initialize_gui_and_start_monitoring():
    set_update_label_function(update_label)
    initialize_gui()
