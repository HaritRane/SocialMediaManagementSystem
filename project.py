# -*- coding: utf-8 -*-
"""
Created on Mon May 30 04:44:28 2022

@author: raneh
"""
from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector
class User :
    def __init__ ( self , root ) :
        self.root= root
        self.root.title( " User " )
        self.root.geometry("1540x800+0+0")
        lbltitle = Label(root, bd = 20 , relief = RIDGE , text= " SOCIAL MEDIA MANAGEMENT SYSTEM ",fg='red',bg='white',font=("times new roman",35,"bold"))
        lbltitle.pack(side=TOP,fill=X)
        
        self.var_email1= StringVar()
        frame = Frame( self.root , bg = "white" )
        frame.place( x = 20 , y = 100 , width = 800 , height = 550 )
        email = Label( frame , text = " email id " , font = ( "times new roman" , 15 , "bold" ) , bg = "white" )
        email.place ( x = 25 , y = 5 )
        email_entry = ttk.Entry( frame ,textvariable=self.var_email1, font = ( "times new roman" , 15 , "bold" ) )
        email_entry.place( x = 100 , y = 5 , width = 250 )
        view_account = Button( frame , text = "View Account " , font = ( "times new roman" , 15 , "bold" ) , bd = 3 , relief = RIDGE , fg = "white" , bg = "red",activeforeground='white',activebackground='red' )
        view_account.place ( x = 20 , y = 50, width = 300 , height = 35 )
        approve_posts = Button( frame , text = "Approve posts " , font = ( "times new roman" , 15 , "bold" ) , bd = 3 , relief = RIDGE , fg = "white" , bg = "red",activeforeground='white',activebackground='red' )
        approve_posts.place ( x = 20 , y = 90, width = 300 , height = 35 )
        
        conn = mysql.connector.connect( host = "localhost" , user = "root" ,password = "root@123" , database = "mini_project" )
        my_cursor = conn.cursor()
        my_cursor.execute ( " (select user_id from User where email=%s))" , (
            self.var_email1
            
            ) )
        lbl1 = Label(root, bd = 10 , relief = RIDGE , text= " User ID",fg='red',bg='white',font=("times new roman",35,"bold"))
        lbl1.pack(side=BOTTOM)
        id_entry = ttk.Entry( frame ,text=my_cursor.fetchone(), font = ( "times new roman" , 15 , "bold" ) )
        id_entry.pack(side=BOTTOM)
       # conn.commit()
       # conn.close()
       
        add_account = Button( frame ,command=self.add_account, text = " Add new Account " , font = ( "times new roman" , 15 , "bold" ) , bd = 3 , relief = RIDGE , fg = "white" , bg = "red",activeforeground='white',activebackground='red' )
        add_account.place ( x = 360 , y = 5, width = 300 , height = 35 )
        
        
        account_details = Button( frame ,command=self.acc_detail, text = " Account Details " , font = ( "times new roman" , 15 , "bold" ) , bd = 3 , relief = RIDGE , fg = "white" , bg = "red",activeforeground='white',activebackground='red' )
        account_details.place ( x = 360 , y = 45 , width = 300 , height = 35 )
        createpost = Button( frame ,command=self.create_post, text = " Create post " , font = ( "times new roman" , 15 , "bold" ) , bd = 3 , relief = RIDGE , fg = "white" , bg = "red",activeforeground='white',activebackground='red' )
        createpost.place ( x = 360 , y = 85 , width = 300 , height = 35 )
        scheduler = Button( frame ,command=self.schedule, text = " Scheduler " , font = ( "times new roman" , 15 , "bold" ) , bd = 3 , relief = RIDGE , fg = "white" , bg = "red",activeforeground='white',activebackground='red' )
        scheduler.place ( x = 360 , y = 125 , width = 300 , height = 35 )
        post_history = Button( frame ,command=self.post_hist, text = " Post history " , font = ( "times new roman" , 15 , "bold" ) , bd = 3 , relief = RIDGE , fg = "white" , bg = "red",activeforeground='white',activebackground='red' )
        post_history.place ( x = 360 , y = 165 , width = 300 , height = 35 )
        
        
    def add_account(self):
            self.new_window1 = Toplevel(self.root)
            self.app1 = Add_acc(self.new_window1)
    def acc_detail(self):
            self.new_window2 = Toplevel(self.root)
            self.app2 = Acc_detail(self.new_window2)
    def create_post(self):
        self.new_window3 = Toplevel(self.root)
        self.app3 = Create_post(self.new_window3)
    def schedule(self):
        self.new_window4 = Toplevel(self.root)
        self.app4 = Scheduler(self.new_window4)
    def post_hist(self):
        self.new_window5 = Toplevel(self.root)
        self.app5 = History(self.new_window5)
    def view_acc(self):
        self.new_window6 = Toplevel(self.root)
        self.app6 = View_acc(self.new_window6)
    def approve(self):
        self.new_window7 = Toplevel(self.root)
        self.app7 = Approve_post(self.new_window7)


class Add_acc:
    def __init__(self , root ) :
        self.root = root
        self.root.title ( " Add Account " )
        self.root.geometry ( "1550x800+0+0" )
        
        
        self.var_email = StringVar()
        self.var_site = StringVar()
        

        frame = Frame( self.root , bg = "white" )
        frame.place( x = 520 , y = 100 , width = 800 , height = 550 )
        
        
        fname = Label( frame , text = " Enter email id " , font = ( "times new roman" , 15 , "bold" ) , bg = "white" )
        fname.place ( x = 50 , y = 100 )
        fname_entry = ttk.Entry( frame ,textvariable=self.var_email, font = ( "times new roman" , 15 , "bold" ) )
        fname_entry.place( x = 50 , y = 130 , width = 250 )
        
        
        site = Label( frame , text = " Select Site " , font = ( "times new roman" , 15 , "bold" ) , bg = "white" , fg = "black")
        site.place( x =50 , y = 240 )
        self.combo_domain = ttk.Combobox( frame ,textvariable=self.var_site, font = ( "times new roman" , 15 , "bold" ),state="readonly" )
        self.combo_domain[ "values" ] = ( "Select" , " Instagram " , " Facebook " , "Twitter","Linkedin" )
        self.combo_domain.current(0)
        self.combo_domain.place ( x = 50 , y = 270 , width = 250 )
        
        
        add_btn = Button( frame ,command=self.add_data, text = " ADD " , font = ( "times new roman" , 15 , "bold" ) , bd = 3 , relief = RIDGE , fg = "white" , bg = "red",activeforeground='white',activebackground='red' )
        add_btn.place ( x = 10 , y = 420 , width = 300 , height = 35 )
        backbtn = Button( frame ,command=self.return_login, text = " Back " , font = ( "times new roman" , 15 , "bold" ) , bd = 3 , relief = RIDGE , fg = "white" , bg = "red",activeforeground='white',activebackground='red' )
        backbtn.place( x = 330 , y = 420 , width = 200 , height = 35 )
        
    def add_data ( self ) :
        if self.var_email.get() == "" or self.var_site.get() == "" :
            messagebox.showerror( " Error " , " All fields are required " )
        
       
        else :
            conn =mysql.connector.connect ( host = "localhost" , user = "root" , password= "root@123" , database = "mini_project" )
            my_cursor= conn.cursor()
            query= ( " select * from User where email=%s" )
            value = ( self.var_email.get(), )
            my_cursor.execute( query , value )
            row= my_cursor.fetchone()
            if row == None:
                messagebox.showerror( " Error " , " User do not exist.register " )
            #else :
                 
                   # my_cursor.callproc()
                
                    
            conn.commit()
            conn.close()
            messagebox.showinfo(" success " , " Added  successfully")
    def return_login(self):
        self.root.destroy()


class Create_post :
    def __init__(self , root ) :
        self.root = root
        self.root.title ( " Create Post " )
        self.root.geometry ( "1600x900+0+0" )
        
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_uname = StringVar()
        self.var_email = StringVar()
        self.var_domain = StringVar()
        self.var_location = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()
        self.var_role=StringVar()

        frame = Frame( self.root , bg = "white" )
        frame.place( x = 520 , y = 100 , width = 800 , height = 550 )
        register_lbl = Label( frame , text = " REGISTER HERE " , font = ( "times new roman" , 20 , "bold" ) , fg = "green" ,bg="white")
        register_lbl.place( x = 20 , y = 20 )
        
        fname = Label( frame , text = " First Name " , font = ( "times new roman" , 15 , "bold" ) , bg = "white" )
        fname.place ( x = 50 , y = 100 )
        fname_entry = ttk.Entry( frame ,textvariable=self.var_fname, font = ( "times new roman" , 15 , "bold" ) )
        fname_entry.place( x = 50 , y = 130 , width = 250 )
        l_name = Label( frame , text = " Last Name " , font = ( "times new roman" , 15 , "bold" ) , bg = "white" , fg = "black")
        l_name.place( x =370 , y = 100 )
        self.txt_lname = ttk.Entry( frame ,textvariable=self.var_lname, font = ( "times new roman" , 15 ) )
        self.txt_lname.place( x = 370 , y = 130 , width = 250 )
       # --- row2
        u_name= Label( frame , text = " User Name " , font = ( "times new roman" , 15 , "bold" ) , bg = "white" , fg = "black")
        u_name.place( x = 50 , y = 170)
        self.txt_uname =ttk.Entry( frame ,textvariable=self.var_uname, font =( "times new roman" , 15 ) )
        self.txt_uname.place( x = 50 , y = 200 , width = 250 )
        email = Label( frame , text = " Email " , font = ( "times new roman" , 15 , "bold" ) , bg = "white" , fg = "black" )
        email.place( x = 370 , y = 170 )
        self.txt_email = ttk.Entry( frame ,textvariable=self.var_email, font = ( "times new roman" , 15 ) )
        self.txt_email.place( x = 370 , y = 200 , width = 250 )
       # ---- row3
        domain = Label( frame , text = " Select Domain " , font = ( "times new roman" , 15 , "bold" ) , bg = "white" , fg = "black")
        domain.place( x =50 , y = 240 )
        self.combo_domain = ttk.Combobox( frame ,textvariable=self.var_domain, font = ( "times new roman" , 15 , "bold" ),state="readonly" )
        self.combo_domain[ "values" ] = ( "Select" , " Regular " , " celebrity " , "Educational","Marketing","Healthcare","Lifestyle","others" )
        self.combo_domain.current(0)
        self.combo_domain.place ( x = 50 , y = 270 , width = 250 )
        
        location = Label( frame , text = " Location " , font = ( "times new roman" , 15 , "bold" ) , bg = "white" , fg = "black" )
        location.place( x = 370 , y = 240 )
        self.txt_loc = ttk.Entry ( frame ,textvariable=self.var_location, font = ( "times new roman" , 15 ) )
        self.txt_loc.place ( x = 370 , y = 270 , width = 250 )
        role = Label( frame , text = " Select Role" , font = ( "times new roman" , 15 , "bold" ) , bg = "white" , fg = "black")
        role.place( x =50 , y = 470 )
        self.combo_role = ttk.Combobox( frame ,textvariable=self.var_role, font = ( "times new roman" , 15 , "bold" ),state="readonly" )
        self.combo_role[ "values" ] = ( "Select" , " User " , " Agent "  )
        self.combo_role.current(0)
        self.combo_role.place ( x = 300 , y = 470 , width = 250 )
        pswd = Label( frame , text = " Password " , font = ( "times new roman" , 15 , "bold" ) , bg = "white" , fg = "black" )
        pswd.place ( x = 50 , y = 310 )
        self.txt_pswd = ttk.Entry( frame ,textvariable=self.var_pass, font = ( "times new roman" , 15 ) )
        self.txt_pswd.place( x = 50 , y = 340 , width = 250 )
        confirm_pswd = Label( frame , text = " Confirm Password " , font = ( "times new roman" , 15 , "bold" ) , bg = "white" , fg = "black" )
        confirm_pswd.place( x = 370 , y = 310 )
        self.txt_confirm_pswd = ttk.Entry( frame ,textvariable=self.var_confpass, font = ( "times new roman" , 15 ) )
        self.txt_confirm_pswd.place( x = 370 , y = 340 , width = 250 )
        registerbtn1 = Button( frame ,command=self.register_data, text = " Register Now " , font = ( "times new roman" , 15 , "bold" ) , bd = 3 , relief = RIDGE , fg = "white" , bg = "red",activeforeground='white',activebackground='red' )
        registerbtn1.place ( x = 10 , y = 420 , width = 300 , height = 35 )
        loginbtn1 = Button( frame ,command=self.return_login, text = " Login Now " , font = ( "times new roman" , 15 , "bold" ) , bd = 3 , relief = RIDGE , fg = "white" , bg = "red",activeforeground='white',activebackground='red' )
        loginbtn1.place( x = 330 , y = 420 , width = 200 , height = 35 )
        
    def register_data ( self ) :
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_domain.get() == " Select " or self.var_role.get()==" Select " :
            messagebox.showerror( " Error " , " All fields are required " )
        elif self.var_pass.get() != self.var_confpass.get() :
            messagebox.showerror( " Error " , " password & confirm password must be same " )
       
        else :
            conn =mysql.connector.connect ( host = "localhost" , user = "root" , password= "root@123" , database = "mini_project" )
            my_cursor= conn.cursor ( )
            query= ( " select * from User where email=%s" )
            value = ( self.var_email.get(), )
            my_cursor.execute( query , value )
            row= my_cursor.fetchone()
            if row !=None:
                messagebox.showerror( " Error " , " User already exist , plaese try another email " )
            else :
                if self.var_role.get()==" User ":
                    now= datetime.now()
                    formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
                    my_cursor.execute( "insert into User(first_name,last_name,user_name,email,password,registered_at,domain,location) values(%s,%s,%s,%s,%s,%s,%s,%s) " , (
                    self.var_fname.get() ,
                    self.var_lname.get() ,
                    self.var_uname.get() ,
                    self.var_email.get() ,
                    self.var_pass.get() ,
                    formatted_date,
                    
                    self.var_domain.get(),
                    self.var_location.get()
                    ))
                else:
                    my_cursor.execute( "insert into Agents(agent_name,login_password,agent_mail) values(%s,%s,%s) " , (
                    self.var_fname.get() ,
                    
                    self.var_pass.get(),
                    self.var_email.get()
                    ))
            conn.commit()
            conn.close()
            messagebox.showinfo(" success " , " Register successfully")
    def return_login(self):
        self.root.destroy()
        
    
        
        
class View_acc :
    def __init__(self , root ) :
        self.root = root
        self.root.title ( " Accounts " )
        self.root.geometry ( "1600x900+0+0" )
        
        
        self.var_id = IntVar()
        

        frame = Frame( self.root , bg = "white" )
        frame.place( x = 520 , y = 100 , width = 800 , height = 550 )
        
        
        fname = Label( frame , text = " User_id " , font = ( "times new roman" , 15 , "bold" ) , bg = "white" )
        fname.place ( x = 50 , y = 100 )
        fname_entry = ttk.Entry( frame ,textvariable=self.var_id, font = ( "times new roman" , 15 , "bold" ) )
        fname_entry.place( x = 50 , y = 130 , width = 250 )
        
        registerbtn1 = Button( frame ,command=self.register_data, text = " View " , font = ( "times new roman" , 15 , "bold" ) , bd = 3 , relief = RIDGE , fg = "white" , bg = "red",activeforeground='white',activebackground='red' )
        registerbtn1.place ( x = 10 , y = 420 , width = 300 , height = 35 )
        loginbtn1 = Button( frame ,command=self.return_login, text = " Back " , font = ( "times new roman" , 15 , "bold" ) , bd = 3 , relief = RIDGE , fg = "white" , bg = "red",activeforeground='white',activebackground='red' )
        loginbtn1.place( x = 330 , y = 420 , width = 200 , height = 35 )
        
    def register_data ( self ) :
        if self.var_email.get() == ""  :
            messagebox.showerror( " Error " , " All fields are required " )
        
        
        else :
                my_cursor.execute("drop view V if exists")
                my_cursor.execute( "CREATE VIEW V AS ( SELECT User.user_name,Site.site_name,User_accounts.account_id  FROM User LEFT JOIN  User_accounts ON User_accounts.user_id =User.user_id LEFT JOIN Site ON User_accounts.site_id=Site.site_id  WHERE User_accounts.user_id=%s); " , (
                    self.user_id
                    ))
                my_cursor.execute("Select * from V")
                records = mycursor.fetchall()
                print(records)

                for i, (user_name, site_name,account_id) in enumerate(records, start=1):
                    listBox.insert("", "end", values=(user_name, site_name,account_id))
                cols = ('id', 'stname', 'course','fee')
                listBox = ttk.Treeview(root, columns=cols, show='headings')

                for col in cols:
                    listBox.heading(col, text=col)    
                    listBox.grid(row=1, column=0, columnspan=2)
        conn.commit()
        conn.close()
        messagebox.showinfo(" success " , " Register successfully")
    def return_login(self):
        self.root.destroy()
        
        






root = Tk()
ob = User(root)
root.mainloop()