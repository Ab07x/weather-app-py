
import tkinter as tk
from tkinter import messagebox
import requests
import datetime

API_KEY = "your_api_key_here"  # Replace this with your actual OpenWeatherMap API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def display_weather():
    city = city_entry.get()
    weather = get_weather(city)
    if weather:
        temp = weather['main']['temp']
        condition = weather['weather'][0]['description']
        result = f"City: {city}\nTemperature: {temp}°C\nCondition: {condition}\nTime: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        output_label.config(text=result)
        save_to_file(result)
    else:
        messagebox.showerror("Error", "City not found or API error.")

def save_to_file(data):
    with open("weather_log.txt", "a") as file:
        file.write(data + "\n---\n")

# Tkinter GUI setup
root = tk.Tk()
root.title("Weather App")
root.geometry("350x250")

tk.Label(root, text="Enter City Name:", font=('Arial', 12)).pack(pady=10)
city_entry = tk.Entry(root, width=30)
city_entry.pack()

tk.Button(root, text="Get Weather", command=display_weather).pack(pady=10)
output_label = tk.Label(root, text="", font=('Arial', 10), justify='left')
output_label.pack(pady=10)

root.mainloop()
