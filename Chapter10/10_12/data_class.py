# python3.7 から使える
# 参考：https://qiita.com/tag1216/items/13b032348c893667862a

from dataclasses import dataclass


class TeenyClass:
    def __init__(self, name):
        self.name = name


teeny = TeenyClass("itsy")
print(teeny.name)


@dataclass
class TeenyDataClass:
    name: str


teeny = TeenyDataClass("bitsy")
print(teeny.name)


@dataclass
class AnimalClass:
    name: str
    habitat: str
    teeth: int = 0


snowman = AnimalClass("yeti", "Himalayas", 46)
duck = AnimalClass(habitat="lake", name="duck")
print(snowman)
print(duck)

print(duck.habitat)
print(snowman.teeth)
