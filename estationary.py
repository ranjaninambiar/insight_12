from Tkinter import *
import Tkinter as tk
import tkMessageBox as tm
import pickle
import datetime

# Declare some global variable to use across the functions

# Dictionary to control user login with Access level
#A:Admin ; C:Cashier
#M:Mobile view ; C:Computer view
#["username","password","Access level","View Mode"]
val=1
userlist = [["Adm_7","7300","A","M"],
        ["Adm_3","1000","A","C"],
        ["Sales_1","2000","C","M"],
        ["Sales_2","3000","C","C"]]
screen_type = "ICON"

#screen_type = "GENERAL"
# Main function to call to validate user login
def user_login(root):

    def sign_in():
        
        username = entry_username.get()
        password = entry_password.get()
        
        name_found = ' '
        name_check={}

        for name, pwd, role, type in userlist:
            name_check[name]=[pwd, role, type]

        if username in name_check.keys():
            #print username
            #print name_check[username]
            name_check[username][1]
            if name_check[username][0] == password:

                tm.showinfo("Login info", "Welcome "+str(username)+" !")
                root.withdraw()
                home_screen(root, name_check[username][1], name_check[username][2])

            else:
                tm.showerror("Login error", "Incorrect password ! ")

        else:
            tm.showerror("Login error", "Login!!!!  only as a admin user for new registration!!!!")
                


    user = tk.Frame(root, bg="blue")
    user.pack(side=tk.TOP, fill=tk.X)

    Home = tk.PhotoImage(file="e_stationery.gif")
    button4 = tk.Button(user,  image=Home, command=sign_in)
    button4.image= Home
    button4.grid(row=2,columnspan=6)



    userblock = tk.Label(user, text="Enter the captcha code below to continue", font=("Lucida Handwriting", 12), fg="white", bg="red")
    userblock.grid(row=3,columnspan=5, pady=2,padx=175)
    cap_user = tk.Label(user, text="Adm_3       1000", font=("Lucida Handwriting", 12), fg="white", bg="red")
    cap_user.grid(row=4,columnspan=5, pady=2,padx=175)
   
    label_username = tk.Label(user, text="Captcha Name", width=20, bg="red")
    label_password = tk.Label(user, text="Captcha no.", width=20, bg="red")
    label_username.grid(row=5,column=0, padx=10, pady=10)
    label_password.grid(row=5,column=3, padx=10, pady=10)

    entry_username = Entry(user)
    entry_password = Entry(user)
    entry_username.grid(row=5,column=1,padx=0)
    entry_password.grid(row=5,column=4,padx=0)

    New = tk.PhotoImage(file="signin.gif")
    button4 = tk.Button(user,  text="Sign In", image=New, command=sign_in)
    button4.image= New
    button4.grid(row=6,column=2)
    


# Method to build home screen with different options
# based on the user who logged in.  Admin role will have more options
# where as cashier will have limited options
def home_screen(root, role, screen_type):

    home = tk.Toplevel(root, bg="#FFF8DC")
    home.wm_title("Home Page")

    label21  = tk.Label(home, text="e-Archies", width=15, font=("Magneto", 30), fg="maroon", bg="white")
    label21.grid(row=0, columnspan=5)
    label31  = tk.Label(home, text="e-Stationery", width=27, font=("Lucida Handwriting", 24), fg="blue", bg="white")
    label31.grid(row=1, columnspan=5)

    dummy =  tk.Label(home, font=("Helvetica", 11), fg="#FFF8DC", bg="#FFF8DC")
    dummy.grid(row=2)

    if screen_type == "M":

        New        = PhotoImage(file=r"01_New.gif")
        Delete     = PhotoImage(file=r"02_Delete.gif")
        Modify     = PhotoImage(file=r"03_Modify.gif")
        NoSearch   = PhotoImage(file=r"04_Search.gif")
        NameSearch = PhotoImage(file=r"05_Search.gif")
        Logout     = PhotoImage(file=r"10_Logout.gif")
        InvReport  = PhotoImage(file=r"Inv_Report.gif")
        SalesReport= PhotoImage(file=r"Sales_Report.gif")


        
    else:

        # Product

        if role == "A":
            label1  = tk.Label(home, text="User Registration Module", font=("Lucida Handwriting", 12), fg="white", bg="blue")
            label1.grid(row=3,  column=0, pady=2)
            button1 = tk.Button(home, text="Register", width=13, bg="red", command=lambda: reg_create(home))
            button1.grid(row=3, column=1, padx=2, pady=2)
    

            b1t1 = ToolTip(button1, text='Create a new user login')


        dummy =  tk.Label(home, text="1",  font=("Helvetica", 11), fg="#FFF8DC", bg="#FFF8DC")
        dummy.grid(row=8)



# Class to handle mouse over text
class ToolTip:
    def __init__(self, master, text='Your text here', delay=500, **opts):
        self.master = master
        self._opts = {'anchor':'center', 'bd':1, 'bg':'lightyellow', 'delay':delay, 'fg':'black',\
                      'follow_mouse':0, 'font':None, 'justify':'left', 'padx':4, 'pady':2,\
                      'relief':'solid', 'state':'normal', 'text':text, 'textvariable':None,\
                      'width':0, 'wraplength':150}
        self.configure(**opts)
        self._tipwindow = None
        self._id = None
        self._id1 = self.master.bind("<Enter>", self.enter, '+')
        self._id2 = self.master.bind("<Leave>", self.leave, '+')
        self._id3 = self.master.bind("<ButtonPress>", self.leave, '+')
        self._follow_mouse = 0
        if self._opts['follow_mouse']:
            self._id4 = self.master.bind("<Motion>", self.motion, '+')
            self._follow_mouse = 1

    def configure(self, **opts):
        for key in opts:
            if self._opts.has_key(key):
                self._opts[key] = opts[key]
            else:
                KeyError = 'KeyError: Unknown option: "%s"' %key
                raise KeyError

    ##----these methods handle the callbacks on "<Enter>", "<Leave>" and "<Motion>"---------------##
    ##----events on the parent widget; override them if you want to change the widget's behavior--##

    def enter(self, event=None):
        self._schedule()

    def leave(self, event=None):
        self._unschedule()
        self._hide()

    def motion(self, event=None):
        if self._tipwindow and self._follow_mouse:
            x, y = self.coords()
            self._tipwindow.wm_geometry("+%d+%d" % (x, y))

    ##------the methods that do the work:---------------------------------------------------------##

    def _schedule(self):
        self._unschedule()
        if self._opts['state'] == 'disabled':
            return
        self._id = self.master.after(self._opts['delay'], self._show)

    def _unschedule(self):
        id = self._id
        self._id = None
        if id:
            self.master.after_cancel(id)

    def _show(self):
        if self._opts['state'] == 'disabled':
            self._unschedule()
            return
        if not self._tipwindow:
            self._tipwindow = tw = tk.Toplevel(self.master)
            # hide the window until we know the geometry
            tw.withdraw()
            tw.wm_overrideredirect(1)

            if tw.tk.call("tk", "windowingsystem") == 'aqua':
                tw.tk.call("::tk::unsupported::MacWindowStyle", "style", tw._w, "help", "none")

            self.create_contents()
            tw.update_idletasks()
            x, y = self.coords()
            tw.wm_geometry("+%d+%d" % (x, y))
            tw.deiconify()

    def _hide(self):
        tw = self._tipwindow
        self._tipwindow = None
        if tw:
            tw.destroy()

    ##----these methods might be overridden in derived classes:----------------------------------##

    def coords(self):
        # The tip window must be completely outside the master widget;
        # otherwise when the mouse enters the tip window we get
        # a leave event and it disappears, and then we get an enter
        # event and it reappears, and so on forever :-(
        # or we take care that the mouse pointer is always outside the tipwindow :-)
        tw = self._tipwindow
        twx, twy = tw.winfo_reqwidth(), tw.winfo_reqheight()
        w, h = tw.winfo_screenwidth(), tw.winfo_screenheight()
        # calculate the y coordinate:
        if self._follow_mouse:
            y = tw.winfo_pointery() + 20
            # make sure the tipwindow is never outside the screen:
            if y + twy > h:
                y = y - twy - 30
        else:
            y = self.master.winfo_rooty() + self.master.winfo_height() + 3
            if y + twy > h:
                y = self.master.winfo_rooty() - twy - 3
        # we can use the same x coord in both cases:
        x = tw.winfo_pointerx() - twx / 2
        if x < 0:
            x = 0
        elif x + twx > w:
            x = w - twx
        return x, y

    def create_contents(self):
        opts = self._opts.copy()
        for opt in ('delay', 'follow_mouse', 'state'):
            del opts[opt]
        label = tk.Label(self._tipwindow, **opts)
        label.pack()

# Method to handle product creation step
def reg_create(home):
    def login_btn_clicked():
        userno   = entry_userno.get()
        username = entry_username.get()
        shipad   = entry_shipad.get()
        bilad = entry_bilad.get()



        if userno == "" or username=="" or  shipad== "" or bilad== "":
            tm.showerror("User Creation Error!!!", "Enter all the values")
            prodc.focus()
        elif not userno.isdigit():
            tm.showerror("User  Creation Error!!!", "Check the contact no. field")
            prodc.focus()

    
        else:
            prodc.wm_title("User Creation")
            tm.showinfo("User Creation!!!", str(username)+" successfully created !")
            prodc.destroy()
            home.focus()
            pass

    prodc = tk.Toplevel(root, bg="white")
    prodc.minsize(540,350)
    var = IntVar()

    header1 = tk.Label(prodc, text="e-Archies",  font=("Magneto", 30), fg="maroon", bg="white")
    header1.grid(row=0,columnspan=5, padx=175)

    header2 = tk.Label(prodc, text="e-Stationery",  font=("Helvetica", 13), fg="white", bg="#696969")
    header2.grid(row=1, columnspan=5, padx=175, pady=2)
    

    entry_username = tk.Entry(prodc, width=25)
    entry_userno   = tk.Entry(prodc, width=25)
    entry_shipad    = tk.Entry(prodc, width=50)
    entry_bilad = tk.Entry(prodc, width=50)

    label_username = tk.Label(prodc, text="User Name",bg="orange", width=18)
    label_userno   = tk.Label(prodc, text="User Number",bg="orange", width=18)
    label_shipad    = tk.Label(prodc, text="Shipping Address",bg="orange", width=18)
    label_bilad = tk.Label(prodc, text="Billing Address",bg="orange", width=18)
    save   = Button(prodc, text="Save", command = login_btn_clicked, bg="lightgreen", width=8)
    cancel = Button(prodc, text="Cancel", command = prodc.destroy, bg="indianred", width=8)

    label_username.grid(row=3, column=0,sticky=W, pady=10, padx=10)
    label_userno.grid(row=4,column=0, sticky=W, pady=10, padx=10)
    label_shipad.grid(row=8, column=0,sticky=W, pady=10, padx=10)
    label_bilad.grid(row=9, column=0,sticky=W, pady=10, padx=10)
    entry_username.grid(row=3, column=1,sticky=W, pady=10, padx=10)
    entry_userno.grid(row=4, column=1,sticky=W, pady=10, padx=10)
    entry_shipad.grid(row=8, column=1,sticky=W, pady=10, padx=10)
    entry_bilad.grid(row=9, column=1,sticky=W, pady=10, padx=10)
    save.grid(row=10, column=2,sticky=E, pady=10)
    cancel.grid(row=10, column=3,sticky=E, pady=10)






# Initiate python process to trigger initial screen
if __name__ == "__main__":
    root = tk.Tk()
    user_login(root)
    root.mainloop()
    import earchiesdispaly
    import tcsmainproject

