# <if> ::= if <cond> then <stmt seq> end; | if <cond> then <stmt seq> else <stmt seq> end;

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from stmt_seq import StmtSeq

import sys
from cond import Cond
from scanner import Scanner


class If:
    def __init__(self):
        self.alt: int = None
        self.cond: Cond = None
        self.then_ss: StmtSeq = None
        self.else_ss: StmtSeq = None  # for alt 2

    def parse(self, scanner: Scanner):
        if scanner.getToken() != 5:  # if
            print("Expected if")
            sys.exit(1)
        scanner.skipToken()

        self.cond = Cond()
        self.cond.parse(scanner)

        if scanner.getToken() != 6:  # then
            print("Expected then got: " + str(scanner.getToken()))
            sys.exit(1)
        scanner.skipToken()

        from stmt_seq import StmtSeq

        self.then_ss = StmtSeq()
        self.then_ss.parse(scanner)

        if scanner.getToken() == 3:  # end
            self.alt = 1
        elif scanner.getToken() == 7:  # else
            self.alt = 2
            scanner.skipToken()
            self.else_ss = StmtSeq()
            self.else_ss.parse(scanner)
            if scanner.getToken() != 3:  # end
                print("Expected end got: " + str(scanner.getToken()))
                sys.exit(1)
        else:
            print("Unexpected token")
            sys.exit(1)
        scanner.skipToken()

        # Expect ';'
        if scanner.getToken() != 12:
            print("ERROR: Expected ';' after if statement")
            sys.exit(1)
        scanner.skipToken()

    def print_if(self, indent=0):
        print("    " * indent + "if ", end="")
        self.cond.print_cond()
        print(" then")
        self.then_ss.print_stmt_seq(indent + 1)
        if self.alt == 2:
            print("    " * indent + "else")
            self.else_ss.print_stmt_seq(indent + 1)
        print("    " * indent + "end;")

    def execute(self, data_file):
        if self.cond.execute():
            self.then_ss.execute(data_file)
        elif self.alt == 2:
            self.else_ss.execute(data_file)
