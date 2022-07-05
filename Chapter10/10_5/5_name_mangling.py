class Duck:
    def __init__(self, input_name):
        """戦闘に2つのアンダースコア(__)でクラス外から見えなくする"""
        self.__name = input_name

    @property
    def name(self):
        print("inside the getter")
        return self.__name

    @name.setter
    def name(self, input_name):
        print("inside the setter")
        self.__name = input_name


fowl = Duck("Howard")
print(fowl.name)

fowl.name = "Donald"
print(fowl.name)

# error
try:
    print(fowl.__name)
except Exception:
    pass

# ok
print(fowl._Duck__name)
