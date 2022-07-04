def outer(a, b):
    def inner(c, d):
        return c + d

    return inner(a, b)


def knights(saying):
    def inner(quote):
        return f"We are the knights who say: '{quote}'"

    return inner(saying)


if __name__ == "__main__":
    print(outer(4, 7))

    print(knights("Ni!"))
