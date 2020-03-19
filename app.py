import requests

URL = 'http://api.openweathermap.org/data/2.5/weather?q='
API_KEY = '5f73f957cfc51f3c9da6f5022db662a1'
check_weather = True
while check_weather:
    city = input("Введите название города:")
    res = requests.get(URL + city + '&appid=' + API_KEY)
    res = res.json()
    if city == "/exit":
        check_weather = False
    else:
        try:
            name = res['name']
            country = res['sys']['country']
            temp = int(res['main']['temp'] - 273)
            weather = res['weather'][0]['main']
            wind = res['wind']['speed']
            print(name, country)
            print("Temp:", temp, "°C")
            print("Weather:", weather)
            print("Wind:", wind, "mps")
        except:
            print("Invalid city name, try again")
