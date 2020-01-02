from requests import get
import sys


def get_fahrenheit(tempC, city):
    tempF = 9.0 / 5.0 * tempC + 32
    end = print("the weather in", city, "today is", tempF, "Fahrenheit")
    return end


def main(city):
    weather = get("http://api.weatherstack.com/current?access_key=fce675c04b207f60a9e880fa544f7e80&query=" + city)
    data = weather.json()
    temp = data["current"]["temperature"]
    if sys.argv[2] == '-f':
        fahrenheit = get_fahrenheit(temp, city)
        return fahrenheit
    else:
        end = print("the weather in", city, "today is", temp, "Celsius")
        return end


if __name__ == '__main__':
    main(sys.argv[1])

