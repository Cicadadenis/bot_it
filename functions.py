import sqlite3
import os
import random
import requests
import json
import datetime
import threading
import traceback
from time import time
from datetime import datetime, date
from sys import exit
from random import choice
start_date = '04.07.2021'
import datetime
import json
import random

import requests

import config

import texts
from utils.mydb import *
from utils.user import User

buy_dict = {}

class Buy:
    def __init__(self, user_id):
        self.user_id = user_id
        self.product_code = None


def first_join(user_id, first_name, username, code):
    conn, cursor = connect()
    
    cursor.execute(f'SELECT * FROM users WHERE user_id = "{user_id}"')
    row = cursor.fetchall()
    who_invite = code[7:]

    if who_invite == '':
        who_invite = 0
    
    if len(row) == 0:
        user = [user_id, first_name, f"@{username}", '0', who_invite, datetime.datetime.now(), 'no']
        sql = f'INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?)'
        cursor.execute(sql, user)
        conn.commit()

        return True, who_invite
        
    return False, 0


def check_in_bd(user_id):
    conn, cursor = connect()
    
    cursor.execute(f'SELECT * FROM users WHERE user_id = "{user_id}"')
    row = cursor.fetchall()

    if len(row) == 0:
        return False
    else:
        return True

def replenish_balance(user_id):
    conn, cursor = connect()
    
    cursor.execute(f'SELECT * FROM check_payment WHERE user_id = "{user_id}"')
    row = cursor.fetchall()
    
    if len(row) > 0:
        code = row[0][1]
    else:
        code = random.randint(1111, 9999)

        cursor.execute(f'INSERT INTO check_payment VALUES ("{user_id}", "{code}", "0")')
        conn.commit()

    msg = texts.replenish_balance.format(
        number=config.config("qiwi_number"),
        code=code,
    )
    url =  f'https://qiwi.com/payment/form/99?extra%5B%27account%27%5D={config.config("qiwi_number")}&amountFraction=0&extra%5B%27comment%27%5D={code}&currency=643&&blocked[0]=account&&blocked[1]=comment'

    markup = menu.payment_menu(url)

    return msg, markup

def check_payment(user_id):
    try:
        conn, cursor = connect()
    
        session = requests.Session()
        session.headers['authorization'] = 'Bearer ' + config.config("qiwi_token")
        parameters = {'rows': '10'}
        h = session.get(
            'https://edge.qiwi.com/payment-history/v1/persons/{}/payments'.format(config.config("qiwi_number")),
            params=parameters)
        req = json.loads(h.text)

        cursor.execute(f'SELECT * FROM check_payment WHERE user_id = {user_id}')
        result = cursor.fetchone()
        comment = result[1]

        for i in range(len(req['data'])):
            if comment in str(req['data'][i]['comment']):
                if str(req['data'][i]['sum']['currency']) == '643':
                    User(user_id).update_balance(req["data"][i]["sum"]["amount"])
                    User(user_id).give_ref_reward(req["data"][i]["sum"]["amount"])

                    cursor.execute(f'DELETE FROM check_payment WHERE user_id = "{user_id}"')
                    conn.commit()

                    rub = req["data"][i]["sum"]["amount"]

                    try:
                        cursor.execute(f'INSERT INTO deposit_logs VALUES ("{user_id}", "qiwi", "{rub}", "{datetime.datetime.now()}")')
                        conn.commit()
                    except:
                        pass

                    return 1, req["data"][i]["sum"]["amount"], req["data"][i]["personId"], req['data'][i]['comment']

                    
    except Exception as e:
        print(e)

    return 0, 0

        
    
