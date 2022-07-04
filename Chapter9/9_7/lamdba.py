def edit_story(words, func):
    for word in words:
        print(func(word))


def enliven(word):
    return word.capitalize() + "!"


if __name__ == "__main__":
    stairs = ["thud", "meow", "thud", "hiss"]

    edit_story(stairs, enliven)

    print("-----")

    # enliven は短いのでラムダに変える
    edit_story(stairs, lambda word: word.capitalize() + "!")
