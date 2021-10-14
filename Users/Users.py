import time
import sqlite3
import re


class get_users:
    user_list = {}
    #admins_list = []
    active_users = {}

    def __init__(self):
        connection = sqlite3.connect('Users.db')
        cursor = connection.cursor()
        try:
            u = cursor.execute('select * from chat_id').fetchall()
        except sqlite3.OperationalError as y:
            u = []
        #try:
        #    a = cursor.execute('select * from Admins').fetchall()
        #except sqlite3.OperationalError as y:
        #    a = []
        self.user_list = [i[0] for i in u]
        #self.admins_list = [i[0] for i in a]
        connection.close()

    def update(self):
        self.__init__()

    def ismember(self, uid):
        return uid in  self.user_list

class SuperUser:
    def __init__(self, bot, message):
        self.bot = bot
        self.user_id = message.from_user.id
        self.message = message

class Admin(SuperUser):
    def __init__(self, bot, message):
        super().__init__(bot, message)
        get_users().active_users[self.user_id] = self.user_id

        if not (self.user_id in get_users().admins_list):
            txt = "Для завершения регистрации введите свои данные в следующем формате:\n" \
                  "<Фамилия> <Имя> <Отчество>, <Номер телефона>, <кратко о том, кто вы>\n" \
                  "Пример:\n Пупкин Василий Игоревич, 8-800-555-3535, Физик-ядерщик, вожатый 6 отряда"
            resp = self.bot.send_message(self.user_id, txt)
            self.bot.register_next_step_handler(resp, self.hello)
        else:
            try:
                self.command = self.list_commands[message.text.split(" ")[0]]
                self.command(self, message=message.text)
            except KeyError as a:
                self.bot.send_message(self.user_id, "Неверная команда")
                self.bot.send_message(self.user_id, "Введите /help для получения списка с описанием команд")
                self.de()

    def hello(self, message):

        connection = sqlite3.connect('Users.db')
        cursor = connection.cursor()
        try:
            txt = [i.strip() for i in message.text.split(",", maxsplit=2)]
            txt[:1] = txt[0].split(" ")
            txt = [self.user_id] + txt
            try:
                cursor.execute("""CREATE TABLE Users (
                                            'chat_id'	TEXT NOT NULL,
                                            'first_name'	TEXT NOT NULL,);""")
            except sqlite3.OperationalError:
                pass
            cursor.execute("insert into Users values (?, ?)", txt)

            self.bot.send_message(self.user_id, "Вы зарегистрированы как администратор")
            self.bot.send_message(self.user_id, "Введите команду /help для получения справки о функциях бота")
        except:
            self.bot.send_message(self.user_id, "Неверный формат ввода")
        connection.commit()
        get_users().update()
        cursor.close()
        connection.close()
        self.de()