class Animal:
    def says(self):
        return "I speak!"


class Horse(Animal):
    def says(self):
        return "Neigh!"


class Donkey(Animal):
    def says(self):
        return "Hee-haw!"


class Mule(Donkey, Horse):
    """
    探索順
    1. オブジェクト自体（自分：Mule型）
    2. オブジェクトのクラス（Mule）
    3. オブジェクトの第一親クラス（Donkey）
    4. オブジェクトの第二親クラス（Horse）
    5. オブジェクトの祖先クラス（Animal）
    """

    pass


class Hinny(Horse, Donkey):
    pass


print(Mule.mro())
print(Hinny.mro())

mule = Mule()
hinny = Hinny()
print(mule.says())
print(hinny.says())
