import requests


import click

weather_url = "http://api.weatherstack.com/current?"


@click.command()
@click.option('-t', '--token', )
@click.option('-l', '--celsius', )
@click.option('-c', '--fahrenheit')
@click.option('--cities', multiple=True)
def weather(cities, celsius, fahrenheit, token):
    for city in range(cities):
        complete_url = weather_url + "access_key=" + token + "&query=" + city
        response = requests.get(complete_url)
        response_in_json_format = response.json()
        city_weather = response_in_json_format['current']['temperature']
        city_name = response_in_json_format['location']['name']
        if celsius:
            print("the weather of " + city_name + " is " + str(city_weather) + "-c")
        elif fahrenheit:
            print("the weather of " + city_name + " is " + str(city_weather) + "-f")
        if 'error' in response_in_json_format:
            print(response_in_json_format)


if __name__ == '__main__':
    weather()
