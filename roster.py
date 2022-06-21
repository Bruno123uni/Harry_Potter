from sys import argv, exit
from cs50 import SQL

db = SQL("sqlite:///students.db")

if len(argv) != 2:
    print("Incorrect input")
    exit(1)
else:
    houst = argv[1]
    dictq = db.execute("SELECT first, middle, last, birth FROM students WHERE house = ? ORDER BY last", houst)
    for row in dictq:
        if row["middle"] == None:
            print(row["first"], end=" ")
            print(row["last"], end="")
            print(", born", end=" ")
            print(row["birth"])
        else:
            print(row["first"], end=" ")
            print(row["middle"], end=" ")
            print(row["last"], end="")
            print(", born", end=" ")
            print(row["birth"])
            