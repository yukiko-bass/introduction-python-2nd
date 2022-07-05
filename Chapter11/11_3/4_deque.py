# deque (デック：両端キュー)
# スタックとキューの両方の機能を持つ

from collections import deque


# 回文チェックをする
def palindrome(word):
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True


print(palindrome("a"))
print(palindrome("racecar"))
print(palindrome(""))
print(palindrome("radar"))
print(palindrome("halibut"))

print("-----")


def another_palindrome(word):
    # [::-1] で逆順の文字列を作っている（スライス）
    return word == word[::-1]


print(palindrome("radar"))
print(palindrome("halibut"))
