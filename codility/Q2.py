"""
+
-
POP
DUP
"""


class LackOfElementsException(Exception):
    def __init__(self):
        super().__init__('stack의 크기가 2 이하 입니다.')


class NoElementException(Exception):
    def __init__(self):
        super().__init__('요소가 없습니다.')


class MyStack(object):
    def __init__(self, string):
        self.string = string.split()
        self.stack = []

    def plus(self):
        """
        요소가 1개면 오류 리턴
        """
        if len(self.stack) > 1:
            first = self.stack.pop()
            second = self.stack.pop()
            self.stack.append(first + second)
        else:
            raise LackOfElementsException

    def minus(self):
        """
        요소가 1개면 오류 리턴
        """
        if len(self.stack) > 1:
            first = self.stack.pop()
            second = self.stack.pop()
            self.stack.append(first - second)
        else:
            raise LackOfElementsException

    def push(self, num: int):
        self.stack.append(num)

    def pop(self):
        """
        요소가 없으면 오류 리턴
        """
        if self.stack:
            return self.stack.pop()
        raise NoElementException

    def duplicate(self):
        """
        요소가 없으면 오류 리턴
        """
        if self.stack:
            return self.stack.append(self.stack[-1])
        raise NoElementException

    def result(self):
        try:
            for s in self.string:
                if s == '+':
                    self.plus()
                elif s == '-':
                    self.minus()
                elif s == 'POP':
                    self.pop()
                elif s == 'DUP':
                    self.duplicate()
                else:
                    self.push(int(s))
            return self.stack.pop()
        except (NoElementException, LackOfElementsException):
            return -1


def solution(S):
    my_stack = MyStack(S)
    return my_stack.result()


print(solution("4 5 6 - 7 +"))
print(solution("13 DUP 4 POP 5 DUP + DUP + -"))
print(solution("5 6 + -"))
print(solution("3 DUP 5 - -"))



