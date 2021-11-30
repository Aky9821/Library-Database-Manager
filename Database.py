import sqlite3


def connectToDatabase():
    connection = sqlite3.connect("Books.db")
    cur = connection.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS 'Book' (ISBN VARCHAR(13) PRIMARY KEY, Title varchar(255),Author varchar(255), "
        "Year INTEGER(10), Publisher varchar(255)) ")

    # sqlFile = open("BX-Books.sql")
    # sqlAsString = sqlFile.read()
    # cur.executescript(sqlAsString)
    # cur.execute("ALTER TABLE 'Bx-Books' RENAME TO Book")

    connection.commit()
    connection.close()


def insert(title, author, year, ISBN):
    connection = sqlite3.connect("Books.db")
    cur = connection.cursor()
    cur.execute("INSERT INTO Book VALUES(?,?,?,?,'')", (ISBN, title, author, year))
    connection.commit()
    connection.close()


def search(title="", author="", year="", ISBN=""):
    title = '%' + title + '%'
    author = '%' + author + '%'
    year = '%' + year + '%'
    ISBN = '%' + ISBN + '%'
    connection = sqlite3.connect("Books.db")
    cur = connection.cursor()

    if title != "" and author != "" and year != "" and ISBN != "":
        cur.execute(
            "SELECT * FROM Book WHERE UPPER(title)LIKE ? AND UPPER(author) LIKE ? AND year LIKE ? AND ISBN LIKE?",
            (title, author, year, ISBN))
    elif (
            title != "" and author == "" and year == "" and ISBN == "") or (
            title == "" and author != "" and year == "" and ISBN == "") or (
            title == "" and author == "" and year != "" and ISBN == "") or (
            title == "" and author == "" and year == "" and ISBN != ""):
        cur.execute(
            "SELECT * FROM Book WHERE UPPER(title) LIKE ? OR UPPER(author) LIKE ? OR year LIKE ? OR ISBN LIKE ?",
            (title, author, year, ISBN) )
    elif title != "" and author != "" and year == "" and ISBN == "":
        cur.execute("SELECT * FROM Book WHERE UPPER(title) LIKE ? AND UPPER(author) LIKE ? ", (title, author))
    elif title != "" and author == "" and year != "" and ISBN == "":
        cur.execute("SELECT * FROM Book WHERE UPPER(title) LIKE ?  AND year LIKE?", (title, year))
    elif title != "" and author == "" and year == "" and ISBN != "":
        cur.execute("SELECT * FROM Book WHERE UPPER(title) LIKE ? AND ISBN LIKE ?", (title, ISBN))
    elif title == "" and author != "" and year != "" and ISBN == "":
        cur.execute("SELECT * FROM Book WHERE UPPER(author)LIKE ? AND year LIKE ? ", (author, year))
    elif title == "" and author != "" and year == "" and ISBN != "":
        cur.execute("SELECT * FROM Book WHERE  UPPER(author) LIKE ? AND ISBN LIKE ?", (author, ISBN))
    elif title == "" and author == "" and year != "" and ISBN != "":
        cur.execute("SELECT * FROM Book WHERE year LIKE ? AND ISBN LIKE ?", (year, ISBN))
    elif title != "" and author != "" and year != "" and ISBN == "":
        cur.execute("SELECT * FROM Book WHERE UPPER(title) LIKE ? AND UPPER(author) LIKE ? AND year LIKE ?",
                    (title, author, year))
    elif title != "" and author != "" and year == "" and ISBN != "":
        cur.execute("SELECT * FROM Book WHERE UPPER(title) LIKE ? AND UPPER(author) LIKE ?  AND ISBN LIKE ?",
                    (title, author, ISBN))
    elif title != "" and author == "" and year != "" and ISBN != "":
        cur.execute("SELECT * FROM Book WHERE UPPER(title) LIKE ?  AND year LIKE ? AND ISBN LIKE ?",
                    (title, year, ISBN))
    elif title == "" and author != "" and year != "" and ISBN != "":
        cur.execute("SELECT * FROM Book WHERE UPPER(author) LIKE ? AND year LIKE ? AND ISBN LIKE ?",
                    (author, year, ISBN))
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


def delete(ISBN):
    connection = sqlite3.connect("Books.db")
    cur = connection.cursor()
    cur.execute("DELETE FROM book where ISBN=?", (ISBN,))
    connection.commit()
    connection.close()


def update(title, author, year, ISBNnew, ISBNold):
    connection = sqlite3.connect("Books.db")
    cur = connection.cursor()
    cur.execute("UPDATE Book SET title=?, author=?,year=?,ISBN=? WHERE ISBN=?", (title, author, year, ISBNnew, ISBNold))
    connection.commit()
    connection.close()


connectToDatabase()
