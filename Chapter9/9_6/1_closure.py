def knight2(saying):
    def inner2():
        return f"We are the knights who say: '{saying}'"

    # 関数自体を返す
    return inner2


if __name__ == "__main__":
    a = knight2("Duck")
    b = knight2("Hasenpfeffer")

    print(type(a))
    print(type(b))

    print(a)
    print(b)

    print(a())
    print(b())
