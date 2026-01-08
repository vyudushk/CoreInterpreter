# <prog> ::= program <decl seq> begin <stmt seq> end

from declseq import DeclSeq
from stmt_seq import StmtSeq
from scanner import Scanner
import sys


class Prog:
    def __init__(self):
        self.decl_seq: DeclSeq = None
        self.stmt_seq: StmtSeq = None

    def parse(self, scanner: Scanner):
        if scanner.getToken() != 1:  # program
            print("Error: Expected program")
            sys.exit(1)
        scanner.skipToken()
        self.decl_seq = DeclSeq()
        self.decl_seq.parse(scanner)
        if scanner.getToken() != 2:  # begin
            print(f"ERROR: Expected 'begin', got token {scanner.getToken()}")
            sys.exit(1)
        scanner.skipToken()
        self.stmt_seq = StmtSeq()
        self.stmt_seq.parse(scanner)
        if scanner.getToken() != 3:  # end
            print("Error: Expected end")
            sys.exit(1)
        scanner.skipToken()

    def print_program(self):
        print("program")
        self.decl_seq.print_declseq(indent=1)
        print("begin")
        self.stmt_seq.print_stmt_seq(indent=1)
        print("end")

    def execute(self, data_filename):
        try:
            data_file = open(data_filename, "r")
            self.stmt_seq.execute(data_file)
            data_file.close()
        except FileNotFoundError:
            print("Data file: " + data_filename + " not found")
            sys.exit(1)
        except Exception as e:
            print(f"Error executing {e}")
            sys.exit(1)
