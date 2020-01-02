from requests import get
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--cities', nargs='+')
parser.add_argument('-u', '--units', help="enter f/c for Celsius or Fahrenheit. ")
args = parser.parse_args()
if args.units == 'f':
    for city in args.cities:
        weather = get(
            "http://api.weatherstack.com/current?access_key=fce675c04b207f60a9e880fa544f7e80&query=" + city + "&units=f")
        data = weather.json()
        temperature = data["current"]["temperature"]
        print("the weather in", city, "today is", temperature, "Fahrenheit")

else:
    for city in args.cities:
        weather = get(
            "http://api.weatherstack.com/current?access_key=fce675c04b207f60a9e880fa544f7e80&query=" + city)
        data = weather.json()
        temperature = data["current"]["temperature"]
        print("the weather in", city, "today is", temperature, "Celsius")
