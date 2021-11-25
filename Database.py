import sqlite3


def connectToDatabase():
    connection = sqlite3.connect("Books.db")
    cur = connection.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS Book(SNo INTEGER PRIMARY KEY, Title VARCHAR, Author  VARCHAR, Year INTEGER, "
        "UID INTEGER UNIQUE)")
    connection.commit()
    connection.close()


def insert(title, author, year, UID):
    connection = sqlite3.connect("Books.db")
    cur = connection.cursor()
    cur.execute("INSERT INTO Book VALUES(NULL,?,?,?,?)", (title, author, year, UID))
    connection.commit()
    connection.close()


def search(title="", author="", year="", UID=""):
    connection = sqlite3.connect("Books.db")
    cur = connection.cursor()

    if title != "" and author != "" and year != "" and UID != "":
        cur.execute("SELECT * FROM Book WHERE title=? AND author=? AND year=? AND UID=?", (title, author, year, UID))
    elif (
            title != "" and author == "" and year == "" and UID == "") or (
            title == "" and author != "" and year == "" and UID == "") or (
            title == "" and author == "" and year != "" and UID == "") or (
            title == "" and author == "" and year == "" and UID != ""):
        cur.execute("SELECT * FROM Book WHERE title=? OR author=? OR year=? OR UID=?", (title, author, year, UID))
    elif title != "" and author != "" and year == "" and UID == "":
        cur.execute("SELECT * FROM Book WHERE title=? AND author=? ", (title, author))
    elif title != "" and author == "" and year != "" and UID == "":
        cur.execute("SELECT * FROM Book WHERE title=?  AND year=?", (title, year))
    elif title != "" and author == "" and year == "" and UID != "":
        cur.execute("SELECT * FROM Book WHERE title=? AND UID=?", (title, UID))
    elif title == "" and author != "" and year != "" and UID == "":
        cur.execute("SELECT * FROM Book WHERE author=? AND year=? ", (author, year))
    elif title == "" and author != "" and year == "" and UID != "":
        cur.execute("SELECT * FROM Book WHERE  author=? AND UID=?", (author, UID))
    elif title == "" and author == "" and year != "" and UID != "":
        cur.execute("SELECT * FROM Book WHERE year=? AND UID=?", (year, UID))
    elif title != "" and author != "" and year != "" and UID == "":
        cur.execute("SELECT * FROM Book WHERE title=? AND author=? AND year=?", (title, author, year))
    elif title != "" and author != "" and year == "" and UID != "":
        cur.execute("SELECT * FROM Book WHERE title=? AND author=?  AND UID=?", (title, author, UID))
    elif title != "" and author == "" and year != "" and UID != "":
        cur.execute("SELECT * FROM Book WHERE title=?  AND year=? AND UID=?", (title, year, UID))
    elif title == "" and author != "" and year != "" and UID != "":
        cur.execute("SELECT * FROM Book WHERE author=? AND year=? AND UID=?", (author, year, UID))
    rows = cur.fetchall()
    connection.close()
    return rows


def viewAll():
    connection = sqlite3.connect("Books.db")
    cur = connection.cursor()
    cur.execute("SELECT * FROM Book")
    rows = cur.fetchall()
    connection.close()
    return rows


def delete(SNo):
    connection = sqlite3.connect("Books.db")
    cur = connection.cursor()
    cur.execute("DELETE FROM book where SNo=?", (SNo,))
    connection.commit()
    connection.close()


def update(SNo, title, author, year, UID):
    connection = sqlite3.connect("Books.db")
    cur = connection.cursor()
    cur.execute("UPDATE Book SET title=?, author=?,year=?,UID=? WHERE SNo=?", (title, author, year, UID, SNo))
    connection.commit()
    connection.close()


connectToDatabase()
delete(6)
'''print(search(year=2000, UID=5678, title='Six of crows'))
print(viewAll())
delete(4)

print(viewAll())
'''
