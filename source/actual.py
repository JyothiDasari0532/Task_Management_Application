from tkinter import Tk, Frame, Label, Entry, Button, messagebox,StringVar,END
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from tkinter import ttk
from datetime import datetime, timedelta
import sqlite3
import bcrypt
from plyer import notification


root = Tk()
root.geometry("1300x650")
root.resizable(False,False)
root.title("TASK ALARM")
root.iconbitmap("assets/logo_icon.ico")
font1 = ('Helvetica',25,'bold')
font2 = ('Arial',17,'bold')
font3 = ('Arial',13,'bold')
font4 = ('Arial',13,'bold','underline')
fonts = ('Arial', 16, 'bold')
helv36 =("Helvetica",18,"bold")

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
        
        self.config_button = Button(self.f1,text="Get Started",command=self.next_page,width=20,height=3,bg="#346340",fg="#FFFFFF",font=helv36,cursor="hand2")
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
        
        self.un_lbl = Label(self.f2,text="SIGNUP FORM",width=25,font =("Helvetica",25,"bold"),fg="dark blue")
        self.un_lbl.place(x=650,y=100)

        self.un_lbl1 = Label(self.f2,text="USERNAME",font =fonts,width = 15)
        self.un_lbl1.place(x=670,y=240)
        self.un_ent = Entry(self.f2,fg="red",font=("Arial","16","bold"))
        self.un_ent.place(x=890,y=240)

        self.un_lbl2 = Label(self.f2,text="PASSWORD",font =fonts,width=15)
        self.un_lbl2.place(x=670,y=290)
        self.un_lbl2_ent = Entry(self.f2,show="*",font=("Arial","16","bold"),fg="red")
        self.un_lbl2_ent.place(x=890,y=290)

        self.si_but = Button(self.f2,text="Signup",font=font3,bg="red",fg="yellow",cursor="hand2",command=self.func1)
        self.si_but.place(x=870,y=350)
        self.lal = Label(self.f2,text="If already registered?",font=font3)
        self.lal.place(x=700,y=430)
        self.lal1 = Button(self.f2,text="Login",font=font4,fg="yellow",bg="red",cursor="hand2",command=self.func2)
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
        self.un1_lbl = Label(self.f3,text="LOGIN FORM",width=25,font =("Helvetica",25,"bold"),fg="dark blue")
        self.un1_lbl.place(x=650,y=100)

        self.un_lbl12 = Label(self.f3,text="USERNAME",font =fonts,width = 15)
        self.un_lbl12.place(x=670,y=240)
        self.un_ent2 = Entry(self.f3,fg="red",font=("Arial","16","bold"))
        self.un_ent2.place(x=890,y=240)

        self.un_lbl21 = Label(self.f3,text="PASSWORD",font =fonts,width=15)
        self.un_lbl21.place(x=670,y=290)
        self.pw_ent2 = Entry(self.f3,show="*",font=("Arial","16","bold"),fg="red")
        self.pw_ent2.place(x=890,y=290)

        self.backsib = Button(self.f3,text="Back to signup",font=font3,bg="red",fg="yellow",cursor="hand2",command=self.back)
        self.backsib.place(x=670,y=380)
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
        self.mbg3 = Image.open("assets/main.png")
        self.mbg3 = self.mbg3.resize((1300,650))
        self.mbg3 = ImageTk.PhotoImage(self.mbg3)
        self.mbg3_lbl2 = Label(self.f4, image = self.mbg3)
        self.mbg3_lbl2.image = self.mbg3
        self.mbg3_lbl2.place(x = 0, y= 0)

        self.u1 = Image.open("assets/userlogo.png")
        self.u1= self.u1.resize((350,350))
        self.u1= ImageTk.PhotoImage(self.u1)
        self.u1_lbl = Label(self.f4, image = self.u1)
        self.u1_lbl.image = self.u1
        self.u1_lbl.place(x=50, y=80)

        self.username_lbl = Label(self.f4, text=f"{self.username}", font=fonts)
        self.username_lbl.place(x=162, y=260)
        self.logout_button = Button(self.f4, text="Logout",width=15, font=font3, bg="red", fg="yellow", cursor="hand2", command=self.logout)
        self.logout_button.place(x=890, y=550)

        self.create = Button(self.f4,text="CREATE TASK",bg="#eb34e1",font=font2,command = self.creation,cursor="hand2")
        self.create.place(x=550,y=100)
        self.edit = Button(self.f4,text="VIEW TASKS",bg="#eb34e1",font=font2,command=self.view_tasks,cursor="hand2")
        self.edit.place(x=550,y=200)
        self.com = Button(self.f4,text="COMPLETED TASKS",bg="#eb34e1",font=font2,command=self.goto_comp,cursor="hand2")
        self.com.place(x=550,y=300)
        self.overdue = Button(self.f4,text="OVERDUE TASKS",bg="#eb34e1",font=font2,cursor="hand2",command=self.go_over)
        self.overdue.place(x=550,y=400)


    def goto_comp(self):
        self.f4.destroy()
        comt = Completed_tasks(self.root,self.username)
    def creation(self):
        self.f4.destroy()
        cr = Create_Tasks(self.root,self.username)
    def view_tasks(self):
        self.f4.destroy()
        vt = ViewTasks(self.root, self.username)
    def go_over(self):
        self.f4.destroy()
        od = OverdueTasks(self.root,self.username)

    def logout(self):
        self.f4.destroy()
        confirmation = Confirmation_Page(self.root)
 
class ViewTasks:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.f6 = Frame(self.root, width=1300, height=650)
        self.f6.place(x=0, y=0)
        self.mbg4 = Image.open("assets/sourcebg.png")
        self.mbg4 = self.mbg4.resize((1300,650))
        self.mbg4 = ImageTk.PhotoImage(self.mbg4)
        self.mbg4_lbl2 = Label(self.f6, image = self.mbg4)
        self.mbg4_lbl2.image = self.mbg4
        self.mbg4_lbl2.place(x=0,y=0)
        self.back2 = Button(self.f6,text="BACK",bg="pink",fg="black",font = font3,width = 15,command= self.goto_uspage,cursor="hand2")
        self.back2.place(x=650,y=550)
        user_db_name = f"{self.username}_tasks.db"
        user_conn = sqlite3.connect(user_db_name)
        user_cursor = user_conn.cursor()

        user_cursor.execute("SELECT * FROM tasks")
        tasks = user_cursor.fetchall()
        y = 20
        for task in tasks:
            task_name, task_ddate, topt_time, t_priority = task[1:]
            task_label = Label(self.f6, text=f"Task: {task_name}, Due Date: {task_ddate}, Time: {topt_time}, Priority: {t_priority}")
            #task_label.grid(row=row, column=0, padx=10, pady=5, sticky="w")
            task_label.place(x=20,y=y)
    
            edit_button = Button(self.f6, text="Edit", command=lambda t=task: self.edit_task(t),cursor="hand2")
            #edit_button.grid(row=row, column=1, padx=10, pady=5)
            edit_button.place(x=430,y=y)
            done_button = Button(self.f6,text="Done",command=lambda t = task:self.done_task(t),cursor="hand2")
            done_button.place(x=480,y=y)
            y+=40
        for task in tasks:
            self.check_task_due_time(task)

        user_conn.close()

    def goto_uspage(self):
        self.f6.destroy()
        Mp =Main_Page(self.root,self.username)
    def done_task(self, task):
        task_name, task_ddate, topt_time, t_priority = task[1:]
        # Move the task to the Completed Tasks page
        user_db_name = f"{self.username}_tasks.db"
        user_conn = sqlite3.connect(user_db_name)
        user_cursor = user_conn.cursor()

        # Create completed_tasks table if it doesn't exist
        user_cursor.execute('''
                            CREATE TABLE IF NOT EXISTS completed_tasks(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            task_name TEXT NOT NULL,
                            task_ddate TEXT NOT NULL,
                            topt_time TEXT NOT NULL,
                            t_priority TEXT NOT NULL)
                            ''')

        user_cursor.execute('INSERT INTO completed_tasks (task_name, task_ddate, topt_time, t_priority) VALUES (?, ?, ?, ?)',
                            (task_name, task_ddate, topt_time, t_priority))
        user_conn.commit()
        user_cursor.execute('DELETE FROM tasks WHERE task_name=? AND task_ddate = ? AND topt_time = ? AND t_priority = ?',(task_name, task_ddate, topt_time, t_priority))
        user_conn.commit()
       
         # Display a message
        messagebox.showinfo("Task Completed", f"Hurray! You completed task: {task_name}")

        #task_frame.destroy()
        self.f6.destroy()
        vt = ViewTasks(self.root,self.username)
        user_conn.close()
    
    def check_task_due_time(self, task):
        task_name, task_ddate, topt_time, t_priority = task[1:]
        
        # Convert due date and time strings to datetime objects
        due_datetime = datetime.strptime(f"{task_ddate} {topt_time}", "%m/%d/%y %I:%M%p")
        
        # Get current time
        current_datetime = datetime.now()
        
        # Calculate time difference between current time and due time
        time_difference = due_datetime - current_datetime
        
        # Check if the task is due within a certain threshold (e.g., 15 minutes)
        if timedelta(minutes=0) <= time_difference <= timedelta(minutes=30):
            # Notify the user about the task
            self.notify_user(task_name, due_datetime)

    def notify_user(self, task_name, due_datetime):
        app_name = "Task Alarm"
        title = "Task Reminder"
        message = f"Task '{task_name}' is due at {due_datetime}!"
        notification.notify(app_name=app_name, title=title, message=message, timeout=10)
        messagebox.showinfo("Task Reminder", f"Task '{task_name}' is due at {due_datetime}!")




    def edit_task(self, task):
         task_name, task_ddate, topt_time, t_priority = task[1:]
        # Implement logic to edit the task based on the selected task details
        # You can open a new window or dialog for editing the task
        #pass
         user_db_name = f"{self.username}_tasks.db"
         user_conn = sqlite3.connect(user_db_name)
         user_cursor = user_conn.cursor()
         user_cursor.execute("DELETE FROM tasks WHERE task_name = ? AND task_ddate = ? AND topt_time = ? AND t_priority = ?", (task_name, task_ddate, topt_time, t_priority))
         user_conn.commit()
         user_conn.close()
         self.f6.destroy()
         create_task_page = Create_Tasks(self.root, self.username, task_name, task_ddate, topt_time, t_priority)
    
class Completed_tasks:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.f7 = Frame(self.root, width=1300, height=650)
        self.f7.place(x=0, y=0)
        self.mbgct = Image.open("assets/comp_tasks.png")
        self.mbgct = self.mbgct.resize((1300, 650))
        self.mbgct = ImageTk.PhotoImage(self.mbgct)
        self.mbgct_lbl21 = Label(self.f7, image=self.mbgct)
        self.mbgct_lbl21.image = self.mbgct
        self.mbgct_lbl21.place(x=0, y=0)
        self.back3 = Button(self.f7,text="BACK",bg="pink",font = font3,width = 13,command= self.goto_usp,cursor="hand2")
        self.back3.place(x=700,y=570)


        # Connect to the user's database
        user_db_name = f"{self.username}_tasks.db"
        user_conn = sqlite3.connect(user_db_name)
        user_cursor = user_conn.cursor()

        # Fetch completed tasks from the database
        user_cursor.execute("SELECT * FROM completed_tasks")
        completed_tasks = user_cursor.fetchall()

        user_conn.close()

        y = 20
        for task in completed_tasks:
            task_name, task_ddate, topt_time, t_priority = task[1:]
            task_label = Label(self.f7, text=f"Task: {task_name}, Due Date: {task_ddate}, Time: {topt_time}, Priority: {t_priority}")
            task_label.place(x=20, y=y)
            y += 40
    def goto_usp(self):
        self.f7.destroy()
        Mp =Main_Page(self.root,self.username)

class OverdueTasks:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.f8 = Frame(self.root, width=1300, height=650)
        self.f8.place(x=0, y=0)
        self.m4 = Image.open("assets/overdue.png")
        self.m4 = self.m4.resize((1300, 650))
        self.m4 = ImageTk.PhotoImage(self.m4)
        self.m4_lbl21 = Label(self.f8, image=self.m4)
        self.m4_lbl21.image = self.m4
        self.m4_lbl21.place(x=0, y=0)
        self.back4 = Button(self.f8, text="BACK", bg="pink", font=font3, width=13, command=self.goto_usp, cursor="hand2")
        self.back4.place(x=700, y=570)
        # Connect to the user's database
        user_db_name = f"{self.username}_tasks.db"
        user_conn = sqlite3.connect(user_db_name)
        user_cursor = user_conn.cursor()

        # Create overdue_tasks table if it doesn't exist
        user_cursor.execute('''
                            CREATE TABLE IF NOT EXISTS overdue_tasks(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            task_name TEXT NOT NULL,
                            task_ddate TEXT NOT NULL,
                            topt_time TEXT NOT NULL,
                            t_priority TEXT NOT NULL)
                            ''')
        user_cursor.execute("SELECT * FROM tasks")
        all_tasks = user_cursor.fetchall()

        # Get current datetime
        current_datetime = datetime.now()

        # Check for overdue tasks and insert them into the overdue_tasks table
        for task in all_tasks:
            task_name, task_ddate, topt_time, t_priority = task[1:]
            task_datetime = datetime.strptime(f"{task_ddate} {topt_time}", "%m/%d/%y %I:%M%p")
            if task_datetime < current_datetime:
                user_cursor.execute('INSERT INTO overdue_tasks (task_name, task_ddate, topt_time, t_priority) VALUES (?, ?, ?, ?)',
                                    (task_name, task_ddate, topt_time, t_priority))

        user_conn.commit()

        # Fetch overdue tasks from the overdue_tasks table
        user_cursor.execute("SELECT distinct * FROM overdue_tasks")
        overdue_tasks = user_cursor.fetchall()

        # Display overdue tasks
        y = 20
        for task in overdue_tasks:
            task_name, task_ddate, topt_time, t_priority = task[1:]
            task_label = Label(self.f8, text=f"Task: {task_name}, Due Date: {task_ddate}, Time: {topt_time}, Priority: {t_priority}")
            task_label.place(x=20, y=y)
            y += 40

        user_conn.close()

    def goto_usp(self):
        self.f8.destroy()
        Mp = Main_Page(self.root, self.username)


from tkinter import PhotoImage

class Create_Tasks:
    imageobj = []
    count = 0

    def __init__(self, root, username,task_name='',task_ddate="",topt_time="",t_priority=""):
        self.root = root
        self.username = username
        self.task_name = task_name
        self.task_ddate = task_ddate
        self.topt_time = topt_time
        self.t_priority = t_priority
        self.f5 = Frame(self.root, width=1300, height=650)
        self.f5.place(x=0, y=0)
        self.mbg31 = Image.open("assets/mainbg.png")
        self.mbg31 = self.mbg31.resize((1300, 650))
        self.mbg31 = ImageTk.PhotoImage(self.mbg31)
        self.mbg3_lbl21 = Label(self.f5, image=self.mbg31)
        self.mbg3_lbl21.image = self.mbg31
        self.mbg3_lbl21.place(x=0, y=0)

        gifimage = "assets/giphy2.gif"
        openimage = Image.open(gifimage)
        frames = openimage.n_frames
        self.imageobj = [PhotoImage(file=gifimage, format=f"gif -index {i}") for i in range(frames)]

        self.gif_label = Label(self.f5)
        self.gif_label.place(x=800, y=100,width=300,height=300)
        self.animation(0)

        self.tk1 = Label(self.f5, text="Task", font=("Arial", "15", "bold"))
        self.tk1.place(x=100, y=90)
        self.tk1_lbl = Entry(self.f5, font=("Arial", "15", "bold"), width=40)
        self.tk1_lbl.place(x=200, y=90)
        self.dd = Label(self.f5, text="Due Date", font=("Arial", "13", "bold"))
        self.dd.place(x=100, y=150)
        self.dd_en = DateEntry(self.f5, width=30, bg="darkblue", fg="white", borderwidth=2,font=("Arial", "15", "bold")) #year=2024, month=3,
                              # day=4, font=("Arial", "15", "bold"))
        self.dd_en.place(x=200, y=150)

        self.time_var = StringVar(self.f5)
        #self.time_var.set("12:00 AM")
        self.dtime = Label(self.f5, text="Due Time", font=("Arial", "13", "bold"))
        self.dtime.place(x=100, y=220)
        self.time_values = [f"{i:02d}:{j:02d}{am_pm}" for i in range(1, 13) for j in range(0, 60, 15) for am_pm in
                            ["AM", "PM"]]
        self.opt_menu = ttk.Combobox(self.f5, textvariable=self.time_var, values=self.time_values, font=font3)
        self.opt_menu.place(x=200, y=220)

        self.prilbl = Label(self.f5, text="Priority", font=("Arial", "13", "bold"))
        self.prilbl.place(x=100, y=270)
        self.priority_var = StringVar(self.f5)
        #self.priority_var.set("High")
        self.priority_option_menu = ttk.Combobox(self.f5, textvariable=self.priority_var,
                                                  values=["High", "Medium", "Low"])
        self.priority_option_menu.place(x=200, y=270)

        self.setbut = Button(self.f5, text="Set", bg='pink', font=font3,width=15,command=self.Set_tasks,cursor="hand2")
        self.setbut.place(x=330, y=350)

        self.back1 = Button(self.f5,text="BACK",bg="pink",font = font3,width = 13,command= self.goto_userpage,cursor="hand2")
        self.back1.place(x=150,y=350)
    
    def goto_userpage(self):
        self.f5.destroy()
        Mp =Main_Page(self.root,self.username)

    def Set_tasks(self):
        task_name = self.tk1_lbl.get()
        task_ddate = self.dd_en.get()
        topt_time = self.opt_menu.get()
        t_priority = self.priority_option_menu.get()

        if task_name != '' and task_ddate != '' and topt_time != '' and t_priority != '':
            # Connect to the user's database
            user_db_name = f"{self.username}_tasks.db"
            user_conn = sqlite3.connect(user_db_name)
            user_cursor = user_conn.cursor()
            # Create tasks table if it doesn't exist
            user_cursor.execute('''
                                CREATE TABLE IF NOT EXISTS tasks(
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                task_name TEXT NOT NULL,
                                task_ddate TEXT NOT NULL,
                                topt_time TEXT NOT NULL,
                                t_priority TEXT NOT NULL)
                                ''')
            # Insert task into tasks table
            user_cursor.execute('INSERT INTO tasks (task_name,task_ddate,topt_time, t_priority ) VALUES (?,?,?,?)',
                                (task_name, task_ddate, topt_time, t_priority))
            user_conn.commit()
            user_conn.close()
            messagebox.showinfo("Success", "Task created successfully.")
            self.tk1_lbl.delete(0, END)
            self.dd_en.delete(0, END)
            self.opt_menu.delete(0,END)
            self.priority_option_menu.delete(0,END)

        else:
            messagebox.showerror("Error", "Please fill in all the data fields.")

    def animation(self, count):
        if count < len(self.imageobj):
            new_image = self.imageobj[count]
            self.gif_label.configure(image=new_image)
            count += 1
            self.root.after(250, lambda: self.animation(count))
        else:
            count = 0
            self.animation(count)



confirmation = Confirmation_Page(root)
root.mainloop()


