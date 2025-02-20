import unittest

import requests


def get_population(country):
    url = f"https://world-population.p.rapidapi.com/population?country_name={country}"
    headers = {"X-RapidAPI-Key": "YOUR_API_KEY"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data["body"]["population"]
    else:
        return "Error fetching data"


country = input("Enter country name: ")
print(f"Population of {country}: {get_population(country)}")




if __name__ == "__main__":
    unittest.main()
