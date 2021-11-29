from tkinter import *

import Database


def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb


def viewFunction():
    booklist.delete(0, END)
    # booklist.insert(END, "SNo   Title      Author   Year UID")
    for x in Database.viewAll():
        booklist.insert(END, x)
    scrollFunction()


def searchFunction():
    booklist.delete(0, END)
    flag = 0
    for x in Database.search(title.get().upper(), author.get().upper(), year.get(), UID.get()):
        flag = 1
        booklist.insert(END, x)
    if flag == 0:
        booklist.insert(END, 'Entered Search Not Found.')


def addFunction():
    booklist.delete(0, END)
    flag = 0
    for x in Database.search(ISBN=UID.get()):
        booklist.insert(END, x)
        flag = 1
    if (title.get() == '' or author.get() == '' or year.get() == '' or UID.get() == ''):
        booklist.insert(END, 'All entries are mandatory and can\'t be left blank.')
    elif flag == 1:
        booklist.insert(END, 'ISBN already present in database.')
        booklist.insert(END, 'ISBN should be unique. Please try again.')
    else:
        Database.insert(title.get(), author.get(), year.get(), UID.get())
        booklist.delete(0, END)

        searchFunction()
        booklist.insert(END, 'Entry Added!')


def deleteFunction():
    if selectedRow[0] != -999:
        Database.delete(selectedRow[0])
        booklist.delete(0, END)
        booklist.insert(END, selectedRow)
        booklist.insert(END, "\nEntry has been deleted.")


def updateFunction():
    if selectedRow[0] != -999:
        if entryUID.get() == selectedRow[0]:
            Database.update(entryTitle.get(), entryAuthor.get(), entryYear.get(), entryUID.get(), entryUID.get())
            booklist.delete(0, END)
            searchFunction()
            booklist.insert(END, "Entry Updated!")
        else:
            booklist.delete(0, END)
            flag = 0

            for x in Database.search(ISBN=UID.get()):
                booklist.insert(END, x)
                flag = 1
            if flag == 1:
                booklist.insert(END, 'ISBN already present in database.')
                booklist.insert(END, 'ISBN should be unique. Please try again.')
            else:
                Database.update(entryTitle.get(), entryAuthor.get(), entryYear.get(), entryUID.get(), selectedRow[0])
                booklist.delete(0, END)
                searchFunction()
                booklist.insert(END, "Entry Updated.")


def exitFunction():
    window.destroy()


def getSelectedRow(event):
    index = booklist.curselection()[0]
    global selectedRow
    selectedRow = booklist.get(index)
    entryAuthor.delete(0, END)
    entryTitle.delete(0, END)
    entryUID.delete(0, END)
    entryYear.delete(0, END)
    entryTitle.insert(END, selectedRow[1])
    entryAuthor.insert(END, selectedRow[2])
    entryYear.insert(END, selectedRow[3])
    entryUID.insert(END, selectedRow[0])


def scrollFunction():
    scrollbarY = Scrollbar(window, bg=rgb_hack((50, 50, 50)))
    scrollbarY.grid(column=4, row=0, rowspan=9, sticky='ns', padx=10, pady=10)
    booklist.configure(yscrollcommand=scrollbarY.set)
    scrollbarY.configure(command=booklist.yview)

    scrollbarX = Scrollbar(window, bg=rgb_hack((50, 50, 50)), orient='horizontal')
    scrollbarX.grid(column=3, row=10, sticky='ew', padx=10, pady=10)
    booklist.configure(xscrollcommand=scrollbarX.set)
    scrollbarX.configure(command=booklist.xview)


window = Tk()
window.title("Book Store")
window.state('zoomed')
window.config(bg=rgb_hack((50, 50, 50)))
myFont = ("Consolas", "16", "bold")

labelTitle = Label(window, text="Book Title", width=10, height=2, font=myFont, bg=rgb_hack((50, 50, 50)),
                   fg=rgb_hack((222, 222, 222)))
labelTitle.grid(row=0, column=0, padx=10, pady=10)
labelAuthor = Label(window, text="Author", width=10, height=2, font=myFont, bg=rgb_hack((50, 50, 50)),
                    fg=rgb_hack((222, 222, 222)))
labelAuthor.grid(row=1, column=0, padx=10, pady=10)
labelYear = Label(window, text="Year", width=10, height=2, font=myFont, bg=rgb_hack((50, 50, 50)),
                  fg=rgb_hack((222, 222, 222)))
labelYear.grid(column=0, row=2, padx=10, pady=10)
labelUID = Label(window, text="ISBN", width=10, height=2, font=myFont, bg=rgb_hack((50, 50, 50)),
                 fg=rgb_hack((222, 222, 222)))
labelUID.grid(column=0, row=3, padx=10, pady=10)

title = StringVar()
entryTitle = Entry(window, textvariable=title, width=20, borderwidth=2, font=myFont,
                   bg=rgb_hack((50, 50, 50)),
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

booklist = Listbox(window, height=28, width=65, font=myFont, bg=rgb_hack((50, 50, 50)),
                   fg=rgb_hack((217, 217, 217)), borderwidth=2,
                   relief="ridge")
booklist.grid(column=3, row=0, rowspan=9, padx=10, pady=10)

booklist.bind('<<ListboxSelect>>', getSelectedRow)

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
                      relief="ridge", command=updateFunction)
buttonUpdate.grid(column=5, row=3, padx=10, pady=10)

buttonDelete = Button(window, text="Delete Selected", width=20, height=2, font=myFont, bg=rgb_hack((50, 50, 50)),
                      fg=rgb_hack((217, 217, 217)), activebackground=rgb_hack((49, 131, 212)), borderwidth=2,
                      relief="ridge", command=deleteFunction)
buttonDelete.grid(column=5, row=4, padx=10, pady=10)

buttonExit = Button(window, text="Exit", width=20, height=2, font=myFont, bg=rgb_hack((50, 50, 50)),
                    fg=rgb_hack((217, 217, 217)), activebackground=rgb_hack((49, 131, 212)), borderwidth=2,
                    relief="ridge", command=exitFunction)
buttonExit.grid(column=5, row=5, padx=10, pady=10)

selectedRow = (-999,)

viewFunction()
window.mainloop()
