class Fruit:
    color = "red"


blueberry = Fruit()
# インスタンス化してなくてもアクセスできる・・・
print(Fruit.color)
print(blueberry.color)

print("-----")
blueberry.color = "blue"
print(blueberry.color)
print(Fruit.color)

print("-----")
Fruit.color = "orange"
print(Fruit.color)
print(blueberry.color)

new_fruit = Fruit()
print(new_fruit.color)
