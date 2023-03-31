import telebot
import config
import dbworker

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=["start"])
def cmd_start(message):
    state = dbworker.get_current_state(message.chat.id)
    if state == config.States.S_ENTER_NAME.value:
        bot.send_message(message.chat.id,"Привіт як тебе звати?")
    elif state == config.States.S_ENTER_CITY.value:
        bot.send_message(message.chat.id, "Укажіть своє місто")
    elif state == config.States.S_SEND_WEATHER_DAY.value:
        bot.send_message(message.chat.id, "Укажіть скільки потрібно вам днів погоди")



@bot.message_handler(commands=["reset"])
def cmd_reset(message):
    bot.send_message(message.chat.id, "Що ж, почнемо по-новому. Як тебе звати?")
    dbworker.set_state(message.chat.id, config.States.S_ENTER_NAME.value)


@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_ENTER_NAME.value)
def user_entering_name(message):
    bot.send_message(message.chat.id, "Тепер вкажіть своє місто")
    dbworker.set_state(message.chat.id, config.States.S_ENTER_CITY.value)


@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_ENTER_CITY.value)
def user_entering_age(message):
    bot.send_message(message.chat.id, "На скільки днів вам потрібна погода")
    dbworker.set_state(message.chat.id, config.States.S_SEND_WEATHER_DAY.value)


if __name__ == "__main__":
    bot.infinity_polling()


