class Word:
    def __init__(self, text):
        self.text = text

    def equals(self, word2):
        return self.text.lower() == word2.text.lower()


first = Word("ha")
second = Word("HA")
third = Word("eh")

# True
print(first.equals(second))
# False
print(first.equals(third))

print("-----")


class Word2:
    def __init__(self, text):
        self.text = text

    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()

    def __str__(self):
        return self.text

    def __repr__(self):
        return 'Word("' + self.text + '")'


first2 = Word2("ha")
second2 = Word2("HA")
third2 = Word2("eh")

# True
print(first2 == second2)
# False
print(first2 == third2)

print("-----")

first3 = Word2("ha")
print(first3.__repr__())
print(first3)
