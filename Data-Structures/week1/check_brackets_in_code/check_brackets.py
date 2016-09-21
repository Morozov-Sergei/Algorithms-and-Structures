# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
    #text = sys.stdin.read()

    def bracket_check(text):
        opening_brackets_stack = []
        for i, next in enumerate(text):
            if next == '(' or next == '[' or next == '{':
                # Process opening bracket, write your code here
                opening_brackets_stack.append(Bracket(next,i))
            elif next == ')' or next == ']' or next == '}':
                # Process closing bracket, write your code here
                if not len(opening_brackets_stack):
                    return i + 1
                last = opening_brackets_stack.pop()
                if not last.Match(next):
                    return i+1
        if len(opening_brackets_stack):
            return opening_brackets_stack.pop().position+1
        else:
            return 'Success'

    def test():
        assert(bracket_check('}') == 1)
        assert(bracket_check('{}[]') == 'Success')
        assert(bracket_check('[()]') == 'Success')
        assert(bracket_check('(())') == 'Success')
        assert(bracket_check('{[]}()') == 'Success')
        assert(bracket_check('{') == 1)
        assert(bracket_check('{[}') == 3)
        assert(bracket_check('foo(bar);') == 'Success')
        assert(bracket_check('foo(bar[i);') == 10)
    #test()
    print(bracket_check(sys.stdin.read()))
