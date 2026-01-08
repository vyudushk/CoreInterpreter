# <id list> ::= <id> | <id>, <id list>

import sys
from id import Id
from scanner import Scanner


class IdList:
    def __init__(self):
        self.alt = 0
        self.id: Id = None  # for all alts
        self.id_list: IdList = None  # for 2

    def parse(self, scanner: Scanner):
        self.id = Id.parse(scanner)
        scanner.skipToken()

        if scanner.getToken() == 13:  # for ,
            self.alt = 2
            scanner.skipToken()
            self.id_list = IdList()
            self.id_list.parse(scanner)
        else:
            self.alt = 1

    def print_idlist(self):
        self.id.print_name()
        if self.alt == 2:
            print(", ", end="")
            self.id_list.print_idlist()

    def declare_all(self):
        self.id.declare()
        if self.alt == 2:
            self.id_list.declare_all()

    def write_all(self):
        print(self.id.get_name() + " = " + str(self.id.get_value()))
        if self.alt == 2:
            self.id_list.write_all()

    def read_all(self, data_file):
        line = data_file.readline().strip()
        if not line:
            print("Error: not enough data in input file")
            sys.exit(1)
        val = int(line)
        self.id.set_value(val)

        if self.alt == 2:
            self.id_list.read_all(data_file)
