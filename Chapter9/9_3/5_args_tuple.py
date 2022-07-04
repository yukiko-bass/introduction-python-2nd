# tuple はイミュータブル（変更不可な）リスト


def print_args(*args):
    print("Positional tuple:", args)


def print_more(required1, required2, *args):
    print("Need this one:", required1)
    print("Need this one too:", required2)
    print("All the rest:", args)


if __name__ == "__main__":
    print_args()
    print_args(3, 2, 1, "wait!", "uh...")

    print_more("cap", "gloves", "scarf", "monocle", "mustache wax")

    # Positional tuple: (2, 5, 7, 'x')
    print_args(2, 5, 7, "x")
    args = (2, 5, 7, "x")
    # Positional tuple: ((2, 5, 7, 'x'),)
    print_args(args)
    # Positional tuple: (2, 5, 7, 'x')
    print_args(*args)
