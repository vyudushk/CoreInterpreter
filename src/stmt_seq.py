# <stmt seq> ::= <stmt> | <stmt> <stmt seq>


# import sys
from stmt import Stmt
from scanner import Scanner


class StmtSeq:
    def __init__(self):
        self.alt: int = 0
        self.stmt: Stmt = None
        self.ss: StmtSeq = None

    def parse(self, scanner: Scanner):
        self.stmt = Stmt()
        self.stmt.parse(scanner)

        token = scanner.getToken()
        # many different possible tokens
        if token in [32, 5, 8, 10, 11]:
            self.alt = 2
            self.ss = StmtSeq()
            self.ss.parse(scanner)
        else:
            self.alt = 1

    def print_stmt_seq(self, indent=0):
        self.stmt.print_stmt(indent)
        if self.alt == 2:
            self.ss.print_stmt_seq(indent)

    def execute(self, data_file):
        self.stmt.execute(data_file)
        if self.alt == 2:
            self.ss.execute(data_file)
