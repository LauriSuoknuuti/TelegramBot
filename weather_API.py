import pyowm


def main():
    owm = pyowm.OWM("183f929d03a36cde0b893c0b59fd1d9d")
    forecast = owm.weather_at_place("Otaniemi, finland")
    w = forecast.get_weather()
    current_weather = ["Otaniemi; Finland", w.get_temperature(unit='celsius')]
    return current_weather


