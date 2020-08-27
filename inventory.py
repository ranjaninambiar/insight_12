import pickle
import os
import random
from Tkinter import *
from tkMessageBox import *
import time
val=0
#Administrator:val=1 for inventory;val=2 for salesmodule
#Salesperson:val=3
#'tcs1.log' : Inventory module
#'tcs2.log' : Sales module
r1=0#r1,r2 refresh list variables
r2=0#

#Administrator:Any username and password:admin123
#Salesperson:Any username and password:sales123

class alter:
    def create1(self,pno,pname,ptype,price,qty):#To create inventory module
        self.pno=pno
        self.pname=pname
        self.ptype=ptype
        self.price=price
        self.qty=qty
    def create2(self,date,pno,pname,qty,price):#To create sales module
        self.date=date
        self.pno=pno
        self.pname=pname
        self.qty=qty
        self.price=price
        self.tc=int(self.qty)*int(self.price)
    def disp1(self,r):#To display inventory module
        l=[self.pno,self.pname,self.ptype,self.price,self.qty]
        for i in range(len(l)):
            Label(root,text=l[i],bg="orange").grid(row=r,column=i)
            
    def disp2(self,r,e):#To display sales module
        l=[self.date,self.pno,self.pname,self.qty,self.price,self.tc]
        for i in range(len(l)):
                Label(root, text=l[i],bg="orange").grid(row=r,column=i+7-e*7)

def disp_a():
    Label(root,text='Do you want to access the inventory or the sales module?').grid(column=1)
    Button(root,text="Inventory",command=disp_c).grid(row=3,column=0)
    Button(root,text="Sales module",command=disp_d).grid(row=3,column=2)
obj=alter()
def b1():
    global r1,r2
    r1=r2
    root.destroy()
def disp_b():#To display inventory module
        global r2
        if r2==0:
            r2=1
        elif r2!=1:
            r2=3
        c=0
        try:
             a=open('tcs1.log','rb')
             a.close();c=1
        except:
             pass
        Button(root,text="Refresh list and date",command=b1).grid(row=5,column=6)
        if c==0:
            Label(root, text="No record exists",bg="orange").grid(row=6,column=1)
        else:
            l=["Product Number","Product Name","Product Type","Price","Quantity"]
            for i in range(len(l)):
                Label(root, text=l[i],bg="orange").grid(row=6,column=i)
            txt=['-'*16,'-'*14,'-'*14,'-'*5,'-'*8]
            for i in range(len(txt)):
                Label(root,text=txt[i],bg="orange").grid(row=7,column=i)
            Label(root,text='|',bg="orange").grid(row=6,column=6)
            Label(root,text='|',bg="orange").grid(row=7,column=6)
            a=open('tcs1.log','rb')
            r=8
            try:
                while True:
                    obj=pickle.load(a)
                    obj.disp1(r)
                    Label(root,text='|',bg="orange").grid(row=r,column=6)
                    r+=1
            except EOFError:
                a.close()
def disp_ci():#To display sales module for salesman
    global r2
    r2=0
    disp_c(1)
def disp_c(e=0):#To display sales module
    global r2
    if r2==0:
        r2=2
    elif r2!=2:
        r2=3
    c=0
    try:
         a=open('tcs2.log','rb')
         a.close();c=1
    except:
         c=0
    if c==0:
        Button(root,text="Refresh list and date",command=b1).grid(row=5,column=6-e*4)
        Label(root, text="No record exists",bg="orange").grid(row=6,column=8-e*6)
    else:
        Button(root,text="Refresh list and date",command=b1).grid(row=5,column=6-e)
        l=["Date","Product number","Product Name","Quantity","Price","Total Cost"]
        for i in range(len(l)):
            Label(root, text=l[i],bg="orange").grid(row=6,column=i+7-e*7)
        txt=['-'*16,'-'*14,'-'*14,'-'*5,'-'*8,'-'*8]
        for i in range(len(txt)):
            Label(root,text=txt[i],bg="orange").grid(row=7,column=i+7-e*7)
        a=open('tcs2.log','rb')
        r=8
        try:
            while True:
                obj=pickle.load(a)
                obj.disp2(r,e)
                r+=1
        except EOFError:
            a.close()
def c1():#To create inventory module
    root=Tk()
    root.title('Create')
    Label(root,text="Enter the product number : ").grid(row=0,column=0)
    Label(root,text="Enter the product name : ").grid(row=1,column=0)
    Label(root,text="Enter the product type : ").grid(row=2,column=0)
    Label(root,text="Enter its price : ").grid(row=3,column=0)
    Label(root,text="Enter the quantity : ").grid(row=4,column=0)
    pno=Entry(root)
    pname=Entry(root)
    price=Entry(root)
    qty=Entry(root)
    pno.grid(row=0,column=1)
    pname.grid(row=1,column=1)
    price.grid(row=3,column=1)
    qty.grid(row=4,column=1)
    v=IntVar()
    v.set(1)
    def p1():
        v.set(1)
    def p2():
        v.set(2)
    def p3():
        v.set(3)
    Radiobutton(root,text='sony',variable=v,value=1,command=p1).grid(row=2,column=1)
    Radiobutton(root,text='hp',variable=v,value=2,command=p2).grid(row=2,column=2)
    Radiobutton(root,text='samsung',variable=v,value=3,command=p3).grid(row=2,column=3)
    def create1():
        a=pno.get();b=pname.get();c=v.get();d=price.get();e=qty.get()
        root.destroy()
        if c==1:
            c='sony'
        elif c==2:
            c='hp'
        elif c==3:
            c='samsung'
        if a.isdigit()==True and b.isalnum()==True and c.isalpha()==True and d.isdigit()==True and e.isdigit()==True:
            obj.create1(a,b,c,d,e)
            a=open('tcs1.log','ab')
            pickle.dump(obj,a)
            a.close()
        else:
            if askyesno('Error','Invalid entry.Would you like to enter again?'):
                c1()
    Button(root,text="Create",command=create1).grid(column=1)
    root.mainloop()
def c2():#To create sales module
    root=Tk()
    root.title('Create')
    Label(root,text="Enter the date dd-mm-yy : ").grid(row=0,column=0)
    Label(root,text="Enter the product number : ").grid(row=1,column=0)
    Label(root,text="Enter the product brand : ").grid(row=2,column=0)
    Label(root,text="Enter the quantity : ").grid(row=3,column=0)
    Label(root,text="Enter its price : ").grid(row=4,column=0)
    da=Entry(root)
    pno=Entry(root)
    pname=Entry(root)
    qty=Entry(root)
    price=Entry(root)
    da.grid(row=0,column=1)
    pno.grid(row=1,column=1)                                                   
    pname.grid(row=2,column=1)
    qty.grid(row=3,column=1)
    price.grid(row=4,column=1)
    def create2():
        a=da.get()
        b=pno.get()
        c=pname.get()
        d=qty.get()
        e=price.get()
        root.destroy()
        e1=0
        e2=0
        if b.isdigit()==True and c.isalnum()==True and d.isdigit()==True and e.isdigit()==True:
            a1=open('tcs1.log','rb')
            while True:
                try:
                    obj=pickle.load(a1)
                    if obj.pno==b and int(obj.qty)<int(d):
                        if askyesno('Error','Required quantity not available. Would you like to enter again?'):
                            e1=1
                        else:
                            e1=2
                    if obj.pno==b:
                        e2=1
                except EOFError:
                    break
            a1.close()
            if e1==0 and e2==1:
                obj.create2(a,b,c,d,e)
                b1=open('tcs2.log','ab')
                pickle.dump(obj,b1)
                b1.close()
            if e1==1:
                c2()
            if e2==0:
                if askyesno('Error','Product not available in inventory. Would you like to enter again?'):
                    c2()
        else:
            if askyesno('Error','Invalid entry.Would you like to enter again?'):
                c2()
    Button(root,text="Create",command=create2).grid(column=1)
    root.mainloop()
def pnomod(x=0):#To modify product number
    root=Tk()
    root.title('Modify')
    Label(root,text="Enter the current product number").grid(row=0,column=0)
    Label(root,text="Enter the new product number").grid(row=1,column=0)
    m=Entry(root)
    n=Entry(root)
    m.grid(row=0,column=1)
    n.grid(row=1,column=1)
    def pnomod1():
        try:
            p=m.get()
            q=n.get()
            k=0
            if p.isdigit()==True and q.isdigit()==True:
                b=open('pseudo.log','wb')
                if x==0:
                    a=open('tcs1.log','rb')
                else:
                    a=open('tcs2.log','rb')
                while True:
                    try:
                        obj=pickle.load(a)
                        if obj.pno!=p:
                            pickle.dump(obj,b)
                        else:
                            obj.pno=q
                            pickle.dump(obj,b)
                            k=1
                    except EOFError:
                        break
                a.close()
                b.close()
                if k==1:
                    if x==0:                
                        os.remove('tcs1.log')
                        os.rename('pseudo.log','tcs1.log')
                    else:
                        os.remove('tcs2.log')
                        os.rename('pseudo.log','tcs2.log')
                    root.destroy()
                elif k==0:
                    if askyesno('Error','Given product number does not exist.Do you want to enter again?'):
                              root.destroy()
                              pnomod(x)
                    else:
                        root.destroy()
            else:
                root.destroy()
                if askyesno('Error','Invalid entry.Do you want to enter again?'):
                    pnomod(x)
        except :
            showerror('Error','No record exists')
            root.destroy()
        root.mainloop()
    Button(root,text="Modify",command=pnomod1).grid(row=2,column=1)
def pnamemod(x=0):#To modify name
    root=Tk()
    root.title('Modify')
    Label(root,text="Enter the current product number").grid(row=0,column=0)
    Label(root,text="Enter the new product name").grid(row=1,column=0)
    m=Entry(root)
    n=Entry(root)
    m.grid(row=0,column=1)
    n.grid(row=1,column=1)
    def pnamemod1():
        p=m.get()
        q=n.get()
        k=0
        try:
            if p.isdigit()==True and q.isalnum()==True:
                    b=open('pseudo.log','wb')
                    if x==0:
                        a=open('tcs1.log','rb')
                    else:
                        a=open('tcs2.log','rb')
                    while True:
                        try:
                            obj=pickle.load(a)
                            if obj.pno!=p:
                                pickle.dump(obj,b)
                            else:
                                obj.pname=q
                                pickle.dump(obj,b)
                                k=1
                        except EOFError:
                            break
                    a.close()
                    b.close()
                    if k==1:
                        root.destroy()
                        if x==0:
                            os.remove('tcs1.log')
                            os.rename('pseudo.log','tcs1.log')
                        else:
                            os.remove('tcs2.log')
                            os.rename('pseudo.log','tcs2.log')
                    elif k==0:
                        if askyesno('Error','Given product number does not exist.Do you want to enter again?'):
                                  root.destroy()
                                  pnamemod(x)
                        else:
                            root.destroy()
            else:
                root.destroy()
                if askyesno('Error','Invalid entry.Do you want to enter again?'):
                    pnamemod(x)
        except :
            showerror('Error','No record exists')
            root.destroy()
        root.mainloop()
    Button(root,text="Modify",command=pnamemod1).grid(row=2,column=1)
def ptypemod():#To modify product type
    root=Tk()
    root.title('Modify')
    Label(root,text="Enter the current product number").grid(row=0,column=0)
    Label(root,text="Enter the new product type").grid(row=1,column=0)
    m=Entry(root)
    m.grid(row=0,column=1)
    v=IntVar()
    v.set(0)
    def ptypemod1():
        p=m.get()
        q=v.get()
        k=0
        try:
            if p.isdigit()==True and q!=0:
                b=open('pseudo.log','wb')
                a=open('tcs1.log','rb')
                while True:
                    try:
                        obj=pickle.load(a)
                        if obj.pno!=m.get():
                            pickle.dump(obj,b)
                        else:
                            obj.ptype=c
                            pickle.dump(obj,b)
                            k=1
                    except EOFError:
                        break
                a.close()
                b.close()
                if k==1:
                    root.destroy()
                    os.remove('tcs1.log')
                    os.rename('pseudo.log','tcs1.log')
                elif k==0:
                    if askyesno('Error','Given product number does not exist.Do you want to enter again?'):
                            root.destroy()
                            ptypemod()
                    else:
                        root.destroy()
            else:
                root.destroy()
                if askyesno('Error','Invalid entry.Do you want to enter again?'):
                    ptypemod()
        except :
            showerror('Error','No record exists')
            root.destroy()
        root.mainloop()
    Button(root,text="Modify",command=ptypemod1).grid(row=3,column=1)    
def pricemod(x=0):#To modify price
    root=Tk()
    root.title('Modify')
    Label(root,text="Enter the current product number").grid(row=0,column=0)
    Label(root,text="Enter the new product price").grid(row=1,column=0)
    m=Entry(root)
    n=Entry(root)
    m.grid(row=0,column=1)
    n.grid(row=1,column=1)
    def pricemod1():
        try:
            p=m.get()
            q=n.get()
            k=0
            if p.isdigit()==True and q.isdigit()==True:
                b=open('pseudo.log','wb')
                if x==0:
                    a=open('tcs1.log','rb')
                else:
                    a=open("tcs2.log",'rb')
                while True:
                    try:
                        obj=pickle.load(a)
                        if obj.pno!=m.get():
                            pickle.dump(obj,b)
                        else:
                            obj.price=n.get()
                            obj.tc=int(obj.price)*int(obj.qty)
                            pickle.dump(obj,b)
                            k=1
                    except EOFError:
                        break
                a.close()
                b.close()
                if k==1:
                    root.destroy()
                    if x==0:
                        os.remove('tcs1.log')
                        os.rename('pseudo.log','tcs1.log')
                    else:
                        os.remove('tcs2.log')
                        os.rename('pseudo.log','tcs2.log')
                elif k==0:
                    if askyesno('Error','Given product number does not exist.Do you want to enter again?'):
                              root.destroy()
                              pricemod(x)
                    else:
                        root.destroy()
            else:
                root.destroy()
                if askyesno('Error','Invalid entry.Do you want to enter again?'):
                    pricemod(x)
        except :
            showerror('Error','No record exists')
            root.destroy()
        root.mainloop()
    Button(root,text="Modify",command=pricemod1).grid(row=2,column=1)
obj10=alter()
def qtymod(x=0):#To modify quantity
    try:
        root=Tk()
        root.title('Modify')
        Label(root,text="Enter the current product number").grid(row=0,column=0)
        Label(root,text="Enter the new quantity").grid(row=1,column=0)
        m=Entry(root)
        n=Entry(root)
        m.grid(row=0,column=1)
        n.grid(row=1,column=1)
        def qtymod1():
            p=m.get()
            q=n.get()
            k=0
            try:
                if p.isdigit()==True and q.isdigit()==True:
                    b=open('pseudo.log','wb')
                    if x==0:
                        a=open('tcs1.log','rb')
                        c=open("tcs2.log",'rb')
                    else:
                        a=open("tcs2.log",'rb')
                        c=open("tcs1.log",'rb')
                    while True:
                        try:
                            obj=pickle.load(a)
                            if obj.pno!=m.get():
                                pickle.dump(obj,b)
                            else:
                                if x==0:
                                    obj.qty=n.get()
                                    obj.tc=int(obj.price)*int(obj.qty)
                                    pickle.dump(obj,b)
                                    k=1
                                else:
                                    while True:
                                        try:
                                            obj10=pickle.load(c)
                                            if obj10.pno==p:
                                                break
                                        except EOFError:
                                            break
                                    if int(obj10.qty)>=int(q):
                                        obj.qty=n.get()
                                        obj.tc=int(obj.price)*int(obj.qty)
                                        pickle.dump(obj,b)
                                        k=1
                                    else:
                                        k=3
                                        if askyesno('Error','Given quanity not available in inventory.Do you want to enter again?'):
                                            k=4
                                        else:
                                            pass
                        except EOFError:
                            break
                    a.close()
                    b.close()
                    c.close()
                    if k==1:
                        root.destroy()
                        if x==0:
                            os.remove('tcs1.log')
                            os.rename('pseudo.log','tcs1.log')
                        else:
                            os.remove('tcs2.log')
                            os.rename('pseudo.log','tcs2.log')
                    elif k==0:
                        if askyesno('Error','Given product number does not exist.Do you want to enter again?'):
                                  root.destroy()
                                  qtymod(x)
                        else:
                            root.destroy()
                    elif k==3:
                        root.destroy()
                    elif k==4:
                        root.destroy()
                        qtymod(1)
                else:
                    root.destroy()
                    if askyesno('Error','Invalid entry.Do you want to enter again?'):
                        qtymod(x)
            except :
                showerror('Error','No record exists')
                root.destroy()
            root.mainloop()
        Button(root,text="Modify",command=qtymod1).grid(row=2,column=1)
    except:
        pass
def pdate():#To modify date
    root=Tk()
    root.title('Date')
    Label(root,text="Enter the current product number").grid(row=0,column=0)
    Label(root,text="Enter the new date").grid(row=1,column=0)
    m=Entry(root)
    n=Entry(root)
    m.grid(row=0,column=1)
    n.grid(row=1,column=1)
    def pdate1():
        try:
            b=open('pseudo.log','wb')
            a=open("tcs2.log",'rb')
            while True:
                try:
                    obj=pickle.load(a)
                    if obj.pno!=m.get():
                        pickle.dump(obj,b)
                    else:
                        obj.date=n.get()
                        pickle.dump(obj,b)
                except EOFError:
                    break
            a.close()
            b.close()
            os.remove('tcs2.log')
            os.rename('pseudo.log','tcs2.log')
        except :
            showerror('Error','No record exists')
        root.destroy()
        root.mainloop()
    Button(root,text="Modify",command=pdate1).grid(row=2,column=1)

def mod_i():#Modify Inventory
    root=Tk()
    root.title('Modify')
    v=IntVar()
    v.set(0)
    Label(root,text="Click the field to be modified").grid(column=1,columnspan=2)
    def p1():
        v.set(1)
    def p2():
        v.set(2)
    def p3():
        v.set(3)
    def p4():
        v.set(4)
    def p5():
        v.set(5)
    Radiobutton(root,text='Product number',variable=v,value=1,command=p1).grid(row=1,column=0)
    Radiobutton(root,text='Product name',variable=v,value=2,command=p2).grid(row=1,column=1)
    Radiobutton(root,text='Product type',variable=v,value=3,command=p3).grid(row=1,column=2)
    Radiobutton(root,text='Price',variable=v,value=2,command=p4).grid(row=1,column=3)
    Radiobutton(root,text='Quantity',variable=v,value=3,command=p5).grid(row=1,column=4)
    def mod1():
        w=v.get()
        if w!=0:
            root.destroy()
            if w==1:
                pnomod()
            if w==2:
                pnamemod()
            if w==3:
                ptypemod()
            if w==4:
                pricemod()
            if w==5:
                qtymod()
        else:
            root.destroy()
            if askyesno('Error','Nothing chosen.Do you want to try again?'):
                    mod_i()
    Button(root,text="Click here to continue",command=mod1).grid(row=3,column=1)
    root.mainloop()
def mod_s():#Modify Sales module
    root=Tk()
    root.title('Modify')
    v=IntVar()
    v.set(0)
    Label(root,text="Click the field to be modified").grid(column=1,columnspan=2)
    def p1():
        v.set(1)
    def p2():
        v.set(2)
    def p3():
        v.set(3)
    def p4():
        v.set(4)
    def p5():
        v.set(5)
    Radiobutton(root,text='Date',variable=v,value=1,command=p1).grid(row=1,column=0)
    Radiobutton(root,text='Product number',variable=v,value=2,command=p2).grid(row=1,column=1)
    Radiobutton(root,text='Product name',variable=v,value=3,command=p3).grid(row=1,column=2)
    Radiobutton(root,text='Quantity',variable=v,value=2,command=p4).grid(row=1,column=3)
    Radiobutton(root,text='Price',variable=v,value=3,command=p5).grid(row=1,column=4)
    def mod2():
        w=v.get()
        if w!=0:
            root.destroy()
            if w==1:
                pdate()
            if w==2:
                pnomod(1)
            if w==3:
                pnamemod(1)
            if w==4:
                qtymod(1)
            if w==5:
                pricemod(1)
        else:
            root.destroy()
            if askyesno('Error','Nothing chosen.Do you want to try again?'):
                    mod_s()
    Button(root,text="Click here to continue",command=mod2).grid(row=3,column=1)
    root.mainloop()
def delete(x=0):
    root=Tk()
    root.title('Delete')
    Label(root,text="Enter the product number of the product to be deleted").grid(row=0,column=0)
    m=Entry(root)
    m.grid(row=1,column=0)
    def delete1():
        try:
            j=0
            b=open('pseudo.log','wb')
            if x==0:
                a=open('tcs1.log','rb')
            else:
                a=open('tcs2.log','rb')
            while True:
                try:
                    obj=pickle.load(a)
                    if obj.pno!=m.get():
                        pickle.dump(obj,b)
                except EOFError:
                    break
            a.close()
            b.close()
            if x==0:
                a=open('tcs1.log')
            else:
                a=open('tcs2.log')
            b=open('pseudo.log')
            if a.read()==b.read():
                j=1
                if not askyesno('Error','Record not found.Do you want to enter another number?'):
                    root.destroy()
            a.close();b.close()
            if j==0:
                root.destroy()
                if x==0:
                    os.remove('tcs1.log')
                    os.rename('pseudo.log','tcs1.log')
                else:
                    os.remove('tcs2.log')
                    os.rename('pseudo.log','tcs2.log')                
        except :
            showerror("Error","File does not exist")
            root.destroy()
        root.mainloop()
    Button(root,text="Delete",command=delete1).grid(row=2,column=0)
def delete_s():
    delete(1)
def search():
    root=Tk()
    root.title('Search')
    Label(root,text="Do you want to search on product number or product name?").grid(row=0,column=0,columnspan=2)
    def pnosearch():
        global j,k
        j=1;k=0
        Label(root,text="Enter a product number").grid(row=3,column=0)
        m=Entry(root)
        m.grid(row=3,column=1)
        def s1a():
            try:
                a=open('tcs1.log','rb')
                while True:
                    try:
                        obj=pickle.load(a)
                        if obj.pno==m.get():
                            global k
                            k=1
                            l=["Product Number","Product Name","Product Type","Price","Quantity"]
                            for i in range(len(l)):
                                Label(root, text=l[i]).grid(row=5,column=i)
                            txt=['-'*16,'-'*14,'-'*14,'-'*5,'-'*8]
                            for i in range(len(txt)):
                                Label(root,text=txt[i]).grid(row=6,column=i)
                            l=[obj.pno,obj.pname,obj.ptype,obj.price,obj.qty]
                            for i in range(len(l)):
                                    Label(root, text=l[i]).grid(row=7,column=i)
                    except EOFError:
                        if k==0:
                            root.destroy()
                            if askyesno('Error','No match found.Do you want to search again?'):
                                search()
                        break
            except:
                Label(root,text="No record exists",bg='orange').grid(column=1)
            def search1():
                root.destroy()
                search()
            if k==1:
                Button(root,text="Search again",command=search1).grid(row=8,column=5)
            root.mainloop()
        Button(root,text="Search",command=s1a).grid(row=4,column=1)
    def pnamesearch():
        global j,k
        j=1;k=0
        Label(root,text="Enter a product name  ").grid(row=3,column=0)
        m=Entry(root)
        m.grid(row=3,column=1)
        def s1b():
            try:
                a=open('tcs1.log','rb')
                while True:
                    try:
                        obj=pickle.load(a)
                        if obj.pname==m.get():
                            global k
                            k=1
                            l=["Product Number","Product Name","Product Type","Price","Quantity"]
                            for i in range(len(l)):
                                Label(root, text=l[i]).grid(row=5,column=i)
                            txt=['-'*16,'-'*14,'-'*14,'-'*5,'-'*8]
                            for i in range(len(txt)):
                                Label(root,text=txt[i]).grid(row=6,column=i)
                            l=[obj.pno,obj.pname,obj.ptype,obj.price,obj.qty]
                            for i in range(len(l)):
                                    Label(root, text=l[i]).grid(row=7,column=i)
                    except EOFError:
                             if k==0:
                                root.destroy()
                                if askyesno('Error','No match found.Do you want to search again?'):
                                    search()
                             break
            except:
                Label(root,text="File does not exist").grid(column=1)
            def search1():
                root.destroy()
                search()
            if k==1:
                Button(root,text="Search again",command=search1).grid(row=8,column=5)
            root.mainloop()
        Button(root,text="Search",command=s1b).grid(row=4,column=1)
    Button(root,text="Product number",command=pnosearch).grid(row=2,column=0)
    Button(root,text="Product name  ",command=pnamesearch).grid(row=2,column=1)
    def close():#To exit for loop
        global j
        j=0
        root.destroy()
    root.protocol('WM_DELETE_WINDOW', close)  # To override close button

def final():#To tally the required data by the end of the day
    obj1=alter()
    try:
        a=open('tcs1.log','rb')
        b=open('tcs2.log','rb')
        a1={};b1={};stk={};s1=0;s2=0
        while True:
            try:
                obj=pickle.load(a)
                a1[obj.pname]=obj.qty
            except:
                break
        while True:
            try:
                obj1=pickle.load(b)
                b1[obj1.pname]=obj1.qty
                s1+=int(obj1.price)*int(obj1.qty)
                s2+=int(obj1.tc)
            except:
                break
        root=Tk()
        root.title('Report')
        root.config(bg='light green')
        Label(root,text="Product name",bg='light green').grid(row=0,column=0)
        Label(root,text="Current stock",bg='light green').grid(row=0,column=1)
        for i in range(2):
            Label(root,text='-'*14,bg='light green').grid(row=1,column=i)
        r=2
        for i in a1:
            stk[i]=int(a1[i])-int(b1[i])
            Label(root,text=i,bg='light green').grid(row=r,column=0)
            Label(root,text=stk[i],bg='light green').grid(row=r,column=1)
            r+=1
        if s1==s2:
            Label(root,text="Price tallied",bg='light green').grid(column=1)
        else:
            Label(root,text="Price not tallied",bg='light green').grid(column=1)
        root.mainloop()
    except:
        pass
q=0
def login(x=0):
    root1=Tk()
    root1.title('Login page')
    Label(root1,text="Login").grid(row=0,column=1)
    Label(root1,text="Username").grid(row=1,column=0)
    Label(root1,text="Password").grid(row=2,column=0)
    un1=Entry(root1)
    pw=Entry(root1,show='*')
    un1.grid(row=1,column=1)
    pw.grid(row=2,column=1)
    def cpw():
        global un
        un=un1.get()
        if x==0:
            if pw.get()=='admin123':
                root1.destroy()
            else:
                if not askyesno('Error','Incorrect password.Do you want to enter again?'):
                    root1.destroy()
                    home()
        elif x==1:
            if pw.get()=='sales123':
                root1.destroy()
            else:
                if not askyesno('Error','Incorrect password.Do you want to enter again?'):
                    root1.destroy()
                    home()
        root1.mainloop()
    Button(root1,text='login',command=cpw).grid(row=3,column=1)
    def close():
        global val
        val=3
        root1.destroy()
    root1.protocol('WM_DELETE_WINDOW', close)  # To override close button
def sales():
    login(1)

def home():
    global val
    val=0
    root=Tk()
    root.config(bg='orange')
    root.title('login page')
    Label(root,text='e-Archies',bg='orange',font='Magneto').grid(row=0,column=0,columnspan=5)
    time1=time.asctime()
    Label(root,text=time1,bg='orange').grid(row=2,column=3,columnspan=2)
    rep1='-'*100
    Label(root,text=rep1,bg='orange').grid(row=1,columnspan=10)
    Label(root,text='e-Stationary',bg='orange',font='LucidaHandwriting').grid(row=2,column=0,columnspan=5)
    a=PhotoImage(file="e_stationery.gif")
    Label(root,image=a,bg='orange').grid(row=3,column=0,rowspan=4,columnspan=2,sticky=E)
    b=PhotoImage(file="bgdesign.gif")
    Label(root,image=b,bg='orange').grid(row=3,column=2,rowspan=4,columnspan=2,sticky=W)
    Label(root,text='Choose your designation',bg='orange',font='Times 16').grid(row=4,column=2,columnspan=2)
    def admin1():
        root.destroy()
        global val
        val=1
        login()
    def sales1():
        root.destroy()
        global val
        val=2
        sales()
    Button(root,text="Administrator",command=admin1,bg='grey').grid(row=5,column=2)
    Button(root,text='SalesPerson',command=sales1,bg='grey').grid(row=5,column=3)
    root.mainloop()
home()

i=0
r1=0
g1=0
if val==1:
    while i==0:
        root=Tk()
        root.title('Admin')
        root.config(bg='orange')
        Label(root,text='e-Archies',bg='orange',font='Times 16').grid(row=0,column=4,columnspan=4)
        a=PhotoImage(file='create.gif')
        b=PhotoImage(file='modify.gif')
        c=PhotoImage(file='delete.gif')
        d=PhotoImage(file='display.gif')
        e=PhotoImage(file='search.gif')
        if g1==0:
            showinfo('Login','Logged in as administrator')
            g1=1
        time1=time.asctime()
        Label(root,text=time1,bg='orange').grid(row=0,column=10,columnspan=2)
        username='Welcome '+un
        Label(root,text=username,bg='orange',font='Times 16').grid(row=0,column=0,columnspan=2,sticky=W)
        #Inventory module
        Label(root,text='Inventory module',font='Times 16',bg='orange').grid(row=1,column=2,columnspan=2)
        Label(root,image=a,bg='orange').grid(row=2,column=0,padx=5)
        Label(root,image=b,bg='orange').grid(row=2,column=1,padx=5)
        Label(root,image=c,bg='orange').grid(row=2,column=2)
        Label(root,image=d,bg='orange').grid(row=2,column=3)
        Label(root,image=e,bg='orange').grid(row=2,column=4,sticky=W)
        Button(root,text='Create',command=c1,bg='grey').grid(row=3,column=0)
        Button(root,text='Modify',command=mod_i,bg='grey').grid(row=3,column=1)
        Button(root,text='Delete',command=delete,bg='grey').grid(row=3,column=2)
        Button(root,text='Display',command=disp_b,bg='grey').grid(row=3,column=3)
        Button(root,text='Search',command=search,bg='grey').grid(row=3,column=4)
        
        #Sales module
        Label(root,text='Sales module',font='Times 16',bg='orange').grid(row=1,column=8,columnspan=2)
        Label(root,text=' '*50,bg='orange').grid(row=2,column=6,padx=5)
        Label(root,image=a,bg='orange').grid(row=2,column=7,padx=5)
        Label(root,image=b,bg='orange').grid(row=2,column=8,padx=5)
        Label(root,image=c,bg='orange').grid(row=2,column=9,padx=5)
        Label(root,image=d,bg='orange').grid(row=2,column=10,padx=5)
        Button(root,text='Create',command=c2,bg='grey').grid(row=3,column=7)
        Button(root,text='Modify',command=mod_s,bg='grey').grid(row=3,column=8)
        Button(root,text='Delete',command=delete_s,bg='grey').grid(row=3,column=9)
        Button(root,text='Display',command=disp_c,bg='grey').grid(row=3,column=10)
        
        if r1==1:#Refresh operation
            disp_b()
        elif r1==2:#Refresh operation
            disp_c()
        elif r1==3:#Refresh operation
            disp_b()
            disp_c()
        Button(root,text='Process report',command=final).grid(row=2,column=6)
        def close():#To exit while loop
            global i
            i=1
            root.destroy()
        root.protocol('WM_DELETE_WINDOW', close)  # To override close button
        root.mainloop()
if val==2:
    while i==0:
        root=Tk()
        root.title('Salesperson')
        root.config(bg='orange')
        Label(root,text='e-Archies',bg='orange',font='Magneto').grid(row=0,column=2,columnspan=3,sticky=W,padx=90)
        a=PhotoImage(file='create.gif')
        b=PhotoImage(file='modify.gif')
        d=PhotoImage(file='display.gif')
        if g1==0:
            showinfo('Login','Logged in as salesperson')
            g1=1
        time1=time.asctime()
        Label(root,text=time1,bg='orange').grid(row=0,column=5,columnspan=3)
        username='Welcome '+un
        Label(root,text=username,bg='orange',font='Times 14').grid(row=0,column=0,columnspan=2,sticky=W)
        #Sales module
        Label(root,text='Sales module',font='Times 16',bg='orange').grid(row=1,column=2,columnspan=2,sticky=W)
        Label(root,image=a,bg='orange').grid(row=2,column=1,padx=5)
        Label(root,image=b,bg='orange').grid(row=2,column=2,padx=5)
        Label(root,image=d,bg='orange').grid(row=2,column=3,padx=5)
        Button(root,text='Create',command=c2,bg='grey').grid(row=3,column=1)
        Button(root,text='Modify',command=mod_s,bg='grey').grid(row=3,column=2)
        Button(root,text='Display',command=disp_ci,bg='grey').grid(row=3,column=3)
        if r1==2:#Refresh operation
            disp_ci()
        def close():
            global i
            i=1
            root.destroy()
        root.protocol('WM_DELETE_WINDOW', close)  # To override close button
        root.mainloop()




















