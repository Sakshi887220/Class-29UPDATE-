# Python code to demonstrate table creation and  
# insertions with SQL 
  
# importing module 
import sqlite3 
from tkinter import * 
# Part 1 Creating a simple Database
root = Tk()
# connecting to the database  
connection = sqlite3.connect("myTable.db") 
  
# cursor  
crsr = connection.cursor() 
  
# SQL command to create a table in the database 
sql_command = """CREATE TABLE emp (  
staff_number INTEGER PRIMARY KEY,  
fname text,  
lname text,  
gender text,  
joining text);"""
  
# execute the statement 
crsr.execute(sql_command) 
  
# SQL command to insert the data in the table 
sql_command = """INSERT INTO emp VALUES (21, "Arpit", "Bansal", "M", "2014-03-28");"""
crsr.execute(sql_command) 
  
# another SQL command to insert the data in the table 
sql_command = """INSERT INTO emp VALUES (1, "Bill", "Gates", "M", "1980-10-28");"""
crsr.execute(sql_command) 
  
# To save the changes in the files. Never skip this.  
# If we skip this, nothing will be saved in the database. 
connection.commit() 
  
# close the connection 
connection.close() 

# Part 2 Creating a interface for entering values to our database.
# Create a submit function


def Submit():
    # connecting to the database  
    connection = sqlite3.connect("myTable.db") 
    # cursor  
    crsr = connection.cursor() 
    # Insert Into Table
    crsr.execute("INSERT INTO emp VALUES (:Staffno,  :f_name , :l_name , :Gender , :DOJi)",
        {
            'Staffno' : Staffno.get(),
            'f_name' : f_name.get(),
            'l_name' : l_name.get(),
            'Gender' : Gender.get(),
            'DOJi' : DOJi.get()
        }
    )
    connection.commit() # Commit all the changes to the database
    connection.close() 
    # Clear the Text Boxes
    Staffno.delete(0 ,END)
    f_name.delete(0 ,END)
    l_name.delete(0 ,END)
    Gender.delete(0 ,END)
    DOJi.delete(0 ,END)
def Query():
    # connecting to the database  
    connection = sqlite3.connect("myTable.db") 
    # cursor  
    crsr = connection.cursor() 
    # Insert Into Table
    crsr.execute("SELECT *,oid FROM emp")  
    # store all the fetched data in the ans variable 
    ans = crsr.fetchall()  
    # Since we have already selected all the data entries  
    # using the "SELECT *" SQL command and stored them in  
    # the ans variable, all we need to do now is to print  
    # out the ans variable 
    # As we want to display the dataframe in our GUI we can use label widget
    # ans is a list and for example we want to find the names of all the 
    # People in datatable we can use the following command
    records =""
    for record in ans:
        records += record[1] +" " +record[2] +"   " + str(record[0]) + '\n'
    Label(root , text = records ,bg = "yellow").grid(row = 10 ,column = 0 , columnspan = 2 )
def delete():
    # connecting to the database  
    connection = sqlite3.connect("myTable.db") 
    # cursor  
    crsr = connection.cursor() 
    # oid is the Primary field
    # We can choose any column instead of oid
    connection.execute("DELETE from emp where oid=" + deli.get())
    deli.delete(0 , END) 
    connection.commit() 
    connection.close()
def edit():
    connection = sqlite3.connect("myTable.db") 
    # cursor  
    crsr = connection.cursor() 
    crsr.execute("""UPDATE emp SET
    staff_number = :staffnum,
    fname = :f_name,
    lname = :l_name,
    gender = :Gender,
    joining = :DOJi
    Where oid = :Aid""",
        {
            'staffnum' : Staffno_edit.get(),
            'f_name' : f_name_edit.get(),
            'l_name' : l_name_edit.get(),
            'Gender' : Gender_edit.get(),
            'DOJi' : DOJi_edit.get(),
            'Aid' : deli.get()
        }
    )
    connection.commit() 
    connection.close()
def update():
    up = Tk() 
    connection = sqlite3.connect("myTable.db") 
    crsr = connection.cursor() 
    record_id = deli.get()
    crsr.execute("SELECT * FROM emp WHERE oid = " + record_id)
    records = crsr.fetchall()
    # Create Text Boxes
    global Staffno_edit
    Staffno_edit = Entry(up , width = 30)
    Staffno_edit.grid(row = 0 ,column = 1, padx = 20)
    global f_name_edit
    f_name_edit = Entry(up , width = 30)
    f_name_edit.grid(row = 1 ,column = 1, padx = 20)
    global l_name_edit
    l_name_edit = Entry(up , width = 30)
    l_name_edit.grid(row = 2 ,column = 1, padx = 20)
    global Gender_edit
    Gender_edit = Entry(up , width = 30)
    Gender_edit.grid(row = 3 ,column = 1, padx = 20)
    global DOJi_edit
    DOJi_edit = Entry(up , width = 30)
    DOJi_edit.grid(row = 4 ,column = 1, padx = 20)
    # Text box for deleting a specific record
    # Create text box labels
    Staffno_label = Label(up, text = "Staff Number") 
    Staffno_label.grid(row = 0 , column =0)

    f_name_label = Label(up, text = "First Name") 
    f_name_label.grid(row = 1 , column =0)

    l_name_label = Label(up, text = "Last Name") 
    l_name_label.grid(row = 2 , column =0)

    Gender_label = Label(up, text = "Gender") 
    Gender_label.grid(row = 3 , column =0)

    DOJi_label = Label(up, text = "Date of Joining") 
    DOJi_label.grid(row = 4 , column =0)
     # Loop through results and complete all the fields
    for record in records:
        Staffno_edit.insert(0, record[0])
        f_name_edit.insert(0, record[1])
        l_name_edit.insert(0,record[2])
        Gender_edit.insert(0, record[3])
        DOJi_edit.insert(0, record[4])
    # Button for Submit
    Button(up , text = "Submit Changes" , command = edit).grid(row = 5 , column = 1,pady = 10 , padx = 10)
    # Button for exit
    Button(up , text = "Exit" , command = up.destroy).grid(row = 6 , column = 1,pady = 10 , padx = 10)
    connection.commit() 
    connection.close()

# Create Text Boxes
Staffno = Entry(root , width = 30)
Staffno.grid(row = 0 ,column = 1, padx = 20)

f_name = Entry(root , width = 30)
f_name.grid(row = 1 ,column = 1, padx = 20)

l_name = Entry(root , width = 30)
l_name.grid(row = 2 ,column = 1, padx = 20)

Gender = Entry(root , width = 30)
Gender.grid(row = 3 ,column = 1, padx = 20)

DOJi = Entry(root , width = 30)
DOJi.grid(row = 4 ,column = 1, padx = 20)
# Text box for deleting a specific record
deli = Entry(root , width = 30)
deli.grid(row = 7 , column = 1 , padx = 20)

# Create text box labels
Staffno_label = Label(root, text = "Staff Number") 
Staffno_label.grid(row = 0 , column =0)

f_name_label = Label(root, text = "First Name") 
f_name_label.grid(row = 1 , column =0)

l_name_label = Label(root, text = "Last Name") 
l_name_label.grid(row = 2 , column =0)

Gender_label = Label(root, text = "Gender") 
Gender_label.grid(row = 3 , column =0)

DOJi_label = Label(root, text = "Date of Joining") 
DOJi_label.grid(row = 4 , column =0)

deli_label = Label(root , text = "Enter the ID of person to be selected")
deli_label.grid(row = 7 , column = 0)


# Create a submit button
Button(root , text = "Add record to data base" , command= Submit).grid(row = 5 , columnspan = 2 , pady=10 , padx = 20 , ipadx = 100 )
Button(root , text = "Query the database" , command= Query).grid(row = 6 , columnspan = 2 , pady=10 , padx = 20 , ipadx = 100 )

Button(root , text = "Delete the entered ID" , command= delete).grid(row = 8 , columnspan = 2 , pady=10 , padx = 20 , ipadx = 100 )
Button(root , text = "Select the entered ID" , command= update).grid(row = 9 , columnspan = 2 , pady=10 , padx = 20 , ipadx = 100 )
root.mainloop()