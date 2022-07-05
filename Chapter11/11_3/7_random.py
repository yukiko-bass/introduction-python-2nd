from random import choice, randint, randrange, sample


# ランダムに返す
print(choice([23, 9, 46, "bacon", 0x123ABC]))

print(choice(("a", "one", "and-a", "two")))

print(choice(range(100)))

print(choice("alphabet"))


print("-----")

# ランダムな値を複数返す
print(sample([23, 9, 46, "bacon", 0x123ABC], 3))

print(sample(("a", "one", "and-a", "two"), 2))

print(sample(range(100), 4))

print(sample("alphabet", 7))

print("-----")

# 任意の範囲からランダムな整数を取り出す
print(randint(38, 74))

print("-----")
# 先頭（含まれる）と末尾（含まれない）を指定し、オプションでステップを指定する
print(randrange(38, 74))

print(randrange(38, 74, 10))

print(randrange(38, 74, 10))

print("-----")
