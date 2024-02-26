from tkinter import Tk, Frame, Label, Entry, Button, messagebox
from tkinter import font as tkFont
from PIL import Image, ImageTk
from datetime import datetime, timedelta
import sqlite3
import bcrypt

root = Tk()
root.geometry("1300x650")
root.title("TASK ALARM")
root.iconbitmap("assets/logo_icon.ico")
font1 = ('Helvetica',25,'bold')
font2 = ('Arial',17,'bold')
font3 = ('Arial',13,'bold')
font4 = ('Arial',13,'bold','underline')
fonts = ('Arial', 16, 'bold')
helv36 = tkFont.Font(family="Helvetica",size=18,weight="bold")

conn = sqlite3.connect('project_db.db')
cursor = conn.cursor()
cursor.execute('''
               CREATE TABLE IF NOT EXISTS USERDB(
               username TEXT NOT NULL,
               password TEXT NOT NULL)''')
class Confirmation_Page:
    def __init__(self,root):
        self.root = root
        self.f1 = Frame(self.root,width=1300,height=650)
        self.f1.place(x=0,y=0)

        self.bg1 = Image.open("assets/backgrd1.png")
        self.bg1 = self.bg1.resize((1300,650))
        self.bg1 = ImageTk.PhotoImage(self.bg1)
        self.bg1_lbl1 = Label(self.f1, image = self.bg1)
        self.bg1_lbl1.place(x = 0, y= 0)
        
        self.img1 = Image.open("assets/intro1.png")
        self.img1 = self.img1.resize((600,500))
        self.img1 = ImageTk.PhotoImage(self.img1)
        self.img1_lbl1 = Label(self.f1, image = self.img1)
        self.img1_lbl1.place(x = 350, y= 15)
        
        self.config_button = Button(self.f1,text="Get Started",command=self.next_page,width=20,height=3,bg="#346340",fg="#FFFFFF",font=helv36)
        self.config_button.place(x = 470,y=527)
        
    def next_page(self):
        self.f1.destroy()
        self.bg1_lbl1.destroy()
        Sp = Signup_Page(self.root)

class Signup_Page:
    def __init__(self,root):
        self.root = root
        
        self.f2 = Frame(self.root,width=1300,height=650)
        self.f2.place(x=0,y=0)

        self.bg2 = Image.open("assets/backgrd2.png")
        self.bg2 = self.bg2.resize((1300,650))
        self.bg2 = ImageTk.PhotoImage(self.bg2)
        self.bg2_lbl2 = Label(self.f2, image = self.bg2)
        self.bg2_lbl2.image = self.bg2
        self.bg2_lbl2.place(x = 0, y= 0)

        self.log = Image.open("assets/login_img.png")
        self.log = self.log.resize((500,400))
        self.log= ImageTk.PhotoImage(self.log)
        self.log_lbl = Label(self.f2, image = self.log)
        self.log_lbl.image = self.log
        self.log_lbl.place(x=50, y=80)
        
        self.un_lbl = Label(self.f2,text="SIGNUP FORM",width=25,font =("Helvetica",25,"bold"),fg="blue")
        self.un_lbl.place(x=650,y=100)

        self.un_lbl1 = Label(self.f2,text="USERNAME",font =fonts,bg="yellow",width = 15)
        self.un_lbl1.place(x=670,y=240)
        self.un_ent = Entry(self.f2,fg="red",font=("Arial","16","bold"))
        self.un_ent.place(x=890,y=240)

        self.un_lbl2 = Label(self.f2,text="PASSWORD",font =fonts,bg="yellow",width=15)
        self.un_lbl2.place(x=670,y=290)
        self.un_lbl2_ent = Entry(self.f2,show="*",font=("Arial","16","bold"),fg="red")
        self.un_lbl2_ent.place(x=890,y=290)

        self.si_but = Button(self.f2,text="Signup",font=font3,bg="red",fg="yellow",cursor="hand2",command=self.func1)
        self.si_but.place(x=870,y=350)
        self.lal = Label(self.f2,text="If already registered?",font=font3)
        self.lal.place(x=700,y=430)
        self.lal1 = Button(self.f2,text="Login",font=font4,fg="red",bg="yellow",cursor="hand2",command=self.func2)
        self.lal1.place(x=900,y=420)
    def func1(self):
        username = self.un_ent.get()
        password = self.un_lbl2_ent.get()
        if username != '' and password != '':
            cursor.execute("SELECT username FROM USERDB WHERE username=?",[username])
            if cursor.fetchone() is not None:
                messagebox.showerror('Error','Username already exists.')
            else:
                encoded_password = password.encode('utf-8')
                hashed_password = bcrypt.hashpw(encoded_password,bcrypt.gensalt())
                cursor.execute('INSERT INTO USERDB VALUES (?,?)',[username,hashed_password])
                conn.commit()
                #create_user_database(username)
                messagebox.showinfo("Success","Account has been created.")
        else:
            messagebox.showerror("Error","Enter all data.")
    def func2(self):
        self.f2.destroy()
        self.f3 = Frame(self.root,width=1300,height=650)
        self.f3.place(x=0,y=0)

        self.bg3 = Image.open("assets/backgrd2.png")
        self.bg3 = self.bg3.resize((1300,650))
        self.bg3 = ImageTk.PhotoImage(self.bg3)
        self.bg3_lbl2 = Label(self.f3, image = self.bg3)
        self.bg3_lbl2.image = self.bg3
        self.bg3_lbl2.place(x = 0, y= 0)

        self.log1 = Image.open("assets/login_img.png")
        self.log1= self.log1.resize((500,400))
        self.log1= ImageTk.PhotoImage(self.log1)
        self.log1_lbl = Label(self.f3, image = self.log1)
        self.log1_lbl.image = self.log1
        self.log1_lbl.place(x=50, y=80)

        global un_ent2
        global pw_ent2
        self.un1_lbl = Label(self.f3,text="LOGIN FORM",width=25,font =("Helvetica",25,"bold"),fg="blue")
        self.un1_lbl.place(x=650,y=100)

        self.un_lbl12 = Label(self.f3,text="USERNAME",font =fonts,bg="yellow",width = 15)
        self.un_lbl12.place(x=670,y=240)
        self.un_ent2 = Entry(self.f3,fg="red",font=("Arial","16","bold"))
        self.un_ent2.place(x=890,y=240)

        self.un_lbl21 = Label(self.f3,text="PASSWORD",font =fonts,bg="yellow",width=15)
        self.un_lbl21.place(x=670,y=290)
        self.pw_ent2 = Entry(self.f3,show="*",font=("Arial","16","bold"),fg="red")
        self.pw_ent2.place(x=890,y=290)

        self.backsib = Button(self.f3,text="Back to signup",font=font3,bg="red",fg="yellow",cursor="hand2",command=self.back)
        self.backsib.place(x=670,y=370)
        self.log_but = Button(self.f3,text="login",font=font2,bg="red",fg="yellow",cursor="hand2",command=self.func3)
        self.log_but.place(x=900,y=370)
    def back(self):
        self.f3.destroy()
        sp=Signup_Page(self.root)

    def func3(self):
        username = self.un_ent2.get()
        password = self.pw_ent2.get()
        if username != '' and password !='':
            cursor.execute('SELECT password FROM USERDB WHERE username=?',[username])
            result = cursor.fetchone()
            if result:
                if bcrypt.checkpw(password.encode('utf-8'),result[0]):
                    messagebox.showinfo('Success','Logged in Successfully.')
                    self.f3.destroy()
                    Mp =Main_Page(self.root,username)
                else:
                    messagebox.showerror('Error','Invalid Password.')
            else:
                messagebox.showerror('Error','Invalid Username')
        else:
            messagebox.showerror('Error','Enter all data.')
class Main_Page:
    def __init__(self,root,username):
        self.root = root
        self.username = username
        self.f4 = Frame(self.root,width=1300,height=650)
        self.f4.place(x=0,y=0)
        self.mbg3 = Image.open("assets/mainbg.png")
        self.mbg3 = self.mbg3.resize((1300,650))
        self.mbg3 = ImageTk.PhotoImage(self.mbg3)
        self.mbg3_lbl2 = Label(self.f4, image = self.mbg3)
        self.mbg3_lbl2.image = self.mbg3
        self.mbg3_lbl2.place(x = 0, y= 0)

        self.u1 = Image.open("assets/user.png")
        self.u1= self.u1.resize((350,350))
        self.u1= ImageTk.PhotoImage(self.u1)
        self.u1_lbl = Label(self.f4, image = self.u1)
        self.u1_lbl.image = self.u1
        self.u1_lbl.place(x=50, y=80)

        self.username_lbl = Label(self.f4, text=f"{self.username}", font=fonts)
        self.username_lbl.place(x=150, y=460)
        self.logout_button = Button(self.f4, text="Logout",width=15, font=font3, bg="red", fg="yellow", cursor="hand2", command=self.logout)
        self.logout_button.place(x=890, y=550)

        self.create = Button(self.f4,text="CREATE TASK",font=font2)#,command = self.creation)
        self.create.place(x=550,y=150)
        self.edit = Button(self.f4,text="EDIT",font=font2)
        self.edit.place(x=550,y=250)
    
    #def creation(self):
       #self.


    def logout(self):
        self.f4.destroy()
        confirmation = Confirmation_Page(self.root)
       









    





       

        
        
        







        

confirmation = Confirmation_Page(root)
root.mainloop()


