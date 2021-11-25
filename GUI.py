from tkinter import *

import Database


def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb


def viewFunction():
    booklist.delete(0, END)
    # booklist.insert(END, "SNo   Title      Author   Year UID")
    for x in Database.viewAll():
        booklist.insert(END, x)


def searchFunction():
    booklist.delete(0, END)
    flag = 0
    for x in Database.search(title.get(), author.get(), year.get(), UID.get()):
        flag = 1
        booklist.insert(END, x)
    if flag == 0:
        booklist.insert(END, 'Entered Search Not Found!')


def addFunction():
    booklist.delete(0, END)
    flag = 0
    for x in Database.search(UID=UID.get()):
        booklist.insert(END, x)
        flag = 1
    if (title.get() == '' or author.get() == '' or year.get() == '' or UID.get() == ''):
        booklist.insert(END, 'All entries are mandatory and can\'t be left blank!')
    elif flag == 1:
        booklist.insert(END, 'UID already present in database!')
        booklist.insert(END, 'All UID should be unique.')
    else:
        Database.insert(title.get(), author.get(), year.get(), UID.get())
        booklist.delete(0, END)

        searchFunction()
        booklist.insert(END, 'Entry Added!')


window = Tk()
window.title("Book Store")
window.config(bg=rgb_hack((50, 50, 50)))
myFont = ("Consolas", "16", "bold")

labelTitle = Label(window, text="Book Title", width=20, height=2, font=myFont, bg=rgb_hack((50, 50, 50)),
                   fg=rgb_hack((222, 222, 222)))
labelTitle.grid(row=0, column=0, padx=10, pady=10)
labelAuthor = Label(window, text="Author", width=20, height=2, font=myFont, bg=rgb_hack((50, 50, 50)),
                    fg=rgb_hack((222, 222, 222)))
labelAuthor.grid(row=1, column=0, padx=10, pady=10)
labelYear = Label(window, text="Year", width=20, height=2, font=myFont, bg=rgb_hack((50, 50, 50)),
                  fg=rgb_hack((222, 222, 222)))
labelYear.grid(column=0, row=2, padx=10, pady=10)
labelUID = Label(window, text="Unique ID", width=20, height=2, font=myFont, bg=rgb_hack((50, 50, 50)),
                 fg=rgb_hack((222, 222, 222)))
labelUID.grid(column=0, row=3, padx=10, pady=10)

title = StringVar()
entryTitle = Entry(window, textvariable=title, width=20, borderwidth=2, font=myFont, bg=rgb_hack((50, 50, 50)),
                   fg=rgb_hack((222, 222, 222)), relief="ridge")
entryTitle.grid(column=1, row=0, padx=10, pady=10, ipady=11)

author = StringVar()
entryAuthor = Entry(window, textvariable=author, width=20, borderwidth=2, font=myFont, bg=rgb_hack((50, 50, 50)),
                    fg=rgb_hack((222, 222, 222)), relief="ridge")
entryAuthor.grid(column=1, row=1, padx=10, pady=10, ipady=11)

year = StringVar()
entryYear = Entry(window, textvariable=year, width=20, borderwidth=2, font=myFont, bg=rgb_hack((50, 50, 50)),
                  fg=rgb_hack((222, 222, 222)), relief="ridge")
entryYear.grid(column=1, row=2, padx=10, pady=10, ipady=11)

UID = StringVar()
entryUID = Entry(window, textvariable=UID, width=20, borderwidth=2, font=myFont, bg=rgb_hack((50, 50, 50)),
                 fg=rgb_hack((222, 222, 222)), relief="ridge")
entryUID.grid(column=1, row=3, padx=10, pady=10, ipady=11)

booklist = Listbox(window, height=20, width=50, font=myFont, bg=rgb_hack((50, 50, 50)),
                   fg=rgb_hack((217, 217, 217)), borderwidth=2,
                   relief="ridge")
booklist.grid(column=3, row=0, rowspan=6, padx=10, pady=10)

scrollbar = Scrollbar(window, bg=rgb_hack((50, 50, 50)))
scrollbar.grid(column=4, row=0, rowspan=6)
booklist.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=booklist.yview)

buttonViewAll = Button(window, text="View All", width=20, height=2, font=myFont, bg=rgb_hack((50, 50, 50)),
                       fg=rgb_hack((217, 217, 217)), activebackground=rgb_hack((49, 131, 212)), borderwidth=2,
                       relief="ridge", command=viewFunction)
buttonViewAll.grid(column=5, row=0, padx=10, pady=10)

buttonSearchEntry = Button(window, text="Search", width=20, height=2, font=myFont, bg=rgb_hack((50, 50, 50)),
                           fg=rgb_hack((217, 217, 217)), activebackground=rgb_hack((49, 131, 212)), borderwidth=2,
                           relief="ridge", command=searchFunction)
buttonSearchEntry.grid(column=5, row=1, padx=10, pady=10)

buttonAddEntry = Button(window, text="Add", width=20, height=2, font=myFont, bg=rgb_hack((50, 50, 50)),
                        fg=rgb_hack((217, 217, 217)), activebackground=rgb_hack((49, 131, 212)), borderwidth=2,
                        relief="ridge",
                        command=addFunction)
buttonAddEntry.grid(column=5, row=2, padx=10, pady=10)

buttonUpdate = Button(window, text="Update Selected", width=20, height=2, font=myFont, bg=rgb_hack((50, 50, 50)),
                      fg=rgb_hack((217, 217, 217)), activebackground=rgb_hack((49, 131, 212)), borderwidth=2,
                      relief="ridge")
buttonUpdate.grid(column=5, row=3, padx=10, pady=10)

buttonDelete = Button(window, text="Delete Selected", width=20, height=2, font=myFont, bg=rgb_hack((50, 50, 50)),
                      fg=rgb_hack((217, 217, 217)), activebackground=rgb_hack((49, 131, 212)), borderwidth=2,
                      relief="ridge")
buttonDelete.grid(column=5, row=4, padx=10, pady=10)

buttonExit = Button(window, text="Exit", width=20, height=2, font=myFont, bg=rgb_hack((50, 50, 50)),
                    fg=rgb_hack((217, 217, 217)), activebackground=rgb_hack((49, 131, 212)), borderwidth=2,
                    relief="ridge")
buttonExit.grid(column=5, row=5, padx=10, pady=10)

window.mainloop()
