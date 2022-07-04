# 見えない形でyieldを実行している
genobj = (pair for pair in zip(["a", "b"], ["1", "2"]))
print(genobj)

for thing in genobj:
    print(thing)
