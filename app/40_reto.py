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
# print("\n")
# print(data[0])

# resultado = filter_country("china", data)
# print(f"\n{resultado}")


def world_population_percentage(data):
    labels = []
    values = []
    for country in data:
        values.append(country["World Population Percentage"])
        labels.append(country["Country/Territory"])

    # result = list(zip(values, labels))
    return values, labels
    # return result


# v, l = world_population_percentage(data)
# print(v[1], l[1])

# go = world_population_percentage(data)
# print(go)


def continent_population_percentage(data):
    labels = []
    values = []
    for country in data:
        values.append(country["World Population Percentage"])
        labels.append(country["Continent"])

    labels = list(dict.fromkeys(labels))
    return values, labels


value, label = continent_population_percentage(data)
print(value[1], label[1])


def continent_population_percentage_2(data):
    dict_continent = {
        "Asia": sum(
            float(country["World Population Percentage"])
            for country in data
            if country["Continent"] == "Asia"
        ),
        "Europe": sum(
            float(country["World Population Percentage"])
            for country in data
            if country["Continent"] == "Europe"
        ),
        "Africa": sum(
            float(country["World Population Percentage"])
            for country in data
            if country["Continent"] == "Africa"
        ),
        "Oceania": sum(
            float(country["World Population Percentage"])
            for country in data
            if country["Continent"] == "Oceania"
        ),
        "South America": sum(
            float(country["World Population Percentage"])
            for country in data
            if country["Continent"] == "South America"
        ),
        "North America": sum(
            float(country["World Population Percentage"])
            for country in data
            if country["Continent"] == "North America"
        ),
    }

    return dict_continent


def solucion_video(data):
    paises = list(map(lambda country: country["Country/Territory"], data))
    porcentaje_poblacion = list(
        map(lambda country: country["World Population Percentage"], data)
    )
    return porcentaje_poblacion, paises


xc = continent_population_percentage_2(data)
print(xc)
