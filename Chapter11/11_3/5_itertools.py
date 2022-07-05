import itertools

# chain(): 引数全体がiterableのように扱い、反復処理をする
for item in itertools.chain([1, 2], ["a", "b"]):
    print(item)

print("-----")
# cycle(): 無限イテレータ
for item in itertools.cycle([1, 2]):
    print(item)
    break

print("-----")
# accumulate(): それまでの要素を一つにまとめた値を計算する。デフォルトは和
for item in itertools.accumulate([1, 2, 3, 4]):
    print(item)


print("-----")


def multiply(a, b):
    return a * b


for item in itertools.accumulate([1, 2, 3, 4], multiply):
    print(item)
