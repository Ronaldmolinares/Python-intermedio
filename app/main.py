import charts
import read_csv
import utils


def mostrar_menu():
    print("\n" + "=" * 50)
    print("World Population Dataset")
    print("=" * 50)
    print("1. Buscar país y mostrar gráfico de barras")
    print("2. Ver porcentaje de población mundial (gráfico de pastel)")
    print("3. Ver población por continente (gráfico de pastel)")
    print("4. Salir")
    print("=" * 50)


def buscar_pais(data):
    country = input("\nIngrese el nombre del país: ")
    keys, values = utils.filter_country(country, data)

    try:
        if len(keys) > 0:
            print(f"\nDatos de {country.title()}:")
            print(f"Años: {keys}")
            print(f"Población: {values}")
            charts.generate_bar_chart(keys, values)
        else:
            print(f"\nNo se encontró el país '{country}'")
    except Exception as e:
        print(f"Error: {e}, {type(e)}")


def mostrar_poblacion_mundial(data):
    print("\nGenerando gráfico de población mundial...")
    values, labels = utils.world_population_percentage(data)
    charts.generate_pie_chart(values, labels)


def mostrar_poblacion_continente(data):
    print("\nGenerando gráfico de población por continente...")
    continent, population = utils.continent_population_percentage(data)
    charts.generate_pie_chart(population, continent)


def run():
    data = read_csv.read_csv("./app/data.csv")

    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-4): ")

        if opcion == "1":
            try:
                buscar_pais(data)
            except ValueError as e:
                print(f"Error: Pais no registrado en el data set\n{e} , {type(e)}")
        elif opcion == "2":
            mostrar_poblacion_mundial(data)
        elif opcion == "3":
            mostrar_poblacion_continente(data)
        elif opcion == "4":
            print("\n¡Hasta luego!")
            break
        else:
            print("\nOpción inválida. Por favor, seleccione 1, 2, 3 o 4.")


if __name__ == "__main__":
    run()
