Countries = {
    "USA": {
        "California": {"Los Angeles": 4000000, "San Francisco": 870000}
    },
    "Canada": {
        "Ontario": {"Toronto": 2930000, "Ottawa": 994837}
    }
}


def updater(countries:dict, country:str, state: dict) -> None:
	countries[country] = state


def get_cities_population(country, state):
    new_country = "Nigeria"
    new_state = {"Lagos": {"mainland": 4_200_329, "ikorodu": 4_230_000}}
    updater(Countries, new_country, new_state)

    if country in Countries :
        if state in Countries[country]:
            print(f"Cities and their populations in {state}, {country}:")
            for city, population in Countries [country][state].items():
                print(f"{city}: {population}")
        else:
            print(f"State '{state}' not found in {country}.") 
            print(f"Possible states in {country}:{(Countries[country].keys())}")
    else:
        print(f"Country '{country}' not found.")
        print(f"the contries we have for now are : {Countries.keys()}")


country_input = input("Enter the country: ")
state_input = input("Enter the state: ")

get_cities_population(country_input, state_input)