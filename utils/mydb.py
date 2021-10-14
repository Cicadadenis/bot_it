import sqlite3


def connect():
    conn = sqlite3.connect("cicada.db")

    cursor = conn.cursor()

    return conn, cursor



conn, cursor = connect()


def create_tables():
    try:
        cursor.execute(f'CREATE TABLE users (user_id TEXT, first_name TEXT, username TEXT, balance DECIMAL(10, 2), who_invite TEXT, date TEXT, terms_of_use TEXT)')
        conn.commit()
    except:
        pass

    try:
        cursor.execute(f'CREATE TABLE check_payment (user_id TEXT, code TEXT, referral_code TEXT)')
        conn.commit()
    except:
        pass

    try:
        cursor.execute(f'CREATE TABLE sending (type TEXT, text TEXT, photo TEXT, date TEXT)')
        conn.commit()
    except:
        pass
    
    try:
        cursor.execute(f'CREATE TABLE list (type TEXT, text TEXT, photo TEXT, date TEXT)')
        conn.commit()
    except:
        pass
    
    try:
        cursor.execute(f'CREATE TABLE btc_list (user_id TEXT, code TEXT)')
        conn.commit()
    except:
        pass

    try:
        cursor.execute(f'CREATE TABLE payouts (user_id TEXT, sum TEXT, btc_check TEXT)')
        conn.commit()
    except:
        pass

    try:
        cursor.execute(f'CREATE TABLE payouts_step_0 (user_id TEXT, code TEXT, time TEXT)')
        conn.commit()
    except:
        pass

    try:
        cursor.execute(f'CREATE TABLE buttons (name TEXT, info TEXT, photo TEXT)')
        conn.commit()
    except:
        pass

    try:
        cursor.execute(f'CREATE TABLE deposit_logs (user_id TEXT, type TEXT, sum DECIMAL(10, 2), date TEXT)')
        conn.commit()
    except:
        pass

    try:
        cursor.execute(f'CREATE TABLE stats (user_id TEXT, money TEXT, ref_amount INT, ref_profit DECIMAL(10, 2))')
        conn.commit()
    except:
        pass

    try:
        cursor.execute(f'CREATE TABLE numbers (code TEXT, name TEXT, country1 TEXT, country2 TEXT, country3 TEXT, country4 TEXT, country5 TEXT, country6 TEXT)')
        conn.commit()
    except:
        pass

    try:
        cursor.execute(f'CREATE TABLE wait_list_number (user_id TEXT, operation_ID TEXT, number TEXT, number_code TEXT, country TEXT, status TEXT, purchase_time DOUBLE, price DECIMAL(10, 2))')
        conn.commit()
    except:
        pass

    try:
        cursor.execute(f'CREATE TABLE ref_log (user_id TEXT, all_profit DECIMAL(10, 2))')
        conn.commit()
    except:
        pass

    try:
        cursor.execute(f'CREATE TABLE message_list (msg TEXT)')
        conn.commit()
    except:
        pass

    try:
        cursor.execute(f'CREATE TABLE number_logs (user_id TEXT, service TEXT, operation_id TEXT, number TEXT, status TEXT, price TEXT, date Text)')
        conn.commit()
    except:
        pass


create_tables()
