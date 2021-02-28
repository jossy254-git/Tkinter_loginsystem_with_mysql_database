#sql.py----creates a responsive login system with tkinter and mysql database.
import pymysql
import os
import time
from tkinter import *

connection = pymysql.connect(host="Jossy", 
user="root", 
password="rootsman",
db="mysql1")

mycur = connection.cursor()

def err_destroy():
    err.destroy()

def succ_destroy():
    succ.destroy()
    root1.destroy()

def error():
    global err
    err = Toplevel(root1)
    err.title("Error")
    err.geometry("200x100")
    Label(err, text="all fields are required.." , fg="red", font="bold").pack()
    Label(err, text="").pack()
    Button(err, text="OK", bg="green", width=8, height=1, command=err_destroy).pack()

def success():
    global succ
    succ = Toplevel(root1)
    succ.title("success")
    succ.geometry("200x100")
    Label(succ, text="Registration succefully...", fg="green", font="bold").pack()
    Label(succ, text="").pack()
    Button(succ, text="OK", bg="grey", width=8, height=1, command=succ_destroy).pack()

def register_user():
    userName_info = username.get()
    password_info = password.get()
        
    if username == "":
        error()
    elif password_info == "":
        error()
    else:
        sql = "insert into login values(%s,%s)"
        t = (userName_info, password_info)
        mycur.execute(sql, t)
        connection.commit()
        Label(root1, text="").pack()
        time.sleep(0.50)
        success()

def registration():
    global root1
    root1 = Toplevel(root)
    root1.title("Registration portal")
    root1.geometry("300x250")
    global username
    global password
    Label(root1, text="Register your account", bg="black", fg="white", font="bold", width=300).pack()
    username = StringVar()
    password =StringVar()
    Label(root1, text="").pack()
    Label(root1, text="username:", font="bold").pack()
    Entry(root1, textvariable=username).pack()
    Label(root1, text="").pack()
    Label(root1, text="password:", font="bold").pack()
    Entry(root1, textvariable=password).pack()
    Label(root1, text="").pack()
    Button(root1, text="Register", bg="green", fg="yellow", command=register_user).pack()
    Label(root1, text="").pack()

def login():
    global root2
    root2 = Toplevel(root)
    root2.title("Log-in portal")
    root2.geometry("300x300")
    global username_varify
    global password_varify
    Label(root2, text="Log-in portal", bg="black", fg="white", font="bold", width=300).pack()
    username_varify = StringVar()
    password_varify = StringVar()
    Label(root2, text="").pack()
    Label(root2, text="username:", font="bold").pack()
    Entry(root2, textvariable=username_varify).pack()
    Label(root2, text="").pack()
    Label(root2, text="password:", font="bold").pack()
    Entry(root2, textvariable=password_varify).pack()
    Label(root2, text="").pack()
    Button(root2, text="log-in", bg="green", fg="yellow", command=login_varify).pack()
    Label(root2, text="").pack()
    Label(root2, text="help?", fg="red", font="san-serif").pack()
    Label(root2, text="").pack()
    Label(root2, text="forgot password!!", fg="blue", font="Helvetica").pack()

def logg_destroy():
    logg.destroy()
    root2.destroy()

def failed_destroy():
    fail.destroy()

def logged():
    global logg
    logg = Toplevel(root2)
    logg.title("welcome")
    logg.geometry("200x100")
    Label(logg, text="welcome{}".format(username_varify.get()), fg="green", font="bold").pack()
    Label(logg, text="").pack()
    Button(logg, text="log-out", bg="grey", width=8, height=1, command=logg_destroy).pack()

def failed():
    global fail
    fail = Toplevel(root2)
    fail.title("invalid")
    fail.geometry("200x100")
    Label(fail, text="invalid credentials...", fg="red", font="bold").pack()
    Label(fail, text="").pack()
    Button(fail, text="OK", bg="grey", width=8, height=1, command=failed_destroy).pack()

def login_varify():
    user_varify = username_varify.get()
    pas_varify = password_varify.get()
    sql = "select * from login1 where user = %s and password = %s"
    mycur.execute( sql, [(user_varify),(pas_varify)])
    results = mycur.fetchall()
    if results:
        for i in results:
            logged()
            break

    else:
        failed()

def main_screen():
    global root
    root = Tk()
    root.title("log-in portal")
    root.geometry("300x300")
    Label(root, text="welcome to log-in portal", font="bold", bg="black", fg="white", width=300).pack()
    Label(root, text="").pack()
    Button(root, text="Registration", height="1", width="15", bg="green", font="bold", command=registration).pack()
    Button(root, text="Login", height="1", width="15", bg="yellow", font="bold", command=login).pack()
    Label(root, text="").pack()
    Label(root, text="").pack()
    Label(root, text="developed by Jossy Kamau", fg="red", font="Helvetica").pack()
    Label(root, text="").pack()
    Label(root, text="about developer", fg="blue", font="san-serif").pack()

main_screen()
root.mainloop()