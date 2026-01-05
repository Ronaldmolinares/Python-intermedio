import matplotlib.pyplot as plt


def generate_bar_chart(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()


def generate_pie_chart(values, labels):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct="%1.1f%%")
    plt.show()


if __name__ == "__main__":
    labels = ["a", "b", "c"]
    values = [100, 200, 300]
    # generate_bar_chart(labels, values)
    generate_pie_chart(labels, values)
