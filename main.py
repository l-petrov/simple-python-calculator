import math


class Node:
    def __init__(self, value, left=None, right=None):
        self.__value = value
        self.__left = left
        self.__right = right

    def get_left(self):
        return self.__left

    def get_right(self):
        return self.__right

    def get_value(self):
        return self.__value

    def set_left(self, node):
        self.__left = node

    def set_right(self, node):
        self.__right = node

    def set_value(self, value):
        self.__value = value


class BinaryTree:
    def __init__(self, root, left=None, right=None):
        self.__root = root
        self.__root.__left = left
        self.__root.__right = right

    def get_root(self):
        return self.__root

    def calc_tree(self):
        calc(self.get_root())


def format_expression(expression):
    expression = expression.replace(' ', '')
    if expression[0] == '-':
        expression = '0' + expression
    for i in range(expression.__len__()):
        if expression[i] == '-' and not expression[i - 1].isdigit():
            expression = expression[:i] + '0' + expression[i:]
    return expression


def build_tree(expression, node):
    node = Node(None)
    for char in ['+', '-', '*', '/', '^', '!', '%', '$', '@', '&']:
        i = expression.find(char)
        if i is not -1:
            node.set_value(char)
            break

    if i is -1:
        node.set_value(expression)
        return node
    node.set_left(build_tree(expression[:i], node.get_left()))
    node.set_right(build_tree(expression[i + 1:], node.get_right()))
    return node


def main():
    expression = raw_input('Enter your expression:\n')
    expression = format_expression(expression)
    root = None
    root = build_tree(expression, root)
    print calc(root)


def is_number(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def calc(node):
    node_value = node.get_value()
    if is_number(node_value):
        return float(node_value)

    if node_value == '+':
        return calc(node.get_left()) + calc(node.get_right())
    elif node_value == '-':
        return calc(node.get_left()) - calc(node.get_right())
    elif node_value == '*':
        return calc(node.get_left()) * calc(node.get_right())
    elif node_value == '/':
        return calc(node.get_left()) / calc(node.get_right())
    elif node_value == '^':
        return calc(node.get_left()) ** calc(node.get_right())
    elif node_value == '%':
        return calc(node.get_left()) % calc(node.get_right())
    elif node_value == '@':
        return (calc(node.get_left()) + calc(node.get_right())) / 2
    elif node_value == '$':
        return max(calc(node.get_left()), calc(node.get_right()))
    elif node_value == '&':
        return min(calc(node.get_left()) & calc(node.get_right()))


main()
