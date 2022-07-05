from collections import namedtuple


Duck = namedtuple("Duck", "bill tail")
duck = Duck("wide orange", "long")
print(duck)

print(duck.bill)
print(duck.tail)

print("-----")

parts = {"bill": "wide orange", "tail": "long"}
duck2 = Duck(**parts)
print(duck2)

print("-----")

duck3 = duck2._replace(tail="magnificent", bill="crushing")
print(duck3)

print("-----")

duck_dict = {"bill": "wide orange", "tail": "long"}
print(duck_dict)

print("-----")

duck_dict["color"] = "green"
print(duck_dict)

print("-----")
"""
名前付きタプルの長所
・イミュータブルなオブジェクトっぽく振る舞える
・オブジェクトよりも、空間的、時間的に効率が良い
・辞書スタイルの角括弧ではなく、ドット記法でアクセスできる
・辞書のキーとして使える
"""
