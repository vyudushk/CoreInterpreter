# <out> ::= write <id list>;


import sys
from scanner import Scanner
from id_list import IdList


class Out:
    def __init__(self):
        self.id_list: IdList = None

    def parse(self, scanner: Scanner):
        if scanner.getToken() != 11:  # write
            print("Error, expected write token")
            sys.exit(1)

        scanner.skipToken()
        self.id_list = IdList()
        self.id_list.parse(scanner)

        if scanner.getToken() != 12:  # ;
            print("Error, expected ; after write")
            sys.exit(1)
        scanner.skipToken()

    def print_out(self, indent=0):
        print("    " * indent + "write ", end="")
        self.id_list.print_idlist()
        print(";")

    def execute(self, data_file):
        self.id_list.write_all()
