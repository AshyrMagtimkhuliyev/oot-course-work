from fnmatch import translate
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

mydb = sqlite3.connect('')
my_cursor = mydb.cursor()

my_cursor.execute("create table if not exists Store(item_name VARCHAR(20) not null unique, item_price INTEGER(10), item_quantity INTEGER(10), item_category VARCHAR(20), item_discount float(3), item_id INTEGER AUTO_INCREMENT PRIMARY KEY)")

root = Tk()
root.title("Writing Suplies Store")
root.configure(width=1500, height=600, bg="LightBlue")


# All functions
def additem():

    try:
        e1 = entry1.get()
        e2 = entry2.get()
        e3 = entry3.get()
        e4 = entry4.get()
        e5 = entry5.get()
        try:
            if (e1 != "" and e2 != "" and e3 != "" and e4 != "" and e5 != "" ):
                if(e1.isdigit() == False and e4.isdigit() == False):
                    my_cursor.execute(
                        f'INSERT INTO Store (item_name, item_price, item_quantity, item_category, item_discount) VALUES ("{e1.lower()}","{int(e2)}","{int(e3)}","{e4}","{int(e5)}")')
                    mydb.commit()
                    entry1.delete(0, END)
                    entry2.delete(0, END)
                    entry3.delete(0, END)
                    entry4.delete(0, END)
                    entry5.delete(0, END)
                    messagebox.showinfo(
                        "ADD ITEM", "ITEM ADDED SUCCESSFULLY....!!!")
                else:
                    messagebox.showinfo("ERROR", "Item Name and Item Category can't be in Numbers")
            else:
                messagebox.showinfo("ERROR", "ENTER ALL DETAILS ...!!!")
        except ValueError:
            messagebox.showinfo("ERROR", "Item Price, quantity, discount can't be in String")
    except:
        messagebox.showerror(
            "Duplicate", "You are trying to insert a item which is already present in database")


def delete1():
    e6 = entry6.get()
    if e6 != "SEARCH" and e6 != "":
        my_cursor.execute(
            f"select * from Store where item_name = '{e6.lower()}'")
        data = my_cursor.fetchone()
        if (data != None):
            my_cursor.execute(
                f"delete from Store where item_name = '{e6.lower()}'")
            mydb.commit()
            messagebox.showinfo(
                "DELETE ITEM", "ITEM DELETED SUCCESSFULLY....!!!")
        else:
            messagebox.showinfo("ERROR", "NO DATA WITH SUCH NAME....!!!")
    else:
        messagebox.showwarning("NO DATA", "PLEASE ENTER ANY NAME....!!!")


def showdatabase():
    root1 = Tk()
    root1.configure(bg="Grey")
    root1.title("Writing Suplies Store Database")
    my_cursor.execute("select * from Store")
    mytext1 = my_cursor.fetchall()
    mytext = Text(root1, width=90, height=20, bg="LightBlue",
                  fg="black", font=("Times", 12))
    mytext.insert(
        END, " Item_Name \t\tItem_Price \t\tItem_Quantity \t\tItem_Category \t\tItem_Discount \n")
    mytext.insert(
        END, " ------------ \t\t----------- \t\t-------------- \t\t--------------- \t\t--------------- \n")
    for row in mytext1:
        mytext.insert(END, "       {0} \t\t     {1} \t\t         {2} \t\t   {3} \t\t          {4}\n".format(
            row[0], row[1], row[2], row[3], row[4]))
    mytext.pack(side=LEFT)


def clear_entry(event, entry):
    entry.delete(0, END)
    entry.unbind('<Button-1>', on_click)


def searchitem():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    e6 = entry6.get()
    if e6 == "SEARCH" or e6 == "":
        {
            messagebox.showwarning(
                "Warning", "Please first enter item name for search")
        }
    else:
        my_cursor.execute(
            "select * from Store where item_name = '{0}'".format(str(e6).lower()))
        mytext1 = my_cursor.fetchone()
        if (mytext1 == None) and (e6 != "SEARCH" or e6 != ""):
            messagebox.showinfo("Error", "Element not exist")
        else:
            entry1.insert(0, mytext1[0])
            entry2.insert(0, mytext1[1])
            entry3.insert(0, mytext1[2])
            entry4.insert(0, mytext1[3])
            entry5.insert(0, mytext1[4])


def update():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    entry6.delete(0, END)
    root2 = Tk()
    root2.title("About")
    root2.configure(width=900, height=500, bg="Grey")




    text = '''This application can be used to maintain the Store Items.\n
In this, a store owners can maintain their purchased Items. If they want by
adding all the writing all Details of the Item and clicking on the ADD ITEM and automatically all items 
get stored in the Database. 
\nIf store owners wants to delete any item which is already there
in database, they can delete by specifying the details and
clicking on the Delete button.\n
If store owners wants to View the Items that they have Purchased or bought by just clicking on the
VIEW DATABASE and all the items will shown.\n
If store owners wants to check whether the item is already been loaded or not or to check the details
of the item, they basically can Type the Name of the Item(which is located on the top of search button)
and clicking the search Button and all the details will be displayed.\n
While entering any Details of an item, if store owners wrote wrong details, they can click on
CLEAR SCREEN button to clear all current entries. \n
If a store owners wants to exit the Application, they basically can click EXIT button to close the Application.'''
    ulabel0 = Label(root2, text=text, bg="lightblue",
                    fg="black", font=("Times", 14), width=80, height = 25)

    ulabel0.grid(columnspan=6, padx=10, pady=10)

def clearitem():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    entry6.delete(0, END)


def qExit():
    qExit=messagebox.askyesno(
        "Quit System", "Do you want to quit?")
    if qExit > 0:
        root.destroy()
        return


# All labels Entrys Button grid place
label0=Label(root, text="Welcome To Writing Supplies Store",
               bg="LightBlue", fg="black", font=("Times", 27), width=35)
label1=Label(root, text="ENTER ITEM NAME", bg="lightblue",
                relief="ridge", fg="black", font=("Times", 16), width=25)
entry1=Entry(root, font=("Times", 14), width=25, bg="white")
label2=Label(root, text="ENTER ITEM PRICE", relief="ridge", height="1",
               bg="lightblue", fg="black", font=("Times", 16), width=25)
entry2=Entry(root, font=("Times", 14), bd=2, width=25, bg="white")
label3=Label(root, text="ENTER ITEM QUANTITY", relief="ridge",
               bg="lightblue", fg="black", font=("Times", 16), width=25)
entry3=Entry(root, font=("Times", 14), bd=2, width=25, bg="white")
label4=Label(root, text="ENTER ITEM CATEGORY", relief="ridge",
               bg="lightblue", fg="black", font=("Times", 16), width=25)
entry4=Entry(root, font=("Times", 14), bd=2, width=25, bg="white")
label5=Label(root, text="ENTER ITEM DISCOUNT", bg="lightblue",
               relief="ridge", fg="black", font=("Times", 16), width=25)
entry5=Entry(root, font=("Times", 14), bd=2, width=25, bg="white")
buttoncolor="#49D810"
buttonfg="black"
button1=Button(root, text="ADD ITEM",
                relief="flat", bg=buttoncolor, fg=buttonfg, width=15, font=("Times", 14), borderwidth=0, compound="center", highlightthickness = 0, command=additem)
button2=Button(root, text="DELETE ITEM",
                relief="flat", bg=buttoncolor, fg=buttonfg, width=25, font=("Times", 14), borderwidth=0, compound="center", highlightthickness = 0, command=delete1)
button3=Button(root, text="VIEW DATABASE",
                relief="flat", bg=buttoncolor, fg=buttonfg, width=25, font=("Times", 14), borderwidth=0, compound="center", highlightthickness = 0, command=showdatabase)
button4=Button(root, text="SEARCH ITEM",
                relief="flat", bg=buttoncolor, fg=buttonfg, width=25, font=("Times", 14), borderwidth=0, compound="center", highlightthickness = 0, command=searchitem)
button5=Button(root, text="CLEAR SCREEN",
                relief="flat", bg=buttoncolor, fg=buttonfg, width=25, font=("Times", 14), borderwidth=0, compound="center", highlightthickness = 0, command=clearitem)
button6=Button(root, text="EXIT",
                relief="flat", bg=buttoncolor, fg=buttonfg, width=25, font=("Times", 14), borderwidth=0, compound="center", highlightthickness = 0, command=qExit)
entry6=Entry(root, font=("Times", 14), justify='left',
                width=25, bg="#EEEEF1")
entry6.insert(0, "SEARCH")
on_click=entry6.bind("<Button-1>", lambda event: clear_entry(event, entry6))
button7=Button(root, text="ABOUT",
                 bg=buttoncolor, fg=buttonfg, width=25, font=("Times", 12), command=update)
# POSITION OF ALL BUTTONS AND ENTRY
label0.grid(columnspan=6, padx=10, pady=10)
label1.grid(row=1, column=0, padx=10, pady=10)
label2.grid(row=2, column=0, padx=10, pady=10)
label3.grid(row=3, column=0, padx=10, pady=10)
label4.grid(row=4, column=0, padx=10, pady=10)
label5.grid(row=5, column=0, padx=10, pady=10)
entry1.grid(row=1, column=1, padx=10, pady=10)
entry2.grid(row=2, column=1, padx=10, pady=10)
entry3.grid(row=3, column=1, padx=10, pady=10)
entry4.grid(row=4, column=1, padx=10, pady=10)
entry5.grid(row=5, column=1, padx=10, pady=10)
entry6.grid(row=1, column=2, padx=10, pady=10)
button1.grid(row=6, column=0, padx=10, pady=10)
button2.grid(row=6, column=1, padx=10, pady=10)
button3.grid(row=3, column=2, padx=10, pady=10)
button4.grid(row=2, column=2, padx=10, pady=10)
button5.grid(row=4, column=2, padx=10, pady=10)
button6.grid(row=6, column=2, padx=10, pady=10)
button7.grid(row=5, column=2, padx=10, pady=10)

root.mainloop()
