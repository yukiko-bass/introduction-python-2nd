def my_range(first=0, last=10, step=1):
    """ジェネレータ関数は普通の関数とは違って yield で値を返す"""
    number = first
    while number < last:
        yield number
        number += step


if __name__ == "__main__":
    print(my_range)

    ranger = my_range(1, 5)
    print(ranger)

    # このジェネレータオブジェクトを対象として反復処理できる
    for x in ranger:
        print(x)

    print("-----")
    # ジェネレータは一度しか実行できない
    for try_again in ranger:
        print(try_again)

    print("-----")
    ranger = my_range(2, 6)
    for try_again2 in ranger:
        print(try_again2)
