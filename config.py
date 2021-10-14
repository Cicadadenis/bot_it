# - *- coding: utf- 8 - *-
import configparser

config = configparser.ConfigParser()
config.read("settings.ini")
BOT_TOKEN = config["settings"]["token"]
adm = config["settings"]["admin_id"]
sms_api = config['settings']['sms']

if "," in adm:
    adm = adm.split(",")
else:
    if len(adm) >= 1:
        adm = [adm]
    else:
        adm = []
        print("***** Вы не указали админ ID *****")

bot_version = "2.9"
bot_description = f"<b>♻ Bot создал Cicada3301</b>\n" \
                  f"<b>⚜ Bot Version:</b> <code>{bot_version}</code>\n" \
                  f"<b>🔗Для выдачи доступов на сутки</b>\n"\
                  f"<b>🎫В случае их нехватки писать ▶️:</b> <a href='https://t.me/satanasat'><b>Cicada</b></a>"