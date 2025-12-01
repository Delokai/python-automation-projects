import requests

city = input("Enter a city: ")

url = f"https://wttr.in/{city}?format=j1"

response = requests.get(url).json()

current = response["current_condition"][0]

print("\nWeather Report:\n")
print("Temperature:", current["temp_C"], "°C")
print("Feels Like:", current["FeelsLikeC"], "°C")
print("Humidity:", current["humidity"] + "%")
print("Condition:", current["weatherDesc"][0]["value"])