import telebot
import config
import dbworker
import weather

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=["start"])
def cmd_start(message):
    state = dbworker.get_current_state(message.chat.id)
    if state == config.States.S_ENTER_NAME.value:
        bot.send_message(message.chat.id, "Здається, хтось обіцяв відправити своє ім'я, але так і не зробив цього: (Чекаю...")
    elif state == config.States.S_ENTER_AGE.value:
        bot.send_message(message.chat.id, "Здається, хтось обіцяв відправити свій вік, але так і не зробив цього: (Чекаю...")
    elif state == config.States.S_SEND_CITY.value:
        bot.send_message(message.chat.id, "Здається, хтось обіцяв відправити картинку, але так і не зробив цього: (Чекаю...")
    else:
        bot.send_message(message.chat.id, "Вітання! Як я можу до тебе звертатись?")
        dbworker.set_state(message.chat.id, config.States.S_ENTER_NAME.value)


@bot.message_handler(commands=["reset"])
def cmd_reset(message):
    bot.send_message(message.chat.id, "Що ж, почнемо по-новому. Як тебе звати?")
    dbworker.set_state(message.chat.id, config.States.S_ENTER_NAME.value)


@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_ENTER_NAME.value)
def user_entering_name(message):
    bot.send_message(message.chat.id, "Чудове ім'я, запам'ятаю! Тепер вкажи, будь ласка, свій вік.")
    dbworker.set_state(message.chat.id, config.States.S_ENTER_AGE.value)


@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_ENTER_AGE.value)
def user_entering_age(message):
    if not message.text.isdigit():
        bot.send_message(message.chat.id, "Щось не так, спробуй ще раз!")
        return

    if int(message.text) <= 5 or int(message.text) >= 100:
        bot.send_message(message.chat.id, "Якийсь дивний вік. Не вірю! Відповідай чесно.")
        return
    else:
        bot.send_message(message.chat.id, "Колись і мені було стільки років... ех... Втім, не відволікатимемося. "
                                           "Відправ мені якусь фотографію.")
        dbworker.set_state(message.chat.id, config.States.S_SEND_CITY.value)


@bot.message_handler(content_types=["text"],
                     func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_SEND_CITY.value)
def get_text_messages(message):
    city = message
    e = weather.weather(city)
    global text, temp
    if e == 0:
        bot.send_message(message.chat.id, "Ви ввели неправильну назву міста(")
    else:
        try:
            temp = str(weather.temp)
            bot.send_message(message.chat.id, f'Привіт погода {weather.city_} на сім днів:\n{weather.first_day}:\n{weather.first_temperature}\nНа вулиці буде {weather.first_weather}\n'
                                            f'{weather.second_day}:\n{weather.second_temperature}\nНа вулиці буде {weather.second_weather}\n'
                                            f'{weather.third_day}:\n{weather.third_temperature}\nНа вулиці буде {weather.third_weather}\n'
                                            f'{weather.fourth_day}:\n{weather.fourth_temperature}\nНа вулиці буде {weather.fourth_weather}\n'
                                            f'{weather.fifth_day}:\n{weather.fifth_temperature}\nНа вулиці буде {weather.fifth_weather}\n')
        except Exception as ex:
            bot.send_message(message.chat.id, "Ви ввели неправильну назву міста(")
            print(1)
            print(ex)
        text = 0

    dbworker.set_state(message.chat.id, config.States.S_START.value)


if __name__ == "__main__":
    bot.infinity_polling()


