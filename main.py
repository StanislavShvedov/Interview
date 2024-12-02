class Stack():
    def __init__(self):
        self.data = []

    def is_empty(self):
        if self.data:
            return False
        else:
            return True

    def push(self, data):
        self.data.append(data)

    def __str__(self):
        print(self.data)

    def pop(self):
        if self.data:
            return self.data.pop()
        else:
            return 'Stack is empty'

    def peek(self):
        return self.data[-1]

    def size(self):
        return len(self.data)


data = '(((([{}]))))'


def check_balance(data):
    stack = Stack()
    pair_symbol = {'(': ')', '[': ']', '{': '}'}
    if len(data) % 2 == 0:
        for symbol in data:
            if stack.is_empty():
                stack.push(symbol)
            elif symbol in pair_symbol.keys():
                stack.push(symbol)
            elif symbol not in pair_symbol.keys() and pair_symbol[stack.peek()] == symbol:
                stack.pop()
        if stack.is_empty():
            result = 'Сбалансированно'
        else:
            result = 'Несбалансированно'
    else:
        result = 'Несбалансированно'
    return result


print(check_balance(data))
