import sys
from typing import TextIO

words_and_symbols = [
    "program",
    "begin",
    "end",
    "int",
    "if",
    "then",
    "else",
    "while",
    "loop",
    "read",
    "write",
    ";",
    ",",
    "=",
    "!",
    "[",
    "]",
    "&&",
    "||",
    "(",
    ")",
    "+",
    "-",
    "*",
    "!=",
    "==",
    "<",
    ">",
    "<=",
    ">=",
]

reserved_word_start = {
    "p",
    "b",
    "e",
    "i",
    "t",
    "w",
    "l",
    "r",
}

special_symbol_start = {
    ";",
    ",",
    "=",
    "!",
    "[",
    "]",
    "&",
    "|",
    "(",
    ")",
    "+",
    "-",
    "*",
    "<",
    ">",
}


class Scanner:
    """Opens and scans a file per the CORE language specifications.

    This class provides a scanner object:
    - getToken: returns current token
    - skipToken: progresses cursor to next token
    - intVal: integer value of current token
    - idName: id of current token
    """

    def __init__(self, filename: str):
        self.filename: str = filename
        self.file: TextIO = open(filename, "r")
        self.tokens: list[int] = []
        self.token_symbols: list[str] = []
        self.cursor: int = 0
        self._tokenizeLine()

    def __del__(self) -> None:
        if hasattr(self, "file") and not self.file.closed:
            self.file.close()

    def getToken(self) -> int:
        return self.tokens[self.cursor]

    def skipToken(self) -> None:
        self.cursor += 1
        if (
            self.cursor == len(self.tokens)
            and 34 not in self.tokens
            and 33 not in self.tokens
        ):
            self._tokenizeLine()

    def _current_token(self) -> str:
        return self.token_symbols[self.cursor]

    def intVal(self):
        if self.getToken() == 31:
            return int(self._current_token())
        print("intVal called on non-integer Token")
        sys.exit(1)

    def idName(self) -> str:
        if self.getToken() == 32:
            return self._current_token()
        print("idName called on non-identifier Token")
        sys.exit(1)

    def _tokenizeLine(self):
        self.tokens = []
        self.token_symbols = []
        self.cursor = 0
        line: str = self.file.readline()

        while line == "\n":
            line = self.file.readline()
        if line == "":
            self.tokens.append(33)
            self.file.close()
            return
        i: int = 0
        word: str
        while i < len(line):
            word = ""
            while i < len(line) and line[i].isspace():
                i += 1
            if i >= len(line):
                break  # end of line
            if line[i] in reserved_word_start:
                while i < len(line) and line[i].islower():
                    word += line[i]
                    i += 1
                if word in words_and_symbols:
                    self.tokens.append(words_and_symbols.index(word) + 1)
                else:
                    self.tokens.append(34)
                    self.file.close()
                    return  # error, stop
            elif line[i] in special_symbol_start:
                if i + 1 < len(line) and (line[i] + line[i + 1] in words_and_symbols):
                    word = line[i] + line[i + 1]
                    self.tokens.append(words_and_symbols.index(word) + 1)
                    i += 2
                else:  # it is a single char special symbol
                    word = line[i]
                    self.tokens.append(words_and_symbols.index(word) + 1)
                    i += 1
            elif line[i].isdigit():
                while i < len(line) and line[i].isdigit():
                    word += line[i]
                    i += 1
                self.tokens.append(31)
            elif line[i].isupper():
                while i < len(line) and (line[i].isupper() or line[i].isdigit()):
                    word += line[i]
                    i += 1
                self.tokens.append(32)
            else:
                self.tokens.append(34)
                self.file.close()
                return  # error, stop
            self.token_symbols.append(word)


def main():
    sc = Scanner(sys.argv[1])

    current_token: int = sc.getToken()
    while current_token != 33 and current_token != 34:
        print(current_token)
        sc.skipToken()
        current_token = sc.getToken()
    print(current_token)


if __name__ == "__main__":
    main()
