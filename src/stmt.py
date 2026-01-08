# <stmt> ::= <assign> | <if> | <loop> | <in> | <out>

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from assign import Assign
    from if_stmt import If
    from loop import Loop
    from in_stmt import In
    from out import Out

import sys
from scanner import Scanner


class Stmt:
    def __init__(self):
        self.alt: int = None
        self.assign: Assign = None  # alt 1
        self.if_stmt: If = None  # alt 2
        self.loop: Loop = None  # alt 3
        self.in_stmt: In = None  # alt 4
        self.out: Out = None  # alt 5

    def parse(self, scanner: Scanner):
        token = scanner.getToken()

        if token == 32:  # is an identifier
            self.alt = 1

            from assign import Assign

            self.assign = Assign()
            self.assign.parse(scanner)
        elif token == 5:  # if
            self.alt = 2
            from if_stmt import If

            self.if_stmt = If()
            self.if_stmt.parse(scanner)
        elif token == 8:  # while
            self.alt = 3
            from loop import Loop

            self.loop = Loop()
            self.loop.parse(scanner)
        elif token == 10:  # read
            self.alt = 4
            from in_stmt import In

            self.in_stmt = In()
            self.in_stmt.parse(scanner)
        elif token == 11:  # write
            self.alt = 5
            from out import Out

            self.out = Out()
            self.out.parse(scanner)
        else:
            print("Got unexpected token" + str(token))
            sys.exit(1)

    def print_stmt(self, indent=0):
        if self.alt == 1:
            self.assign.print_assign(indent)
        elif self.alt == 2:
            self.if_stmt.print_if(indent)
        elif self.alt == 3:
            self.loop.print_loop(indent)
        elif self.alt == 4:
            self.in_stmt.print_in(indent)
        elif self.alt == 5:
            self.out.print_out(indent)

    def execute(self, data_file):
        if self.alt == 1:
            self.assign.execute()
        elif self.alt == 2:
            self.if_stmt.execute(data_file)
        elif self.alt == 3:
            self.loop.execute(data_file)
        elif self.alt == 4:
            self.in_stmt.execute(data_file)
        elif self.alt == 5:
            self.out.execute(data_file)
