# <decl> ::= int <id list>;

import sys
from id_list import IdList
from scanner import Scanner


class Decl:
    def __init__(self):
        self.id_list: IdList = None  # no alts

    def parse(self, scanner: Scanner):
        if scanner.getToken() != 4:  # this is int
            print("Error: expected 'int' ")
            sys.exit(1)

        scanner.skipToken()
        self.id_list = IdList()
        self.id_list.parse(scanner)
        self.id_list.declare_all()

        if scanner.getToken() != 12:  # this is ;
            print("Error: expected ';' ")
            sys.exit(1)
        scanner.skipToken()

    def print_decl(self, indent):
        print("    " * indent + "int ", end="")
        self.id_list.print_idlist()
        print(";")
