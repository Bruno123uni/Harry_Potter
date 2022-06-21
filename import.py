import csv
from sys import argv, exit
from cs50 import SQL

open("students.db", "w").close()
db = SQL("sqlite:///students.db")
db.execute("CREATE TABLE students (first TEXT, middle TEXT, last TEXT, house TEXT, birth NUMERIC)")
if len(argv) != 2:
    print("Incorrect input")
    exit(1)
else:
    with open(argv[1], newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            txt = row["name"]
            nam = txt.split(" ")
            firstname = nam[0]
            if len(nam) == 2:
                lastnam = nam[1]
                middlesnam = None
            else:
                lastnam = nam[2]
                middlesnam = nam[1]
            house = row["house"]
            birth = row["birth"]
            db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)",
                       firstname, middlesnam, lastnam, house, birth)