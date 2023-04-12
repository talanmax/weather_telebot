import requests
from bs4 import BeautifulSoup as bs
def weather(city):
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
        weather_text = f'Привіт погода {city_} на сім днів:\n{first_day}:\n{first_temperature}\nНа вулиці буде {first_weather}\n{second_day}:\n{second_temperature}\nНа вулиці буде {second_weather}\n{third_day}:\n{third_temperature}\nНа вулиці буде {third_weather}\n{fourth_day}:\n{fourth_temperature}\nНа вулиці буде {fourth_weather}\n{fifth_day}:\n{fifth_temperature}\nНа вулиці буде {fifth_weather}\n{sixth_day}:\n{sixth_temperature}\nНа вулиці буде {sixth_weather}\n{seventh_day}:\n{seventh_temperature}\nНа вулиці буде {seventh_weather}\n'
        return weather_text
    return "Не знайшли"
#1 2
#3