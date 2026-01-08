# <comp op> ::= != | == | < | > | <= | >=

import sys
from scanner import Scanner


class CompOp:
    def __init__(self):
        self.alt: int = None
        self.comp_op: int = None

    def parse(self, scanner: Scanner):
        token = scanner.getToken()

        if token < 25 or token > 30:
            print("Was expecting a comp op token")
            sys.exit(1)

        self.comp_op = token
        scanner.skipToken()

    def print_comp_op(self, indent=0):
        if self.comp_op == 25:
            print("!=", end="")
        elif self.comp_op == 26:
            print("==", end="")
        elif self.comp_op == 27:
            print("<", end="")
        elif self.comp_op == 28:
            print(">", end="")
        elif self.comp_op == 29:
            print("<=", end="")
        elif self.comp_op == 30:
            print(">=", end="")

    def compare(self, left, right):
        if self.comp_op == 25:
            return left != right
        elif self.comp_op == 26:
            return left == right
        elif self.comp_op == 27:
            return left < right
        elif self.comp_op == 28:
            return left > right
        elif self.comp_op == 29:
            return left <= right
        elif self.comp_op == 30:
            return left >= right
        else:
            print("Error, invalid comp op token" + str(self.comp_op))
            sys.exit(1)
