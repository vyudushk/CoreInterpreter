import sys
from scanner import Scanner
from prog import Prog


def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <program_file> <data_file>")
        sys.exit(1)

    program_file = sys.argv[1]
    data_file = sys.argv[2]

    try:
        scanner = Scanner(program_file)
        program = Prog()
        program.parse(scanner)
        if scanner.getToken() != 33:  # We are not at end of file, wrong
            print(f"Not at EOF, instead at {scanner.getToken()}")
            sys.exit(1)
        program.print_program()
        program.execute(data_file)

    except FileNotFoundError as e:
        print(f"ERROR: File not found - {e}")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
