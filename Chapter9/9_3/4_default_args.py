def menu(wine, entree, dessert="pudding"):
    return {"wine": wine, "entree": entree, "dessert": dessert}


if __name__ == "__main__":
    # デフォルト引数
    print(menu("chardonnay", "chicken"))

    print(menu("dunkelfelder", "duck", "doughnut"))
