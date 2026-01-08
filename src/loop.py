# <loop> ::= while <cond> loop <stmt seq> end;

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from stmt_seq import StmtSeq

import sys
from cond import Cond
from scanner import Scanner


class Loop:
    def __init__(self):
        self.cond: Cond = None
        self.ss: StmtSeq = None

    def parse(self, scanner: Scanner):
        if scanner.getToken() != 8:  # while
            print("Expected while")
            sys.exit(1)
        scanner.skipToken()

        self.cond = Cond()
        self.cond.parse(scanner)

        if scanner.getToken() != 9:  # loop
            print("Expected loop got: " + str(scanner.getToken()))
            sys.exit(1)
        scanner.skipToken()

        from stmt_seq import StmtSeq

        self.ss = StmtSeq()
        self.ss.parse(scanner)

        if scanner.getToken() != 3:  # end
            print("Expected end")
            sys.exit(1)
        scanner.skipToken()

        # Expect ';'
        if scanner.getToken() != 12:
            print("ERROR: Expected ';' after if statement")
            sys.exit(1)
        scanner.skipToken()

    def print_loop(self, indent=0):
        print("    " * indent + "while ", end="")
        self.cond.print_cond()
        print(" loop")
        self.ss.print_stmt_seq(indent + 1)
        print("    " * indent + "end;")

    def execute(self, data_file):
        while self.cond.execute():
            self.ss.execute(data_file)
