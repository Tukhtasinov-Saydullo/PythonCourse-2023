import tkinter as tk
import requests

# Your OpenWeatherMap API key
API_KEY = "e150b5d2a33d079c015bc021f22e43f9"


def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data


def update_weather():
    city = city_entry.get()
    data = get_weather_data(city)
    if data["cod"] != 200:
        weather_label.config(text=f"Error: {data['message']}")
    else:
        weather = data["weather"][0]["main"]
        temperature = data["main"]["temp"]
        weather_label.config(text=f"Weather: {weather}, Temperature: {temperature}°C")


# Create the Tkinter window
window = tk.Tk()
window.title("Weather App")

# Create the city entry and update button
city_label = tk.Label(text="City:")
city_entry = tk.Entry()
update_button = tk.Button(text="Update", command=update_weather)

# Create the weather label
weather_label = tk.Label(text="Enter a city and click Update to get the weather.")

# Add the widgets to the window
city_label.pack()
city_entry.pack()
update_button.pack()
weather_label.pack()

# Start the Tkinter event loop
window.mainloop()
