class Num:
    def __init__(self, value):
        self.value = value

    def print_visit(self, visitor):
        visitor.visit_num(self)

    def calc_visit(self, visitor):
        return visitor.visit_num(self)


class Add:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def print_visit(self, visitor):
        visitor.visit_add(self)

    def calc_visit(self, visitor):
        return visitor.visit_add(self)


class Mul:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def print_visit(self, visitor):
        visitor.visit_mul(self)

    def calc_visit(self, visitor):
        return visitor.visit_mul(self)


class PrintVisitor:
    def visit_num(self, num):
        print(num.value, end='')

    def visit_add(self, add):
        print('(', end='')
        add.left.print_visit(self)
        print(' + ', end='')
        add.right.print_visit(self)
        print(')', end='')

    def visit_mul(self, mul):
        print('(', end='')
        mul.left.print_visit(self)
        print(' * ', end='')
        mul.right.print_visit(self)
        print(')', end='')


class CalcVisitor:
    def visit_num(self, num):
        return num.value

    def visit_add(self, add):
        return add.left.calc_visit(self) + add.right.calc_visit(self)

    def visit_mul(self, mul):
        return mul.left.calc_visit(self) * mul.right.calc_visit(self)


class StackVisitor:
    def visit_num(self, num):
        print('PUSH', num.value)

    def visit_add(self, add):
        add.left.calc_visit(self)
        add.right.calc_visit(self)
        print('ADD')

    def visit_mul(self, mul):
        mul.left.calc_visit(self)
        mul.right.calc_visit(self)
        print('MUL')


ast = Add(Num(7), Mul(Num(3), Num(2)))

print("Print visitor")
printVisitor = PrintVisitor()
ast.print_visit(printVisitor)
print()
print()

print("Calc visitor")
calcVisitor = CalcVisitor()
print(ast.calc_visit(calcVisitor))
print()

print("Stack visitor")
stackVisitor = StackVisitor()
print(ast.calc_visit(stackVisitor))
