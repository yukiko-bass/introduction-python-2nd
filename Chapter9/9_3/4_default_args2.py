# デフォルト引数が計算されるのは関数が呼ばれたときではなく、定義されたとき
def buggy(arg, result=[]):
    result.append(arg)
    print(result)


# 毎回初期化してほしかったらデフォルト引数に定義しない
def works(arg):
    result = []
    result.append(arg)
    return result


# 最初の呼び出しだということを示す、別のものを渡す方法
def nonbuggy(arg, result=None):
    if result is None:
        result = []
    result.append(arg)
    print(result)


if __name__ == "__main__":
    buggy("a")
    buggy("b")  # ['b'] になると思ってるが['a', 'b']

    print(works("a"))
    print(works("b"))

    nonbuggy("a")
    nonbuggy("b")
