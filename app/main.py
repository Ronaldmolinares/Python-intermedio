import utils

countries = [
    {
        "Country": "Colombia",
        "Population": 1200,
    },
    {
        "Country": "Letonia",
        "Population": 800,
    },
    {
        "Country": "Lituania",
        "Population": 400,
    },
]


keys, values = utils.get_population()

print(keys, values)

country = utils.population_by_country(countries, "Colombia")
print(country)
