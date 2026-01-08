This is just a basic interpretor project I wrote for a class, its nothing crazy but should be evidence of me being half decent at python and programming in general. I'll make this repo public eventually once I start to extend it to compile LLVM IR.

To run the project, the usage is

python3 src/main.py <core source file> <data file>

for example, to run the tests I have provided, run

python3 src/main.py coretests/test1.core testdata/test1.data

This should output something like:
program
    int X;
begin
    X = 5;
    write X;
end
X = 5

Where it pretty prints the source code, and then executes the program, then ouputs any write statements


I took the approach of having a seperate class for each non-terminal, and just call the method for each one.

I did end up calling each class's print something specific, eg .print_stmt() instead of .print()

this was to avoid confusion with python's built in print, there's no real design benefit or rational.
