def answer():
    print(42)


def run_something(func):
    func()


def add_args(arg1, arg2):
    print(arg1 + arg2)


def run_something_with_args(func, arg1, arg2):
    func(arg1, arg2)


def sum_args(*args):
    return sum(args)


def run_with_positioal_args(func, *args):
    return func(*args)


if __name__ == "__main__":
    answer()

    # ()は関数呼び出しを意味する
    # ここではオブジェクトとして呼びたいので、()は無しで。
    run_something(answer)

    type(run_something)

    type(add_args)

    run_something_with_args(add_args, 5, 9)

    print(run_with_positioal_args(sum_args, 1, 2, 3, 4))
