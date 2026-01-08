# <fac> ::= <op> | <op> * <fac>


from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from op import Op


class Fac:
    def __init__(self):
        self.alt: int = 0
        self.op: Op = None  # for both
        self.fac: Fac = None  # for alt 2

    def parse(self, scanner):
        from op import Op

        self.op = Op()
        self.op.parse(scanner)

        # then we check if it is alt 2
        if scanner.getToken() == 24:  # for *
            self.alt = 2
            scanner.skipToken()
            self.fac = Fac()
            self.fac.parse(scanner)
        else:
            self.alt = 1

    def print_fac(self):
        if self.alt == 1:
            self.op.print_op()
        if self.alt == 2:
            self.op.print_op()
            print("*", end="")
            self.fac.print_fac()

    def execute(self):
        if self.alt == 1:
            return self.op.execute()
        else:
            return self.op.execute() * self.fac.execute()
