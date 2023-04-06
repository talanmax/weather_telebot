import requests
import telebot
from bs4 import BeautifulSoup as bs
city = ' '
rezz = 0
text = 0
text_old = 0
city_ = 0
answer = 0
bot = telebot.TeleBot("5914199920:AAEpnKjGl3xc6UG7k--3enzscBQOTXVjp0Q")
def weather(city):
    global city_, html, temp, text_old, text, t_max, t_min, first_day, second_day, third_day, fourth_day, fifth_day, sixth_day
    global seventh_day, first_temperature, second_temperature, third_temperature, fourth_temperature, fifth_temperature
    global sixth_temperature, seventh_temperature, first_weather, second_weather, third_weather, fourth_weather, fifth_weather
    global sixth_weather, seventh_weather
    r = requests.get(f'https://ua.sinoptik.ua/погода-{city}')
    html = bs(r.content, 'lxml')
    for el in html.select('#content'):
        days = html.find_all(class_="day-link")
        temperatures = html.find_all(class_="temperature")
        weath = html.find_all(class_ = "weatherIco")
        first_day = days[0].text
        second_day = days[1].text
        third_day = days[2].text
        fourth_day = days[3].text
        fifth_day = days[4].text
        sixth_day = days[5].text
        seventh_day = days[6].text

        first_temperature = temperatures[0].text
        second_temperature = temperatures[1].text
        third_temperature = temperatures[2].text
        fourth_temperature = temperatures[3].text
        fifth_temperature = temperatures[4].text
        sixth_temperature = temperatures[5].text
        seventh_temperature = temperatures[6].text

        weathh = []
        ff=0
        for day_of_weather in weath:
            ad = str(day_of_weather).split("title=")
            ad1 = ad[1].split('\"')
            if ff != 7:
                weathh.append(ad1[1])
                ff += 1
        first_weather = weathh[0]
        second_weather = weathh[1]
        third_weather = weathh[2]
        fourth_weather = weathh[3]
        fifth_weather = weathh[4]
        sixth_weather= weathh[5]
        seventh_weather = weathh[6]
        temp = html.find(class_="today-temp").text
        t_min = el.select('.temperature .min')[0].text
        t_max = el.select('.temperature .max')[0].text
        text = el.select('.wDescription .description')[0].text
        city_ = html.find("div", class_="clearfix").find("div", class_="cityName cityNameShort").find("strong").text



@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global rez, city_old, rezz, text_old, text, temp, answer
    if answer == 1 and message.text.isdigit():
        tt = int(message.text)
        if tt == 1:
            e = weather(rez)
            if e == 0 or text == 0:
                bot.send_message(message.chat.id, "Ви ввели неправильну назву міста(")
            else:
                try:
                    temp = str(temp)
                    bot.send_message(message.chat.id, f'Привіт погода сьогодні {city_}:\nНа вулиці зараз {temp}\n'
                                                      f'{t_min}{t_max}\n{text}')
                except Exception as ex:
                    bot.send_message(message.chat.id, "Ви ввели неправильну назву міста(")
                    print(1)
                    print(ex)
                text_old = text
                text = 0
            rezz = 0
            rez = ' '
            city_old = " "
            answer = 0
        elif tt == 2:
            e = weather(rez)
            if e == 0 or text == 0:
                bot.send_message(message.chat.id, "Ви ввели неправильну назву міста(")
            else:
                try:
                    temp = str(temp)
                    bot.send_message(message.chat.id, f'Привіт погода {city_} на сім днів:\n{first_day}:\n{first_temperature}\nНа вулиці буде {first_weather}\n'
                                                      f'{second_day}:\n{second_temperature}\nНа вулиці буде {second_weather}\n')
                except Exception as ex:
                    bot.send_message(message.chat.id, "Ви ввели неправильну назву міста(")
                    print(1)
                    print(ex)
                text_old = text
                text = 0
        elif tt == 3:
            e = weather(rez)
            if e == 0 or text == 0:
                bot.send_message(message.chat.id, "Ви ввели неправильну назву міста(")
            else:
                try:
                    temp = str(temp)
                    bot.send_message(message.chat.id, f'Привіт погода {city_} на сім днів:\n{first_day}:\n{first_temperature}\nНа вулиці буде {first_weather}\n'
                                                      f'{second_day}:\n{second_temperature}\nНа вулиці буде {second_weather}\n'
                                                      f'{third_day}:\n{third_temperature}\nНа вулиці буде {third_weather}\n')
                except Exception as ex:
                    bot.send_message(message.chat.id, "Ви ввели неправильну назву міста(")
                    print(1)
                    print(ex)
                text_old = text
                text = 0
        elif tt == 4:
            e = weather(rez)
            if e == 0 or text == 0:
                bot.send_message(message.chat.id, "Ви ввели неправильну назву міста(")
            else:
                try:
                    temp = str(temp)
                    bot.send_message(message.chat.id, f'Привіт погода {city_} на сім днів:\n{first_day}:\n{first_temperature}\nНа вулиці буде {first_weather}\n'
                                                      f'{second_day}:\n{second_temperature}\nНа вулиці буде {second_weather}\n'
                                                      f'{third_day}:\n{third_temperature}\nНа вулиці буде {third_weather}\n'
                                                      f'{fourth_day}:\n{fourth_temperature}\nНа вулиці буде {fourth_weather}\n')
                except Exception as ex:
                    bot.send_message(message.chat.id, "Ви ввели неправильну назву міста(")
                    print(1)
                    print(ex)
                text_old = text
                text = 0
        elif tt == 5:
            e = weather(rez)
            if e == 0 or text == 0:
                bot.send_message(message.chat.id, "Ви ввели неправильну назву міста(")
            else:
                try:
                    temp = str(temp)
                    bot.send_message(message.chat.id, f'Привіт погода {city_} на сім днів:\n{first_day}:\n{first_temperature}\nНа вулиці буде {first_weather}\n'
                                                      f'{second_day}:\n{second_temperature}\nНа вулиці буде {second_weather}\n'
                                                      f'{third_day}:\n{third_temperature}\nНа вулиці буде {third_weather}\n'
                                                      f'{fourth_day}:\n{fourth_temperature}\nНа вулиці буде {fourth_weather}\n'
                                                      f'{fifth_day}:\n{fifth_temperature}\nНа вулиці буде {fifth_weather}\n')
                except Exception as ex:
                    bot.send_message(message.chat.id, "Ви ввели неправильну назву міста(")
                    print(1)
                    print(ex)
                text_old = text
                text = 0
        elif tt == 6:
            e = weather(rez)
            if e == 0 or text == 0:
                bot.send_message(message.chat.id, "Ви ввели неправильну назву міста(")
            else:
                try:
                    temp = str(temp)
                    bot.send_message(message.chat.id, f'Привіт погода {city_} на сім днів:\n{first_day}:\n{first_temperature}\nНа вулиці буде {first_weather}\n'
                                                      f'{second_day}:\n{second_temperature}\nНа вулиці буде {second_weather}\n'
                                                      f'{third_day}:\n{third_temperature}\nНа вулиці буде {third_weather}\n'
                                                      f'{fourth_day}:\n{fourth_temperature}\nНа вулиці буде {fourth_weather}\n'
                                                      f'{fifth_day}:\n{fifth_temperature}\nНа вулиці буде {fifth_weather}\n'
                                                      f'{sixth_day}:\n{sixth_temperature}\nНа вулиці буде {sixth_weather}\n')
                except Exception as ex:
                    bot.send_message(message.chat.id, "Ви ввели неправильну назву міста(")
                    print(1)
                    print(ex)
                text_old = text
                text = 0
        elif tt == 7:
            e = weather(rez)
            if e == 0 or text == 0:
                bot.send_message(message.chat.id, "Ви ввели неправильну назву міста(")
            else:
                try:
                    temp = str(temp)
                    bot.send_message(message.chat.id, f'Привіт погода {city_} на сім днів:\n{first_day}:\n{first_temperature}\nНа вулиці буде {first_weather}\n'
                                                      f'{second_day}:\n{second_temperature}\nНа вулиці буде {second_weather}\n'
                                                      f'{third_day}:\n{third_temperature}\nНа вулиці буде {third_weather}\n'
                                                      f'{fourth_day}:\n{fourth_temperature}\nНа вулиці буде {fourth_weather}\n'
                                                      f'{fifth_day}:\n{fifth_temperature}\nНа вулиці буде {fifth_weather}\n'
                                                      f'{sixth_day}:\n{sixth_temperature}\nНа вулиці буде {sixth_weather}\n'
                                                      f'{seventh_day}:\n{seventh_temperature}\nНа вулиці буде {seventh_weather}\n')
                except Exception as ex:
                    bot.send_message(message.chat.id, "Ви ввели неправильну назву міста(")
                    print(1)
                    print(ex)
                text_old = text
                text = 0
            rezz = 0
            rez = ' '
            city_old = " "
            answer = 0
    elif rezz == 1 and message != '/weather' and message != '/start':
        rez = message.text
        rez = rez.lower()
        bot.send_message(message.chat.id, 'В наступному повідомленні вкажіть кількість днів на які ви хочете отримати погоду(1 до 7),'
                                          'в повідомленні повинна бути тільки цифра.')
        answer = 1
        rezz = 0
    elif message.text == "/weather" or message.text == "/start":
        bot.send_message(message.chat.id, 'В наступному повідомленні вкажіть ваше місто українською')
        rezz =1
    elif message.text == "/stop" and message.from_user.id == 1107876782:
        ed()
    elif message.text == "/help":
        bot.send_message(message.chat.id,"спробуйте написати /weather)")
    else:   
        bot.send_message(message.chat.id,"Я вас не розумію(")

bot.polling(none_stop=True)
