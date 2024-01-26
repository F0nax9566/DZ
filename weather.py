from bs4 import BeautifulSoup
import requests
import time


def fetch_weather_info(target_location):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}

    while True:
        response = requests.get(
            f'https://www.google.com/search?q={target_location}&oq={target_location}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',
            headers=headers
        )

        soup = BeautifulSoup(response.text, 'html.parser')

        time_elem = soup.select('#wob_dts')
        precipitation_elem = soup.select('#wob_dc')
        weather_elem = soup.select('#wob_tm')

        if time_elem and precipitation_elem and weather_elem:
            current_time = time_elem[0].getText().strip()
            precipitation = precipitation_elem[0].getText().strip()
            current_temperature = weather_elem[0].getText().strip()

            print(f'Weather information for {target_location}:')
            print(f'''Time and Date: {current_time}
Precipitation Information: {precipitation}
Temperature: {current_temperature}°C''')

            update_time = time.strftime('%Y-%m-%d %H:%M:%S')
            print(f'Information last updated at: {update_time}')
        else:
            print(f"The required information for {target_location} could not be found or you did not enter your API.")

        time.sleep(1800)


if __name__ == '__main__':
    target_location = 'Kyiv'
    fetch_weather_info(f'{target_location} weather')
