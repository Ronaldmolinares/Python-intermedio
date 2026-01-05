import read_csv as d

data = d.read_csv("./app/data.csv")
filtro_paises = [
    "Country/Territory",
    "2022 Population",
    "2020 Population",
    "2015 Population",
    "2010 Population",
    "2000 Population",
    "1990 Population",
    "1980 Population",
]


def population_country_2(data):
    return [
        {key: country[key] for key in filtro_paises if key in country}
        for country in data
    ]


def population_country(data):
    return [
        {
            "Country/Territory": country["Country/Territory"],
            "2022 Population": country["2022 Population"],
            "2020 Population": country["2020 Population"],
            "2015 Population": country["2015 Population"],
            "2010 Population": country["2010 Population"],
            "2000 Population": country["2000 Population"],
            "1990 Population": country["1990 Population"],
            "1980 Population": country["1980 Population"],
        }
        for country in data
    ]


def population_country_1(data):
    new_dict = []
    for country in data:
        pais = {
            "Country/Territory": country["Country/Territory"],
            "2022 Population": country["2022 Population"],
            "2020 Population": country["2020 Population"],
            "2015 Population": country["2015 Population"],
            "2010 Population": country["2010 Population"],
            "2000 Population": country["2000 Population"],
            "1990 Population": country["1990 Population"],
            "1980 Population": country["1980 Population"],
        }
        new_dict.append(pais)
    return new_dict


def filter_country(busqueda: str, data):
    diccionario = population_country_1(data)
    try:
        for country in diccionario:
            if country["Country/Territory"] == busqueda.title():
                resultado = {
                    "2022 Population": country["2022 Population"],
                    "2020 Population": country["2020 Population"],
                    "2015 Population": country["2015 Population"],
                    "2010 Population": country["2010 Population"],
                    "2000 Population": country["2000 Population"],
                    "1990 Population": country["1990 Population"],
                    "1980 Population": country["1980 Population"],
                }

        return resultado
        # return resultado.keys(), resultado.values()
    except UnboundLocalError:
        return "Error: pais no encontrado."


# r = population_country_2(data)
# print(r)
print("\n")
print(data[0])

resultado = filter_country("china", data)
print(f"\n{resultado}")
