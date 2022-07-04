def menu(wine, entree, dessert):
    return {"wine": wine, "entree": entree, "dessert": dessert}


if __name__ == "__main__":
    print(menu("chardonnay", "chicken", "cake"))
    print(menu("beef", "bagel", "bordeaux"))
