import os
import json

CONFIG_FILE = os.path.expanduser("~/.deployvault_config.json")

def save_email(email):
    config = {}
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            config = json.load(f)
    
    config['email'] = email
    
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f)

def get_email():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            config = json.load(f)
            return config.get('email')
    return None

def clear_config():
    if os.path.exists(CONFIG_FILE):
        os.remove(CONFIG_FILE)