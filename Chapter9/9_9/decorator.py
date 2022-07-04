def document_it(func):
    def new_function(*args, **kwargs):
        print("Running function:", func.__name__)
        print("Positional arguments:", args)
        print("Keyword arguments:", kwargs)
        result = func(*args, **kwargs)
        print("Result:", result)
        return result

    return new_function


def add_ints(a, b):
    return a + b


# アノテーションでも同じ
@document_it
def add_ints2(a, b):
    return a + b


def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result

    return new_function


# デコレータは複数持てる
@document_it
@square_it
def add_ints3(a, b):
    return a + b


# デコレータの順序を変えると処理順序も変わる
@square_it
@document_it
def add_ints4(a, b):
    return a + b


if __name__ == "__main__":
    print(add_ints(3, 5))
    print("-----")

    # 手作業でデコレータの戻り値を代入
    cooler_add_ints = document_it(add_ints)

    print(cooler_add_ints(3, 5))

    print("-----")
    print(add_ints2(2, 6))

    print("-----")
    print(add_ints3(3, 5))

    print("-----")
    print(add_ints4(3, 5))
