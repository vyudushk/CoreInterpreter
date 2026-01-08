# <cond> ::= <comp> | !<cond> | [<cond> && <cond>] | [<cond> || <cond>]

import sys
from scanner import Scanner
from comp import Comp


class Cond:
    def __init__(self):
        self.alt: int = None
        self.comp: Comp = None  # alt 1
        self.cond: Cond = None  # alt 2
        self.left: Cond = None  # left and right are for alt 3 and 4
        self.right: Cond = None

    def parse(self, scanner: Scanner):
        if scanner.getToken() == 20:  # (
            self.alt = 1
            self.comp = Comp()
            self.comp.parse(scanner)
        elif scanner.getToken() == 15:  # !
            self.alt = 2
            self.cond = Cond()
            self.cond.parse(scanner)
        elif scanner.getToken() == 16:  # [
            scanner.skipToken()
            self.left = Cond()
            self.left.parse(scanner)

            if scanner.getToken() == 18:  # &&
                self.alt = 3
            elif scanner.getToken() == 19:  # ||
                self.alt = 4
            else:
                print("Unexpected tokens")
                sys.exit(1)
            scanner.skipToken()

            self.right = Cond()
            self.right.parse(scanner)

            if scanner.getToken() != 17:  # ]
                print("Unexpected tokens")
                sys.exit(1)
            scanner.skipToken()
        else:
            print("Error, Unexpected tokens, wanted conditional")
            sys.exit(1)

    def print_cond(self, indent=0):
        if self.alt == 1:
            self.comp.print_comp()
        elif self.alt == 2:
            print("!", end="")
            self.cond.print_cond()
        elif self.alt == 3:
            print("[", end="")
            self.left.print_cond()
            print(" && ", end="")
            self.right.print_cond()
            print("]", end="")
        elif self.alt == 4:
            print("[", end="")
            self.left.print_cond()
            print(" || ", end="")
            self.right.print_cond()
            print("]", end="")

    def execute(self):
        if self.alt == 1:
            return self.comp.execute()
        elif self.alt == 2:
            return not self.cond.execute()
        elif self.alt == 3:
            return self.left.execute() and self.right.execute()
        elif self.alt == 4:
            return self.left.execute() or self.right.execute()
        else:
            print("Invalid cond")
            sys.exit(1)
