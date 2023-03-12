import json
import os

from source._storage import data
from source._system import system

def load_ids(path):
    try:
        with open(path, 'r') as id_file:
            try:
                ids = json.loads(id_file.read())['posts']
                return ids
            except:
                return None
    except FileNotFoundError:
        return None

def save_posts(path):
    try:
        with open(path, 'w') as id_file:
            json.dump(data.collected_posts, id_file, indent=4)
        print(f' {system.DEFAULT}[{system.GREEN}+{system.DEFAULT}] saved posts to file.{system.FLUSH}')
    except:
        print(f' {system.DEFAULT}[{system.RED}!{system.DEFAULT}] failed to save posts to file.{system.FLUSH}')
        return
    
def load_config():
    try:
        with open('./config/config.json', 'r') as config:
            config = json.loads(config.read())
       
        data.config['discord']['webhook_url'] = config['discord']['webhook_url']
        data.config['discord']['webhook_username'] = config['discord']['webhook_username']
        data.config['app']['refresh_time'] = config['app']['refresh_time']
        
        print(f' {system.DEFAULT}[{system.GREEN}+{system.DEFAULT}] config loaded.{system.FLUSH}\n')
    except:
        print(f' {system.DEFAULT}[{system.RED}!{system.DEFAULT}] failed to read configuration file. using default settings{system.FLUSH}')
        write_config()
        return

def write_config():
    try:
        if not os.path.exists('./config'):
            os.mkdir('./config')
        
        with open('./config/config.json', 'w') as config:
            json.dump(data.config, config, indent=4)
        print(f' {system.DEFAULT}[{system.GREEN}+{system.DEFAULT}] default configuration saved.{system.FLUSH}\n')
    except:
        print(f' {system.DEFAULT}[{system.RED}!{system.DEFAULT}] failed to save default settings to configuration File.{system.FLUSH}\n')
        return
