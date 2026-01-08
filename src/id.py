import sys
from scanner import Scanner


class Id:
    _existing_ids = {}

    @staticmethod
    def parse(scanner: Scanner):
        if scanner.getToken() != 32:  # 32 is the token number for identifiers:
            print("Expected identifier, got somethint else: " + str(scanner.getToken()))
            sys.exit(1)

        name = scanner.idName()

        if name in Id._existing_ids:
            return Id._existing_ids[name]
        else:
            new_id = Id(name)
            Id._existing_ids[name] = new_id
            return new_id

    def __init__(self, name):
        self.name = name
        self.declared = False
        self.Initialized = False
        self.value = None

    def declare(self):
        if self.declared:
            print("Error, " + self.name + "is already declared")
            sys.exit(1)
        self.declared = True

    def check_declared(self):
        if not self.declared:
            print("Error: Variable " + self.name + " used but not declared")
            sys.exit(1)

    def set_value(self, val):
        self.value = val
        self.Initialized = True

    def get_value(self):
        if not self.Initialized:
            print("Error, Variable " + self.name + " accessed before being initialized")
            sys.exit(1)
        return self.value

    def get_name(self):
        return self.name

    def print_name(self):
        print(self.name, end="")
