# -*- coding: utf-8 -*-
"""
Created on Sun May 29 16:43:54 2022

@author: raneh
"""

from tkinter import *
from tkinter import ttk
from PIL import Image , ImageTk

from tkinter import messagebox
import mysql.connector
from datetime import datetime

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()


class Login_Window :
    def __init__( self , root ):
        self.root = root
        self.root.title( " Login")
        self.root.geometry("1550x800+0+0" )
        self.bg = ImageTk.PhotoImage( file = r"C:\Users\raneh\dbms miniproject\front.jpg")
        lbl_bg = Label( self.root , image = self.bg )
        lbl_bg.place( x = 0 , y = 0 , relwidth = 1 , relheight = 1 )
        frame = Frame( self.root , bg = "black" )
        frame.place(x = 610 , y = 170 , width = 340 , height = 450 )
        img1 = Image.open( r"C:\Users\raneh\dbms miniproject\fron1.jpg")
        img1 = img1.resize(( 100,100 ) , Image.ANTIALIAS )
        self.photoimage1 = ImageTk.PhotoImage( img1 )
        lblimg1 = Label( image = self.photoimage1 , bg = "black" , borderwidth = 0 )
        lblimg1.place( x = 730 , y = 175 , width = 100 , height = 100)
        get_str = Label( frame , text = " Get Started " , font = ( "times new roman" , 20 , "bold" ) , fg = "white" , bg = "black" )
        get_str.place( x = 95 , y = 100 )
        # label
        username =lbl=Label( frame , text = " Username " , font = ( "times new roman" , 15 , "bold" ) , fg = "white" , bg = "black" )
        username.place ( x = 70 , y = 155 )
        self.txtuser = ttk.Entry( frame , font = ( "times new roman" , 15 , "bold" ) )
        self.txtuser.place( x = 40 , y = 180 , width = 270 )
        password= lbl = Label( frame , text= " Password " , font = ( "times new roman" , 15 , "bold" ) , fg = "white" , bg = "black" )
        password.place ( x = 70 , y = 225 )
        self.txtpass = ttk.Entry( frame , font = ( " times new roman " , 15 , " bold " ) )
        self.txtpass.place( x = 40 , y = 250 , width = 270 )
        loginbtn = Button( frame ,command=self.login(), text = " Login " , font = ( "times new roman" , 15 , "bold" ) , bd = 3 , relief = RIDGE , fg = "white" , bg = "red",activeforeground='white',activebackground='red' )
        loginbtn.place ( x = 110 , y = 300 , width = 120 , height = 35 )
        registerbtn = Button( frame ,command=self.register_window, text = " Register " , font = ( "times new roman" , 15 , "bold" ) , bd = 3 , relief = RIDGE , fg = "white" , bg = "red",activeforeground='white',activebackground='red' )
        registerbtn.place ( x = 20 , y = 350 , width = 160 , height = 35 )
    
    def register_window( self ) :
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)
    def login(self):
        
        if self.txtuser.get() == "" or self.txtpass.get() == "" :
            messagebox.showerror( " Error " , " all field required " )
            
        elif self.txtuser.get() == " kapu " and self.txtpass.get() == "ashu" :
            messagebox.showinfo( " Success " , " Welcome to codewithkiran channel plaze subscribe my channel " )
        else :
            conn = mysql.connector.connect ( host = "localhost" , user = "root" ,password = "root@123" , database = "mini_project" )
            my_cursor = conn.cursor()
            my_cursor.execute ( " select * from User where email = %s and password = %s  OR select * from Agents where agent_email=%s and login_password=%s" , (
                self.txtuser.get() ,
                self.txtpass.get(),
                self.txtuser.get() ,
                self.txtpass.get(),
                ) )
            row = my_cursor.fetchone()
            if row == None :
                messagebox.showerror ( " Error " , " Inavalid Username & password " )
            else :
                
                self.new_window = Toplevel( self.new_window )
                self.app =cafe_management(self.new_window)
            conn.commit()
            conn.close()

class Register :
    def __init__(self , root ) :
        self.root = root
        self.root.title ( " Register " )
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
        
        
        
        
        




        
if __name__ =="__main__":
    main()
    
