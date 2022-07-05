from collections import defaultdict


periodic_table = {"Hydrogen": 1, "Helium": 2}
print(periodic_table)

print("-----")

# キーにまだなければ追加
carbon = periodic_table.setdefault("Carbon", 12)
print(carbon)

print(periodic_table)
print("-----")

# 既存のキーに別のデフォルト値を入れようとしても変更されない
helium = periodic_table.setdefault("Helium", 947)
print(helium)
print(periodic_table)

print("-----")

# defaultdict はvalueの初期値を設定する
periodic_table = defaultdict(int)

print(periodic_table["Lead"])
print(periodic_table)

print("-----")


def no_idea():
    return "Huh?"


bestiary = defaultdict(no_idea)
bestiary["A"] = "Abominable Snowman"
bestiary["B"] = "Basilisk"
print(bestiary["A"])
print(bestiary["B"])
print(bestiary["C"])

print("-----")

bestiary = defaultdict(lambda: "Huh?")
print(bestiary["E"])

print("-----")

food_counter = defaultdict(int)
for food in ["spam", "spam", "eggs", "spam"]:
    food_counter[food] += 1

for food, count in food_counter.items():
    print(food, count)

print("-----")

# 普通の辞書の場合
dict_counter = {}
for food in ["spam", "spam", "eggs", "spam"]:
    # 追加のロジックが必要になる
    if not food in dict_counter:
        dict_counter[food] = 0
    dict_counter[food] += 1

for food, count in food_counter.items():
    print(food, count)
