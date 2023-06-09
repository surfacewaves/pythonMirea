class Test:
    field1 = 1
    field2 = "as"

    def method1(self):
        print(str(self.field1) + " method1")

    def method2(self):
        print(str(self.field2 + " method2"))


# show all field of class expect service fields and methods
def get_all_fields():
    return [attr for attr in dir(Test) if not callable(getattr(Test, attr)) and not attr.startswith("__")]


def call_function_by_name(func_name):
    c = C()
    return eval("Test()." + func_name + "()")


class A:
    pass


class B(A):
    pass


class C(B):
    pass


# recursivly get all inheritance
def get_inheritance():
    # delete last 3 symbols
    parents = [x.__name__ for x in C.__mro__]
    result = ""
    print("len = ", len(parents))
    for i in range(len(parents)):
        if i != len(parents) - 1:
            result += parents[i] + " -> "
        else:
            result += parents[i]
    return result


def main():
    print(get_all_fields())
    call_function_by_name("method1")
    print(get_inheritance())


if __name__ == '__main__':
    main()
