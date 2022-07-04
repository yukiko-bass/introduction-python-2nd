def whatis(thing):
    if thing is None:
        print(thing, "is None")
    elif thing:
        print(thing, "is True")
    else:
        print(thing, "is False")


if __name__ == "__main__":
    whatis(None)
    whatis(True)
    whatis(False)
    whatis(0)
    whatis(0.0)
    whatis("")
    whatis("")
    whatis("""""")
    whatis(())
    whatis([])
    whatis({})
    whatis(set())

    whatis(0.00001)
    whatis([0])
    whatis([""])
    whatis(" ")
