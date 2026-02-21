"""
Jalen Banks
Feb 19, 2026
Lab 7, working with data in Python
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def p(filename):
    return BASE_DIR / filename

print("\n----- Example 1: Read file ----- ")
with open(p("phrases.txt"), "r") as file1:
    filecontent = file1.read(30)
    print(filecontent)
    filecontent = file1.read(5)
    print(filecontent)

# Check if the file is closed.
print(f"Is the file closed? {file1.closed}")


print("\n----- Example 2: Readline file ----- ")
with open(p("phrases.txt"), "r") as file1:
    filecontent = file1.readline(30)
    print(filecontent)
    filecontent = file1.readline(5)
    print(filecontent)


print("\n----- Example 3: Readlines file ----- ")
# Readlines makes a list of all the lines in the text file. Each line is an item in the list.
with open(p("phrases.txt"), "r") as file1:
    filecontent = file1.readlines()
    print(filecontent)
    filecontent = file1.readlines(5)
    print(filecontent)


print("\n----- Example 4: Loop through each line in a file ----- ")
# Readlines makes a list of all the lines in the text file. Each line is an item in the list.
with open(p("phrases.txt"), "r") as file1:
    filecontent = file1.readlines()
    for eachline in filecontent:
        print(eachline.strip())     # strip() method removes \n in each line.


print("\n----- Example 5: Create file ----- ")
# "W" mode creates a file if the file doesn't exist. On the other hand, if the file exists, "W" mode will overwrite the data in the file.
with open(p("Banks.txt"), "w") as file:
    file.write("Python basics for data science\n")
    file.write("Jalen Banks")
    

print("\n----- Example 6: Append data to an existing file ----- ")
# Append the date and time into "Banks.txt" file
from datetime import datetime
with open(p("Banks.txt"), "a") as file:
    file.write(f"\nLast update: {datetime.now()}")


print("\n----- Example 7: Copy a file ----- ")
# Copy file "Banks.txt" into a new file
with open(p("Banks.txt"), "r") as readfile:
    with open(p("newfile.txt"), "w") as writefile:
        for eachline in readfile:
            writefile.write(eachline)


print("\n----- Example 8: Pandas a file ----- ")
try:
    import pandas as pd

    data = {
        'Name' : ['Alice', 'Bob', 'Charlie'],
        'Age'  : [25, 30, 35] 
    }
    df = pd.DataFrame(data)
    print(df)
except ModuleNotFoundError:
    print("Skipping pandas examples because 'pandas' is not installed.")


print("\n----- Example 9: Creating df with pandas from an excel file ----- ")
try:
    df = pd.read_excel(p("classdata.xlsx"))
    print(df)
    print(df.head())
except NameError:
    print("Skipping Excel example because pandas is not available.")
except ModuleNotFoundError:
    print("Skipping Excel example because an Excel dependency is missing.")



print("\n----- EXERCISE ----- ")
def email_read(filename):
    gmail_count = 0
    yahoo_count = 0
    hotmail_count = 0
    
    try:
        with open(p(filename), "r") as file:
            lines = file.readlines()
            for line in lines:
                line = line.lower()
                if "gmail" in line:
                    gmail_count += 1
                if "yahoo" in line:
                    yahoo_count += 1
                if "hotmail" in line:
                    hotmail_count += 1

        
        with open(p("reportemail.txt"), "w") as email:
            email.write(f"gmail  : {gmail_count}\n")
            email.write(f"yahoo  : {yahoo_count}\n")
            email.write(f"hotmail: {hotmail_count}\n")

            print(f"gmail   = {gmail_count}")
            print(f"yahoo   = {yahoo_count}")
            print(f"hotmail = {hotmail_count}")

        return gmail_count, yahoo_count, hotmail_count
    
    except FileNotFoundError:
        print("Error: The file was not found")

email_read("user_email.txt")