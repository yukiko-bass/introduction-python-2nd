def echo(anything):
    """echoは、与えられた入力引数を返す。"""
    return anything


def print_if_true(thing, check):
    """
    第2引数が真なら、第1引数を表示する
    処理内容：
        1. 第2引数が真かどうかチェックする。
        2. 真なら第1引数を表示する
    """
    if check:
        print(thing)


if __name__ == "__main__":
    help(echo)

    print(echo.__doc__)
