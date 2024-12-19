import phonenumbers
from phonenumbers import geocoder, carrier
import folium
from geopy.geocoders import Nominatim
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

# Input phone number with country code
phone_number = input("Enter phone number with country code: ")

# Parse the phone number
parsed_number = phonenumbers.parse(phone_number)

# Get the location and carrier info
location = geocoder.description_for_number(parsed_number, 'en')
service_provider = carrier.name_for_number(parsed_number, 'en')

print(f"Location: {location}")
print(f"Carrier: {service_provider}")

if location:
    # Geocode the location to get coordinates
    geolocator = Nominatim(user_agent="phone_location_map")
    location_data = geolocator.geocode(location)

    if location_data:
        # Get detailed address components
        address = location_data.address
        city = None
        state = None
        country = None

        # Splitting the address into components
        address_components = location_data.raw.get('address', {})
        if address_components:
            city = address_components.get('city', None)
            state = address_components.get('state', None)
            country = address_components.get('country', None)

        # Print location details including state and city
        print(f"Address: {address}")
        print(f"City: {city if city else 'Not Available'}")
        print(f"State: {state if state else 'Not Available'}")
        print(f"Country: {country if country else 'Not Available'}")

        # Create a map centered at the location's coordinates
        country_map = folium.Map(location=[location_data.latitude, location_data.longitude], zoom_start=5)
        folium.Marker([location_data.latitude, location_data.longitude], popup=f"Location: {location}").add_to(country_map)

        # Save map as HTML
        map_file = os.path.abspath("country_map.html")
        country_map.save(map_file)

        # Configure Selenium WebDriver
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get(f"file://{map_file}")

        # Wait for the map to load (more time to ensure map is fully rendered)
        time.sleep(5)  # Increase wait time to 5 seconds

        # Save screenshot as PNG
        png_file = os.path.abspath("country_map.png")
        driver.save_screenshot(png_file)
        driver.quit()

        # Delete the temporary HTML file after the map is processed
        os.remove(map_file)

        print(f"Map saved successfully as '{png_file}'.")
    else:
        print("Could not fetch coordinates for the location.")
else:
    print("Location could not be determined.")
