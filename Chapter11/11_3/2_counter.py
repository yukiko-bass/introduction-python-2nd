from collections import Counter


breakfast = ["spam", "spam", "eggs", "spam"]
breakfast_counter = Counter(breakfast)
print(breakfast_counter)

print("-----")
print(breakfast_counter.most_common())
print(breakfast_counter.most_common(1))

print("-----")
lunch = ["eggs", "eggs", "bacon"]
lunch_counter = Counter(lunch)
print(lunch_counter)

print("-----")
print(breakfast_counter + lunch_counter)
print(breakfast_counter - lunch_counter)
print(lunch_counter - breakfast_counter)

print("-----")
# 積集合
print(breakfast_counter & lunch_counter)
# 和集合（カウンタを加算せずに大きい方のカウンタ値を採用する）
print(breakfast_counter | lunch_counter)
