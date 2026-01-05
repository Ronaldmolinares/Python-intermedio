def filter_country(busqueda: str, data):
    try:
        for country in data:
            if country["Country/Territory"] == busqueda.title():
                resultado = {
                    "2022 Population": int(country["2022 Population"]),
                    "2020 Population": int(country["2020 Population"]),
                    "2015 Population": int(country["2015 Population"]),
                    "2010 Population": int(country["2010 Population"]),
                    "2000 Population": int(country["2000 Population"]),
                    "1990 Population": int(country["1990 Population"]),
                    "1980 Population": int(country["1980 Population"]),
                }

        return resultado.keys(), resultado.values()
    except UnboundLocalError:
        return "Error: pais no encontrado."


# def population_by_country(data, country):
#     data = list(filter(lambda item: item["Country"] == country, data))
#     return data
