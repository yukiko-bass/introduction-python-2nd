def print_kwargs(**kwargs):
    print("Keyword arguments:", kwargs)


if __name__ == "__main__":
    print_kwargs()

    print_kwargs(wine="merlot", entree="mutton", dessert="macaroon")
