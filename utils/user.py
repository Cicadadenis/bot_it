from utils.mydb import *

import config


class User():
    
    def __init__(self, user_id):
        conn, cursor = connect()

        cursor.execute(f'SELECT * FROM users WHERE user_id = "{user_id}"')
        user = cursor.fetchone()

        self.user_id = user[0]
        self.first_name = user[1]
        self.username = user[2]
        self.balance = user[3]
        self.who_invite = user[4]
        self.date = user[5]
        self.terms_of_use = user[6]

        self.ref_amount = 0
        self.ref_profit = 0

    def update_balance(self, value):
        conn, cursor = connect()
        
        cursor.execute(f'UPDATE users SET balance = {float(self.balance) + float(value)} WHERE user_id = "{self.user_id}"')
        conn.commit()

        return True

    def top_ref_invite(self):
        conn, cursor = connect()

        cursor.execute(f'SELECT * FROM users WHERE who_invite = {self.user_id}')
        check = cursor.fetchall()

        return len(check)

    def give_ref_reward(self, money):
        conn, cursor = connect()

        if self.who_invite != '0':
            User(self.who_invite).update_balance(float(float(money) / 100 * float(config.config("ref_percent"))))

            cursor.execute(f'SELECT * FROM stats WHERE user_id = "{self.who_invite}"')
            user = cursor.fetchall()

            if len(user) == 0:
                cursor.execute(
                    f'INSERT INTO stats VALUES("{self.who_invite}", "0", "1", "0")')
                conn.commit()
            else:
                if user[0][2] is None or user[0][3] is None:
                    cursor.execute(f'UPDATE stats SET ref_profit = 0 WHERE user_id = "{self.who_invite}"')
                    conn.commit()

                    cursor.execute(f'UPDATE stats SET ref_amount = 0 WHERE user_id = "{self.who_invite}"')
                    conn.commit()

                    cursor.execute(f'SELECT * FROM stats WHERE user_id = "{self.who_invite}"')
                    user = cursor.fetchall()

                cursor.execute(
                    f'UPDATE stats SET ref_profit = {float(user[0][3]) + float(float(money) / 100 * float(config.config("ref_percent")))} WHERE user_id = "{self.who_invite}"')
                conn.commit()

    def get_stats(self):
        try:
            cursor.execute(f'SELECT * FROM stats WHERE user_id = "{self.user_id}"')
            user = cursor.fetchone()

            self.ref_amount = user[2]
            self.ref_profit = user[3]
        except TypeError:
            cursor.execute(f'INSERT INTO stats VALUES("{self.user_id}", "0", "0", "0")')
            conn.commit()

            self.ref_amount = 0
            self.ref_profit = 0



