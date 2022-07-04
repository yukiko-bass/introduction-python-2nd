outside = ["one", "fine", "day"]


def mangle(arg):
    arg[1] = "terrible!"


if __name__ == "__main__":
    print(outside)

    mangle(outside)

    # 書き換わる
    print(outside)
