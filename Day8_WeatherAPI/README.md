🌦️ Day 8 — Weather API Script

This project uses a public weather API to fetch real-time weather information for any city.
You learned how to send online API requests and process JSON data—an essential skill for automation and SaaS development.

🔧 Tools Used

requests — sends HTTP requests to fetch API data

wttr.in API — free weather service returning structured JSON

Python 3

📌 What the Script Does

Prompts the user for a city name

Sends a request to the weather API:

https://wttr.in/<city>?format=j1


Extracts:

🌡 Temperature (°C)

🌡 Feels Like (°C)

💧 Humidity

☁️ Weather Description

Displays the weather in a clean, readable format

▶️ How to Run

Open your terminal and navigate to the folder:

cd Day8_WeatherAPI


Run the script:

python weather.py


Enter any city, for example:

Dublin

📘 Example Output
Weather Report:

Temperature: 7 °C
Feels Like: 4 °C
Humidity: 88%
Condition: Partly cloudy

🎯 Skills Learned

How APIs work

Sending HTTP requests

Reading and parsing JSON

Displaying structured data

Real-world automation with internet data
