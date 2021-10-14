import configparser
import os
import time
import os, sys, time, socket, random, requests

def restart_program():
	python = sys.executable
	os.execl(python, python, * sys.argv)
	curdir = os.getcwd()


path = 'settings.ini'

def create_config():

    config = configparser.ConfigParser()
    config.add_section("settings"),
    config.set("settings", 'token', ''),
    config.set("settings", 'admin_id', ''),
    config.set("settings", 'sms', ''),
    config.set("settings", 'ra', '150'),
    config.set("settings", 'gor', '80'),
    config.set("settings", 'ver', '160'),
    config.set("settings", 'r', 'lime')
    
    
    
    with open(path, "w") as config_file:
        config.write(config_file)
        os.system('python3 satana.py')

def check_config_file():
    if not os.path.exists(path):
        create_config()
        
        print('Config created')
        time.sleep(3)
        exit(0)


def config(what):
    
    config = configparser.ConfigParser()
    config.read(path)

    value = config.get("settings", what)

    return value

def send():
    doc = open('config.cfg', 'rb')

    return doc


def edit_config(setting, value):
    config = configparser.ConfigParser()
    config.read(path)

    config.set("settings", setting, value)

    with open(path, "w") as config_file:
        config.write(config_file)



check_config_file()