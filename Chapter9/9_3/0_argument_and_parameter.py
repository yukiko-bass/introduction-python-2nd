def commentary(color):
    if color == "red":
        return "It's a tomato."
    elif color == "green":
        return "It's a green pepper."
    elif color == "bee purple":
        return "I don't know what it is, but only bees can see it."
    else:
        return "I've never heard of the color " + color + "."


if __name__ == "__main__":
    comment = commentary("red")
    print("red: {}".format(comment))

    comment = commentary("green")
    print("green: {}".format(comment))

    comment = commentary("bee purple")
    print("bee purple: {}".format(comment))

    comment = commentary("blue")
    print("blue: {}".format(comment))
