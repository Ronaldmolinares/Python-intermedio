# file = open("./text.txt")
data = "./text.txt"

with open(data, "r+", encoding="utf-8") as f:
    content = f.read()
    print(content)
    f.write("\nFin.")
