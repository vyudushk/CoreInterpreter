# <in> ::= read <id list>

import sys
from scanner import Scanner
from id_list import IdList


class In:
    def __init__(self):
        self.id_list: IdList = None

    def parse(self, scanner: Scanner):
        if scanner.getToken() != 10:  # read
            print("Error, expected read token")
            sys.exit(1)

        scanner.skipToken()
        self.id_list = IdList()
        self.id_list.parse(scanner)

        if scanner.getToken() != 12:  # ;
            print("Error, expected ; after read")
            sys.exit(1)
        scanner.skipToken()

    def print_in(self, indent=0):
        print("    " * indent + "read ", end="")
        self.id_list.print_idlist()
        print(";")

    def execute(self, data_file):
        self.id_list.read_all(data_file)
