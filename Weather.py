#!/usr/bin/env python
# coding: utf-8

# # Weather Checking Application
We can execute the following functions:
1. Check weather by city
2. Add your favorite city
3. Remove your favorite city
4. Display your favorite cities
5. Toggle auto-refresh (15 seconds)
# # Importing Libraries

# In[1]:


import requests
import time
import json


# # API Key

# In[2]:


# Replace the API key from https://www.weatherapi.com/
API_KEY = 'c851881264344e7ca2353350240601'


# # Function To Get Weather By City Name

# In[3]:


def get_weather_by_city(city):
    try:
        url = f'http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}'
        response = requests.get(url)
        data = response.json()
        if 'error' in data:
            print(f"Error: {data['error']['message']}")
        else:
            print(f"Weather in {city}:")
            print(f"Temperature: {data['current']['temp_c']}°C")
            print(f"Condition: {data['current']['condition']['text']}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


# # Function To Add Favourite City

# In[4]:


def add_favorite_city(city, favorites):
    if city not in favorites:
        favorites.append(city)
        print(f"{city} added to favorites.")
    else:
        print(f"{city} is already in favorites.")


# # Function To Remove Favourite City

# In[5]:


def remove_favorite_city(city, favorites):
    if city in favorites:
        favorites.remove(city)
        print(f"{city} removed from favorites.")
    else:
        print(f"{city} is not in favorites.")


# # Function To Display Favourite City

# In[6]:


def display_favorites(favorites):
    if favorites:
        print("Favorite cities:")
        for city in favorites:
            print(f"- {city}")
    else:
        print("No favorite cities.")


# # Main Function To Get Data From User Input

# In[ ]:


def main():
    favorites = []
    auto_refresh = False

    while True:
        print("\nWeather Checking Application!!!\n")
        print("1. Check weather by city")
        print("2. Add your favorite city")
        print("3. Remove your favorite city")
        print("4. Display your favorite cities")
        print("5. Toggle auto-refresh (15 seconds)")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            city_name = input("Enter the city name: ")
            get_weather_by_city(city_name)

        elif choice == '2':
            city_name = input("Enter the city name to add to favorites: ")
            add_favorite_city(city_name, favorites)

        elif choice == '3':
            city_name = input("Enter the city name to remove from favorites: ")
            remove_favorite_city(city_name, favorites)

        elif choice == '4':
            display_favorites(favorites)

        elif choice == '5':
            auto_refresh = not auto_refresh
            print(f"Auto-refresh {'enabled' if auto_refresh else 'disabled'}.")

        elif choice == '0':
            print("Exiting Weather Checking Application.....")
            break

        else:
            print("Invalid choice!!!")

        if auto_refresh:
            time.sleep(15)

if __name__ == "__main__":
    main()


# In[ ]:




