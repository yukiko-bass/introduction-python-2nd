class A:
    count = 0

    def __init__(self):
        # クラス属性
        A.count += 1

    # インスタンスメソッド
    def exclaim(self):
        print("I'm an A!")

    # クラスメソッド（第一引数は必ずcls）
    # クラスを引数にもらうので、クラスに依存はしている
    @classmethod
    def kids(cls):
        print("A has", cls.count, "little objects.")


easy_a = A()
breezy_a = A()
wheezy_a = A()
A.kids()
