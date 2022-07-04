# * は『これ以降の引数はキーワード引数という形でしか渡せない』の意味
def print_data(data, *, start=0, end=100):
    for value in data[start:end]:
        print(value)


if __name__ == "__main__":
    data = ["a", "b", "c", "d", "e", "f"]
    print_data(data)
    print("------")
    print_data(data, start=4)
    print("------")
    print_data(data, end=2)
    print("------")
