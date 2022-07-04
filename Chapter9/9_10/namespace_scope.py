# グローバル変数
animal = "fruitbat"


def print_global():
    print("inside print_global:", animal)


def change_and_print_global():
    # ローカル変数を宣言より先に参照したとみなされてエラーになる
    # 先に参照しなければ書き換えは可能
    print("inside change_and_print_global:", animal)
    animal = "wombat"
    print("after the change:", animal)


def change_local():
    # ローカル変数として捉えられる
    animal = "wombat"
    print("inside change_local:", animal, id(animal))


def change_and_print_global2():
    global animal
    animal = "wombat"
    print("inside change_and_print_global2:", animal)


def change_local2():
    animal = "wombat"
    print("locals:", locals())


if __name__ == "__main__":
    print("at the top level:", animal)
    print_global()

    change_local()

    print(animal)

    print(id(animal))

    change_and_print_global2()

    print(animal)

    change_local2()

    print("globals:", globals())
