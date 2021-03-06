import operator

SUCCESS_MESSAGE = 'Balanced string'
UNSUCCESS_MESSAGE = 'Not balanced string'


class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        try:
            return self.stack.pop()
        except IndexError:
            return

    def push(self, value=None):  # pragma no mutate
        return self.stack.append(value)

    def peek(self):
        return self.stack[-1] if self.stack else None


class ReverseStack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        try:
            first = self.stack[0]
        except IndexError:
            return

        self.stack = self.stack[1:]
        return first

    def push(self, value=None):  # pragma no mutate
        self.stack = [value] + self.stack

    def peek(self):
        return self.stack[0] if self.stack else None


def validate_parentheses(string):
    stack = Stack()

    for char in string:
        if char == '(':
            stack.push()
        elif char == ')' and stack.size():
            stack.pop()
        else:
            return UNSUCCESS_MESSAGE

    if stack.size() > 0:
        return UNSUCCESS_MESSAGE

    return SUCCESS_MESSAGE


OPERATOR = {
    '+': operator.add,
    '-': operator.sub,
    '/': operator.truediv,
    '*': operator.mul,
}


def postfix_count(string):
    stack_one = ReverseStack()
    stack_two = ReverseStack()

    # Fill stack_one:
    stack_one.stack = string.split(' ')

    while stack_one.size():
        element = stack_one.pop()
        if element in OPERATOR:
            previous_element = stack_two.pop()
            stack_two.push(
                OPERATOR.get(element)(
                    stack_two.pop(),
                    previous_element,
                ),
            )
        elif element == '=':
            return stack_two.pop()
        else:
            stack_two.push(int(element))
