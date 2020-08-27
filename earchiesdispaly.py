import sys
import os
from Tkinter import *
import Tkinter
import ttk
from ttk import Combobox
import Tkinter as tk
from Tkinter import Tk, StringVar
import tkMessageBox 
import random
import time
import datetime



root=Tk()
root.geometry("1024x768+0+0")
root.title("e-archies")
root.configure(background='red')

def Exit():
    qExit= tkMessageBox.askyesno("e-archies","Do you want to exit the system")
    if qExit >0:
        root.destroy()
        return
def Reset():
    Combobox.set("")
    Tax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CustomerName.set("")
    CustomerPhone.set("")
    CustomerEmail.set("")
    CustomerRef.set("")

def OrderRef():
    Refpay = random.randint(30000, 505000)
    Refpaid= ("AR" + str(Refpay))
    CustomerRef.set(Refpaid)

def CostofOrder():
    Qty1=float(QtyPendrive.get())
    Qty2=float(QtyMobile.get())
    Qty3=float(QtyCalculator.get())
    Qty4=float(QtyPowerBank.get())
    Qty5=float(QtybluetoothHeadset.get())

    UnitPrice1=float(UnitPricePendrive.get())
    UnitPrice2=float(UnitPriceMobile.get())
    UnitPrice3=float(UnitPriceCalculator.get())
    UnitPrice4=float(UnitPricePowerBank.get())
    UnitPrice5=float(UnitPricebluetoothHeadset.get())

    Cost1= str(Qty1 * 150)
    Cost2= str(Qty2 * 50000)
    Cost3= str(Qty3 * 859)
    Cost4= str(Qty4 * 8000)
    Cost5= str(Qty5 * 900 )

    CostofPendrive.set(Cost1)
    CostofMobile.set(Cost2)
    CostofCalculator.set(Cost3)
    CostofPowerBank.set(Cost4)
    CostofbluetoothHeadset.set(Cost5)


    CostPendrive1= (Qty1 * UnitPrice1)
    CostMobile2= (Qty2 * UnitPrice2)
    CostCalculator3= (Qty3 * UnitPrice3)
    CostPowerBank4= (Qty4 * UnitPrice4)
    CostbluetoothHeadset5= (Qty5 * UnitPrice5)

    AllTax = (   (Qty1 * UnitPrice1)+(Qty2 * UnitPrice2)+(Qty3 * UnitPrice3)+(Qty4 * UnitPrice4)+(Qty5 * UnitPrice5) )
    TaxTotal= "Rs" , str('% 2f' % ((AllTax)*0.05))
    Tax.set(TaxTotal)

    SubTotalPay = "Rs" , str('% 2f' % (AllTax))
    SubTotal.set(SubTotalPay)

    TotalPay = "Rs" , str('% 2f' % (AllTax  + ((AllTax)  *  0.05)))
    TotalCost.set(TotalPay)
    return

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Combobox=StringVar()
Tax=StringVar()
SubTotal=StringVar()
TotalCost=StringVar()
Pendrive=StringVar()
USBFlashDriveCard =StringVar()
bluetoothHeadset =StringVar()
Mobile =StringVar()
PowerBank =StringVar()
Calculator = StringVar()
USBCarCharger = StringVar()
Loudspeaker = StringVar()
CustomerName=StringVar()
CustomerPhone=StringVar()
CustomerEmail=StringVar()
DateofOrder=StringVar()
Discount=StringVar()
TimeofOrder=StringVar()
CustomerRef=StringVar()
QtyPendrive=StringVar()
QtyMobile=StringVar()
QtyCalculator=StringVar()
QtyPowerBank=StringVar()
QtybluetoothHeadset=StringVar()
UnitPricePendrive=StringVar()
UnitPriceMobile=StringVar()
UnitPriceCalculator=StringVar()
UnitPricePowerBank=StringVar()
UnitPricebluetoothHeadset=StringVar()
CostofPendrive=StringVar()
CostofMobile=StringVar()
CostofCalculator=StringVar()
CostofPowerBank=StringVar()
CostofbluetoothHeadset=StringVar()


Discount.set(0)
QtyPendrive.set(0)
QtyMobile.set(0)
QtyCalculator.set(0)
QtyPowerBank.set(0)
QtybluetoothHeadset.set(0)
UnitPricePendrive.set(150)
UnitPriceMobile.set(50000)
UnitPriceCalculator.set(859)
UnitPricePowerBank.set(8000)
UnitPricebluetoothHeadset.set(900)
CostofPendrive.set(0)
CostofMobile.set(0)
CostofCalculator.set(0)
CostofPowerBank.set(0)
CostofbluetoothHeadset.set(0)
TimeofOrder.set(time.strftime("%d/%m/%y"))
DateofOrder.set(time.strftime("%H:%M:%S"))

#--------------------------------------------------------------------------------------------------------------------------------





Tops = Frame (root, width = 1350 ,height=50, bd=16 ,  relief="raise")
Tops.pack(side=TOP)
LF= Frame (root, width = 700 , height=650, bd=16 ,  relief="raise")
LF.pack(side=LEFT)
RF= Frame (root, width = 600 , height=650,  bd=16,  relief="raise")
RF.pack(side=RIGHT)

Tops.configure(background="blue")
LF.configure(background="red")
RF.configure(background="red")

LeftInsideLF=Frame (LF, width = 700 , height=100,  bd= 8, relief="raise")
LeftInsideLF.pack(side=TOP)
LeftInsideLFLF=Frame (LF, width = 700 , height=400,  bd= 8, relief="raise")
LeftInsideLFLF.pack(side=LEFT)

RightInsideLF=Frame (RF, width = 604 , height=200,  bd= 8, relief="raise")
RightInsideLF.pack(side=TOP)
RightInsideLFLF=Frame (RF, width = 306 , height=400,  bd= 8, relief="raise")
RightInsideLFLF.pack(side=LEFT)
RightInsideRFRF=Frame (RF, width = 300 , height=400,  bd= 8, relief="raise")
RightInsideRFRF.pack(side=RIGHT)

lblInfo = Label(Tops, font=('Magneto', 50, 'bold'), text=" E-ARCHIES",bd=10,anchor='w')
lblInfo.grid(row =0, column=0)
#---------------------------------------------------------------------------------------------------------------------------------------------------
lblCustomerName= Label(LeftInsideLF ,font=('Magneto', 12, 'bold'),text="Customer Name", fg="blue", bd=10, anchor="w")
lblCustomerName.grid(row =0, column=0)
txtCustomerName = Entry(LeftInsideLF ,font=('Magneto', 12, 'bold'), bd=20, width=43, fg="white",bg="blue", justify='left', textvariable=CustomerName)
txtCustomerName.grid(row =0, column=1)
lblCustomerPhone= Label(LeftInsideLF ,font=('Magneto', 12, 'bold'),text="Customer Phone", fg="blue", bd=10, anchor="w")
lblCustomerPhone.grid(row =1, column=0)
txtCustomerPhone = Entry(LeftInsideLF ,font=('Magneto', 12, 'bold'), bd=20, width=43, fg="white",bg="blue", justify='left', textvariable=CustomerPhone)
txtCustomerPhone.grid(row =1, column=1)
lblCustomerEmail= Label(LeftInsideLF ,font=('Magneto', 12, 'bold'),text="Customer Email", fg="blue", bd=10, anchor="w")
lblCustomerEmail.grid(row =2, column=0)
txtCustomerEmail = Entry(LeftInsideLF ,font=('Magneto', 12, 'bold'), bd=20, width=43,fg="white", bg="blue", justify='left', textvariable=CustomerEmail)
txtCustomerEmail.grid(row =2, column=1)

#-----------------------------------------------------------------------------------------------------
lblDateofOrder= Label(RightInsideLF ,font=('Magneto', 12, 'bold'),text="Time of Order", fg="blue", bd=10,anchor="w")
lblDateofOrder.grid(row =0, column=0)
txtDateofOrder = Entry(RightInsideLF ,font=('Magneto', 12, 'bold'), bd=20, width=43, fg="white",bg="blue", justify='left', textvariable=DateofOrder)
txtDateofOrder.grid(row =0, column=1)
lblTimeofOrder= Label(RightInsideLF ,font=('Magneto', 12, 'bold'),text="Date of Order", fg="blue", bd=10,anchor="w")
lblTimeofOrder.grid(row =1, column=0)
txtTimeofOrder = Entry(RightInsideLF ,font=('Magneto', 12, 'bold'), bd=20, width=43,fg="white", bg="blue", justify='left', textvariable=TimeofOrder)
txtTimeofOrder.grid(row =1, column=1)
lblCustomerRef= Label(RightInsideLF ,font=('Magneto', 12, 'bold'),text="Customer Ref", fg="blue", bd=10,anchor="w")
lblCustomerRef.grid(row =2, column=0)
txtCustomerRef = Entry(RightInsideLF ,font=('Magneto', 12, 'bold'), bd=20, width=43, fg="white",bg="blue", justify='left', textvariable=CustomerRef)
txtCustomerRef.grid(row =2, column=1)





#-----------------------------------------------------
lblMethodofPayment=Label(RightInsideLFLF ,font=('Magneto', 12, 'bold'),text="Method of Payment", fg="blue", bd=16, anchor='w')
lblMethodofPayment.grid(row =0, column=0)
cmdMethodofPayment=ttk.Combobox(RightInsideLFLF ,font=('Magneto', 10, 'bold'), state='readonly', width=10)
cmdMethodofPayment['value']=(  'Cash', 'Debit Card', 'Visa Card', 'Master Card')
cmdMethodofPayment.current(0)
cmdMethodofPayment.grid(row =0, column=1)
lblDiscount=Label(RightInsideLFLF ,font=('Magneto', 12, 'bold'),text="Discount", fg="blue", bd=16,  anchor='w')
lblDiscount.grid(row =1, column=0)
txtDiscount=Entry(RightInsideLFLF ,font=('Magneto', 12, 'bold'), bd=16, width=12,fg="white", bg="blue", justify='left', textvariable=Discount)
txtDiscount.grid(row =1, column=1)
lblTax=Label(RightInsideLFLF ,font=('Magneto', 12, 'bold'),text="Tax", fg="blue", bd=16,  anchor='w')
lblTax.grid(row =2, column=0)
txtTax=Entry(RightInsideLFLF ,font=('Magneto', 12, 'bold'), bd=16, width=12, fg="white",bg="blue", justify='left', textvariable=Tax)
txtTax.grid(row =2, column=1)
lblSubTotal= Label(RightInsideLFLF ,font=('Magneto', 12, 'bold'),text="Sub Total", fg="blue", bd=16,anchor="w")
lblSubTotal.grid(row =3, column=0)
txtSubTotal = Entry(RightInsideLFLF ,font=('Magneto', 12, 'bold'), bd=16, width=12, fg="white",bg="blue", justify='left', textvariable=SubTotal)
txtSubTotal.grid(row =3, column=1)
lblTotalCost= Label(RightInsideLFLF ,font=('Magneto', 12, 'bold'),text="Total Cost", fg="blue", bd=16,anchor="w")
lblTotalCost.grid(row =4, column=0)
txtTotalCost = Entry(RightInsideLFLF ,font=('Magneto', 12, 'bold'), bd=16, width=12, fg="white",bg="blue", justify='left', textvariable=TotalCost)
txtTotalCost.grid(row =4, column=1)
#------------------------------------------------------------------------------------------------------------------------------------------------------
lblItemOrder = Label(LeftInsideLFLF ,font=('Magneto', 12, 'bold'),text="Item Order", fg="blue", bd=20)
lblItemOrder.grid(row =0, column=0)
lblQty = Label(LeftInsideLFLF ,font=('Magneto', 12, 'bold'),text="Qty", fg="blue", bd=20)
lblQty.grid(row =0, column=1)
lblUnitPrice = Label(LeftInsideLFLF ,font=('Magneto', 12, 'bold'),text="Unit Price", fg="blue", bd=20)
lblUnitPrice.grid(row =0, column=2)
lblCostofItem = Label(LeftInsideLFLF ,font=('Magneto', 12, 'bold'),text="Cost of Item", fg="blue", bd=20)
lblCostofItem.grid(row =0, column=3)
#-----------------------------------------------------------------------------------------------------------------------------------------------------
lblPendrive = Label(LeftInsideLFLF ,font=('Magneto', 12, 'bold'),text="Pendrive", fg="blue", bd=20)
lblPendrive.grid(row =1, column=0)
lblMobile = Label(LeftInsideLFLF ,font=('Magneto', 12, 'bold'),text="Mobile", fg="blue", bd=20)
lblMobile.grid(row =2, column=0)
lblCalculator = Label(LeftInsideLFLF ,font=('Magneto', 12, 'bold'),text="Calculator", fg="blue", bd=20)
lblCalculator.grid(row =3, column=0)
lblPowerBank = Label(LeftInsideLFLF ,font=('Magneto', 12, 'bold'),text="PowerBank", fg="blue", bd=20)
lblPowerBank.grid(row =4, column=0)
lblbluetoothHeadset = Label(LeftInsideLFLF ,font=('Magneto', 12, 'bold'),text="bluetoothHeadset", fg="blue", bd=20)
lblbluetoothHeadset.grid(row =5, column=0)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
txtQtyPendrive=Entry(LeftInsideLFLF ,font=('Magneto', 12, 'bold'), bd=10, width=10,fg="white", bg="blue", justify='left', textvariable=QtyPendrive)
txtQtyPendrive.grid(row =1, column=1)
txtQtyMobile=Entry(LeftInsideLFLF ,font=('Magneto', 12, 'bold'), bd=10, width=10, fg="white",bg="blue", justify='left', textvariable=QtyMobile)
txtQtyMobile.grid(row =2, column=1)
txtQtyCalculator=Entry(LeftInsideLFLF ,font=('Magneto', 12, 'bold'), bd=10, width=10,fg="white", bg="blue", justify='left', textvariable=QtyCalculator)
txtQtyCalculator.grid(row =3, column=1)
txtQtyPowerBank=Entry(LeftInsideLFLF ,font=('Magneto', 12, 'bold'), bd=10, width=10,fg="white", bg="blue", justify='left', textvariable=QtyPowerBank)
txtQtyPowerBank.grid(row =4, column=1)
txtQtybluetoothHeadset=Entry(LeftInsideLFLF ,font=('Magneto', 12, 'bold'), bd=10, width=10,fg="white", bg="blue", justify='left', textvariable=QtybluetoothHeadset)
txtQtybluetoothHeadset.grid(row =5, column=1)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
txtUnitPricePendrive=Entry(LeftInsideLFLF ,font=('Magneto', 12, 'bold'), bd=10, width=10,fg="white", bg="blue", justify='left', textvariable=UnitPricePendrive)
txtUnitPricePendrive.grid(row =1, column=2)
txtUnitPriceMobile=Entry(LeftInsideLFLF ,font=('Magneto', 12, 'bold'), bd=10, width=10,fg="white", bg="blue", justify='left', textvariable=UnitPriceMobile)
txtUnitPriceMobile.grid(row =2, column=2)
txtUnitPriceCalculator=Entry(LeftInsideLFLF ,font=('Magneto', 12, 'bold'), bd=10, width=10, fg="white",bg="blue", justify='left', textvariable=UnitPriceCalculator)
txtUnitPriceCalculator.grid(row =3, column=2)
txtUnitPricePowerBank=Entry(LeftInsideLFLF ,font=('Magneto', 12, 'bold'), bd=10, width=10,fg="white", bg="blue", justify='left', textvariable=UnitPricePowerBank)
txtUnitPricePowerBank.grid(row =4, column=2)
txtUnitPricebluetoothHeadset=Entry(LeftInsideLFLF ,font=('Magneto', 12, 'bold'), bd=10, width=10, fg="white",bg="blue", justify='left', textvariable=UnitPricebluetoothHeadset)
txtUnitPricebluetoothHeadset.grid(row =5, column=2)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
txtCostofPendrive=Entry(LeftInsideLFLF ,font=('Magneto', 12, 'bold'), bd=10, width=10,fg="white", bg="blue", justify='left', textvariable=CostofPendrive)
txtCostofPendrive.grid(row =1, column=3)
txtCostofMobile=Entry(LeftInsideLFLF ,font=('Magneto', 12, 'bold'), bd=10, width=10,fg="white", bg="blue", justify='left', textvariable=CostofMobile)
txtCostofMobile.grid(row =2, column=3)
txtCostofCalculator=Entry(LeftInsideLFLF ,font=('Magneto', 12, 'bold'), bd=10, width=10, fg="white",bg="blue", justify='left', textvariable=CostofCalculator)
txtCostofCalculator.grid(row =3, column=3)
txtCostofPowerBank=Entry(LeftInsideLFLF ,font=('Magneto', 12, 'bold'), bd=10, width=10, fg="white",bg="blue", justify='left', textvariable=CostofPowerBank)
txtCostofPowerBank.grid(row =4, column=3)
txtCostofbluetoothHeadset=Entry(LeftInsideLFLF ,font=('Magneto', 12, 'bold'), bd=10, width=10,fg="white", bg="blue", justify='left', textvariable=CostofbluetoothHeadset)
txtCostofbluetoothHeadset.grid(row =5, column=3)








#------------------------------------------------------------------------------------------------------------------------
btnTotalCost=Button(RightInsideRFRF, pady=8, bd=8, fg="blue", font=('Magneto', 16, 'bold'), width=11, text="TotalCost", bg="white", command=CostofOrder).grid(row=0 , column=0)
btnReset=Button(RightInsideRFRF, pady=8, bd=8, fg="blue", font=('Magneto', 16, 'bold'), width=11, text="Reset", bg="white",command=Reset).grid(row=1 , column=0)
btnOrderRef=Button(RightInsideRFRF, pady=8, bd=8, fg="blue", font=('Magneto', 16, 'bold'), width=11, text="Order Ref", bg="white", command=OrderRef).grid(row=2 , column=0)
btnExit=Button(RightInsideRFRF, pady=8, bd=8, fg="blue", font=('Magneto', 16, 'bold'), width=11, text="Exit", bg="white", command=Exit).grid(row=3 , column=0)

root.mainloop()
