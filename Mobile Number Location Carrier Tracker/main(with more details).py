import phonenumbers
from phonenumbers import geocoder, carrier
import folium
from geopy.geocoders import Nominatim
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

phone_number = input("Enter phone number with country code: ")

parsed_number = phonenumbers.parse(phone_number)

location = geocoder.description_for_number(parsed_number, 'en')
service_provider = carrier.name_for_number(parsed_number, 'en')

print(f"Location: {location}")
print(f"Carrier: {service_provider}")

if location:
    geolocator = Nominatim(user_agent="phone_location_map")
    location_data = geolocator.geocode(location)

    if location_data:
        address = location_data.address
        city = None
        state = None
        country = None

        address_components = location_data.raw.get('address', {})
        if address_components:
            city = address_components.get('city', None)
            state = address_components.get('state', None)
            country = address_components.get('country', None)

        print(f"Address: {address}")
        print(f"City: {city if city else 'Not Available'}")
        print(f"State: {state if state else 'Not Available'}")
        print(f"Country: {country if country else 'Not Available'}")

        country_map = folium.Map(location=[location_data.latitude, location_data.longitude], zoom_start=5)
        folium.Marker([location_data.latitude, location_data.longitude], popup=f"Location: {location}").add_to(country_map)

        map_file = os.path.abspath("country_map.html")
        country_map.save(map_file)

        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get(f"file://{map_file}")

        time.sleep(5)

        png_file = os.path.abspath("country_map.png")
        driver.save_screenshot(png_file)
        driver.quit()

        os.remove(map_file)

        print(f"Map saved successfully as '{png_file}'.")
    else:
        print("Could not fetch coordinates for the location.")
else:
    print("Location could not be determined.")
