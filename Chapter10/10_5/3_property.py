class Duck:
    def __init__(self, input_name):
        self.hidden_name = input_name

    def get_name(self):
        print("inside the getter")
        return self.hidden_name

    def set_name(self, input_name):
        print("inside the setter")
        self.hidden_name = input_name

    name = property(get_name, set_name)


don = Duck("Donald")
# まだ getter/setter も使える
print(don.get_name())
don.set_name("Donna")
print(don.get_name())

print("-----")
# property も使えるようになった
print(don.name)
don.name = "Donna"

print(don.name)

print("-----")


class Duck2:
    def __init__(self, input_name):
        self.hidden_name = input_name

    # getter の前に付ける
    @property
    def name(self):
        print("inside the getter")
        return self.hidden_name

    @name.setter
    def name(self, input_name):
        print("inside the setter")
        self.hidden_name = input_name


fowl = Duck("Howard")
print(fowl.name)

fowl.name = "Donald"
print(fowl.name)
