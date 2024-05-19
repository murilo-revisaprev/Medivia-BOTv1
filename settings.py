import json

settings = {
    'cor_alvo': (0, 0, 0),
    'last_captured_location': (0, 0),
    'botao_mana': "f11",
    'botao_runa': "f4",
    'captura_ativa': False,
    'leitura_ativa': False
}

def save_settings_to_json():
    with open("settings.json", "w") as file:
        json.dump(settings, file)

def load_settings_from_json():
    global settings
    try:
        with open("settings.json", "r") as file:
            settings.update(json.load(file))
    except FileNotFoundError:
        pass
