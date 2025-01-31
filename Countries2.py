Countries = {
    "USA": {
        "California": {"Los Angeles": 4000000, "San Francisco": 870000}
	},
    "Canada": {
        "Ontario": {"Toronto": 2930000, "Ottawa": 994837},
    },
  "Nigeria": {
         "Lagos": {"mainland": 4_200_329, "ikorodu": 4_230_000}}

}

def get_city_population(country, state, city):
    if country in Countries:
        if state in Countries[country]:
            if city in Countries[country][state]:
                return Countries[country][state][city]
            else:
                return f"City '{city}' not found in {state}."
        else:
            return f"State '{state}' not found in {country}."
    else:
        return f"Country '{country}' not found in the Countries."



country = input("Enter the country: ")
state = input("Enter the state:  ")
print(f"{state} state")
city = input("Enter the city: ")


population = get_city_population(country, state, city)
print(f"The population of {city} is {population}.")

























