# <comp> ::= (<op> <comp op> <op>)

import sys
from scanner import Scanner
from op import Op
from comp_op import CompOp


class Comp:
    def __init__(self):
        self.left: Op = None
        self.comp_op: CompOp = None
        self.right: Op = None

    def parse(self, scanner: Scanner):
        if scanner.getToken() != 20:  # (
            print("Error, expecting (")
            sys.exit(1)
        scanner.skipToken()
        self.left = Op()
        self.left.parse(scanner)
        self.comp_op = CompOp()
        self.comp_op.parse(scanner)
        self.right = Op()
        self.right.parse(scanner)
        if scanner.getToken() != 21:  # )
            print("Error, expecting (")
            sys.exit(1)
        scanner.skipToken()

    def print_comp(self, indent=0):
        print("(", end="")
        self.left.print_op()
        print(" ", end="")
        self.comp_op.print_comp_op()
        print(" ", end="")
        self.right.print_op()
        print(")", end="")

    def execute(self):
        return self.comp_op.compare(self.left.execute(), self.right.execute())
