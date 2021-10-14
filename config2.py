import configparser
import os
import time

path = 'config2.cfg'

def create_config():

    config = configparser.ConfigParser()
    config.add_section("Settings"),
    config.set("Settings", 'sms', '**cicada3301**'),
    config.set("Settings", 'ra', '50'),
    config.set("Settings", 'gor', '20'),
    config.set("Settings", 'ver', '25'),
    config.set("Settings", 'r', 'lime')
    
    
    
    with open(path, "w") as config_file:
        config.write(config_file)


def check_config_file():
    if not os.path.exists(path):
        create_config()
        
        print('Config created')
        time.sleep(3)
        exit(0)


def config(what):
    
    config = configparser.ConfigParser()
    config.read(path)

    value = config.get("Settings", what)

    return value

def send():
    doc = open('config.cfg', 'rb')

    return doc


def edit_config(setting, value):
    config = configparser.ConfigParser()
    config.read(path)

    config.set("Settings", setting, value)

    with open(path, "w") as config_file:
        config.write(config_file)



check_config_file()