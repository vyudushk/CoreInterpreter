# <assign> ::= <id> = <exp>;

import sys
from id import Id
from exp import Exp
from scanner import Scanner


class Assign:
    def __init__(self):
        self.id: Id = None
        self.exp: Exp = None

    def parse(self, scanner: Scanner):
        self.id = Id.parse(scanner)
        self.id.check_declared()
        scanner.skipToken()

        if scanner.getToken() != 14:  # must be =
            print("Error expected =")
            sys.exit(1)
        scanner.skipToken()
        self.exp = Exp()
        self.exp.parse(scanner)

        if scanner.getToken() != 12:  # must be ;
            print("Error expected ;")
            sys.exit(1)
        scanner.skipToken()

    def print_assign(self, indent=0):
        print("    " * indent, end="")
        self.id.print_name()
        print(" = ", end="")
        self.exp.print_exp()
        print(";")

    def execute(self):
        self.id.set_value(self.exp.execute())
