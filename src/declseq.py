# <decl seq> ::= <decl> | <decl> <decl seq>

# import sys
from decl import Decl
from scanner import Scanner


class DeclSeq:
    def __init__(self):
        self.alt: int = 0
        self.decl: Decl = None  # for both
        self.decl_seq: DeclSeq = None  # for 2

    def parse(self, scanner: Scanner):
        self.decl = Decl()
        self.decl.parse(scanner)

        if scanner.getToken() == 4:  # for int
            self.alt = 2
            self.decl_seq = DeclSeq()
            self.decl_seq.parse(scanner)
        else:
            self.alt = 1

    def print_declseq(self, indent=0):
        self.decl.print_decl(indent)
        if self.alt == 2:
            self.decl_seq.print_declseq(indent)
