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


if __name__ == "__main__":
    run()
