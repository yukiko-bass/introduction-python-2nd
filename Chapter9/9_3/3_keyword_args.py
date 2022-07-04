def menu(wine, entree, dessert):
    return {"wine": wine, "entree": entree, "dessert": dessert}


if __name__ == "__main__":
    # キーワード引数
    print(menu(entree="beef", dessert="bagel", wine="bordeaux"))

    # 位置引数とキーワード引数は併用できる
    print(menu("frontenac", dessert="flan", entree="fish"))
