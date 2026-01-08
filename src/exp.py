# <exp> ::= <fac> | <fac> + <exp> | <fac> - <exp>

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from fac import Fac

from scanner import Scanner


class Exp:
    def __init__(self):
        self.alt: int = 0
        self.fac: Fac = None  # for all
        self.exp: Exp = None  # for 2 and 3

    def parse(self, scanner: Scanner):
        from fac import Fac

        self.fac = Fac()
        self.fac.parse(scanner)

        token = scanner.getToken()
        if token == 22:  # for +
            self.alt = 2
            scanner.skipToken()
            self.exp = Exp()
            self.exp.parse(scanner)
        elif token == 23:  # for -
            self.alt = 3
            scanner.skipToken()
            self.exp = Exp()
            self.exp.parse(scanner)
        else:
            self.alt = 1  # for just a <fac>

    def print_exp(self):
        self.fac.print_fac()

        if self.alt == 2:
            print(" + ", end="")
            self.exp.print_exp()
        elif self.alt == 3:
            print(" - ", end="")
            self.exp.print_exp()

    def execute(self):
        if self.alt == 1:
            return self.fac.execute()
        elif self.alt == 2:
            return self.fac.execute() + self.exp.execute()
        elif self.alt == 3:
            return self.fac.execute() - self.exp.execute()
