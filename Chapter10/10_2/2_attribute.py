class Cat:
    pass


a_cat = Cat()
another_cat = Cat()

a_cat.age = 3
a_cat.name = "Mr. Fuzzybuttons"
a_cat.namesis = another_cat
print(a_cat.age)
print(a_cat.name)
print(a_cat.namesis)

# error
try:
    print(a_cat.namesis.name)
except Exception as err:
    print(err)
    pass

a_cat.namesis.name = "Mr. Bigglesworth"
print(a_cat.namesis.name)
