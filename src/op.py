from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from exp import Exp

import sys
from id import Id
from scanner import Scanner

# <op> ::= <int> | <id> | (<exp>)


class Op:
    def __init__(self):
        self.alt = 0
        self.int_val: int = None  # for 1
        self.id: Id = None  # for 2
        self.exp: Exp = None  # for 3

    def parse(self, scanner: Scanner):
        token = scanner.getToken()

        if token == 31:  # integer
            self.alt = 1
            self.int_val = scanner.intVal()
            scanner.skipToken()
        elif token == 32:  # variable
            self.alt = 2
            self.id = Id.parse(scanner)
            self.id.check_declared()
            scanner.skipToken()
        elif token == 20:  # ( exp )
            self.alt = 3
            scanner.skipToken()
            from exp import Exp

            self.exp = Exp()
            self.exp.parse(scanner)
            if scanner.getToken() != 21:  # )
                print("Error, expected )")
                sys.exit(1)
            scanner.skipToken()

        else:
            print("Expected <op>, got token " + str(token))
            sys.exit(1)

    def print_op(self):
        if self.alt == 1:
            print(str(self.int_val), end="")

        if self.alt == 2:
            self.id.print_name()

        if self.alt == 3:
            print("(" + self.exp.print_exp() + ")", end="")

    def execute(self):
        if self.alt == 1:
            return self.int_val
        elif self.alt == 2:
            return self.id.get_value()
        elif self.alt == 3:
            return self.exp.execute()
        else:
            print("invalid op.alt " + str(self.alt))
            sys.exit(1)
