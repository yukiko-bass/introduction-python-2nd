# RecursionError: maximum recursion depth exceeded
def dive():
    return dive()


def flatten(lol):
    for item in lol:
        if isinstance(item, list):
            for subitem in flatten(item):
                yield subitem
        else:
            yield item


# ジェネレータが他のジェネレータに移譲できる yield from式を使うこともできる
def flatten2(lol):
    for item in lol:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item


if __name__ == "__main__":
    try:
        dive()
    except RecursionError as e:
        print(e)
        pass

    lol = [1, 2, [3, 4, 5], [6, [7, 8, 9], []]]
    print(flatten(lol))

    print(list(flatten(lol)))

    flatten2(lol)
    print(list(flatten2(lol)))
