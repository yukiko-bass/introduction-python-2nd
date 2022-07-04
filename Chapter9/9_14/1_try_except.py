short_list = [1, 2, 3]

position = 5

try:
    short_list[position]
except Exception:
    print("Need a position between 0 and", len(short_list) - 1, " but got", position)

while True:
    value = input("Position [q to quit]? ")
    if value == "q":
        break
    try:
        position = int(value)
        print(short_list[position])
    except IndexError:
        print("Bad index:", position)
    except Exception as other:
        print("Something else broke:", other)
