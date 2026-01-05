import charts
import read_csv
import utils


def run():
    data = read_csv.read_csv("./app/data.csv")
    country = input("Buscar pais: ")

    keys, values = utils.filter_country(country, data)
    try:
        if len(keys) > 0:
            print(keys, values)
            charts.generate_bar_chart(keys, values)
    except Exception as e:
        print(f"Error: {e}, {type(e)}")

    values, labels = utils.world_population_percentage(data)
    charts.generate_pie_chart(values, labels)

    continent, popultaion = utils.continent_population_percentage(data)
    charts.generate_pie_chart(popultaion, continent)


if __name__ == "__main__":
    run()
