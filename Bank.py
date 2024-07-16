#!/usr/bin/env python
# coding: utf-8

# In[2]:


from tkinter import *
import time
from tkinter import ttk
from tkinter import messagebox
import sqlite3


# In[ ]:


from tkinter import *
import time
from tkinter import ttk
from tkinter import messagebox
import sqlite3
try:
    
    conobj=sqlite3.connect(database="bank.sqlite")
    curobj=conobj.cursor()
    curobj.execute("create table account(acn_no integer primary key autoincrement,acn_name text,acn_pwd text,acn_email text,acn_mob text,acn_bal float,acn_opendate text,acn_gender text,acc_type text)")
    conobj.close()
    print("table created")

except:
    print("something went wrong,Table already exists")

Win=Tk()
Win.state('zoomed')
Win.configure(bg='pink')
Win.resizable(width=False,height=False)
title=Label(Win,text="Banking Automation",font=('arial',50,'bold','underline'),bg='pink')
title.pack()
title=Label(Win,text="By :- Saurabh singh",font=('arial',15,'bold','underline'),bg='pink')
title.place(relx=.02,rely=.02)
title=Label(Win,text="Mob:- 8102466472",font=('arial',15,'bold','underline'),bg='pink')
title.place(relx=.02,rely=.06)
title=Label(Win,text="Email-: 29Saurabhsingh000@gmail.com",font=('arial',15,'bold','underline'),bg='pink')
title.place(relx=.02,rely=.10)
dt=time.strftime ("%d %b,%Y")
date=Label(Win,text=f"{dt}",font=('arial',20,'bold'),bg='pink',fg='blue')
date.place(relx=.80,rely=.05)


def main_screen():
    frm=Frame(Win)
    frm.configure(bg='powder blue')
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)

    def forgotpass():
        frm.destroy()
        forgotpass_screen()
    def newuser():
        frm.destroy()
        newuser_screen()
    def login():
        global gaccn
        gaccn=e_accn.get()
        pwd=e_pass.get()
        if len(gaccn)==0 or len(pwd)==0:
            messagebox.showwarning("Validation","Empty fields are not allowed")
            return
        else:
            gaccn=e_accn.get()
            pwd=e_pass.get()
            conobj=sqlite3.connect(database="bank.sqlite")
            curobj=conobj.cursor()
            curobj.execute("select * from account where acn_no=? and acn_pwd=?",(gaccn,pwd))
            tup=curobj.fetchone()
            conobj.close()
            if tup==None:
                messagebox.showerror("Login","Invalid ACN/Pass")
            else:
                 frm.destroy()
                 welcome_screen()


    
    def clear():
        e_accn.delete(0,"end")
        e_pass.delete(0,"end")
        e_accn.focus()
        
    lbl_accn=Label(frm,text="ACN",font=('arial',20,'bold'),bg='powder blue')
    lbl_accn.place(relx=.3,rely=.1)
     
    e_accn=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_accn.place(relx=.4,rely=.1)
    e_accn.focus()

    
    lbl_pass=Label(frm,text="Pass",font=('arial',20,'bold'),bg='powder blue')
    lbl_pass.place(relx=.3,rely=.2)
     
    e_pass=Entry(frm,font=('arial',20,'bold'),bd=5,show='*')
    e_pass.place(relx=.4,rely=.2)

    btn_login=Button(frm,text="login",font=('arial',20,'bold'),bd=5,command=login)
    btn_login.place(relx=.43,rely=.4)
    
    btn_Clear=Button(frm,text="Clear",font=('arial',20,'bold'),bd=5,command=clear)
    btn_Clear.place(relx=.54,rely=.4)

    btn_FP=Button(frm,text="forgot Password",font=('arial',20,'bold'),bd=5,command=forgotpass)
    btn_FP.place(relx=.43,rely=.52)

    btn_new=Button(frm,command=newuser,text="Open new account",font=('arial',20,'bold'),bd=5)
    btn_new.place(relx=.43,rely=.64)


def forgotpass_screen():
    frm=Frame(Win)
    frm.configure(bg='powder blue')
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)

    def back():
        frm.destroy()
        main_screen()
        
    def clear():
        e_accn.delete(0,"end")
        e_email.delete(0,"end")
        e_mob.delete(0,"end")
        e_accn.focus()

    def forgot_pass():
        accn=e_accn.get()
        email=e_email.get()
        mob=e_mob.get()
        if len(accn)==0 or len(email)==0 or len(mob)==0:
            messagebox.showwarning("Validation","Empty fields are not allowed")
        else:
             conobj=sqlite3.connect(database="bank.sqlite")
             curobj=conobj.cursor()
             curobj.execute("select acn_pwd from account where acn_no=? and acn_email=? and acn_mob=?",(accn,email,mob))
             tup=curobj.fetchone()
             if tup==None:
                 messagebox.showerror("forgot pass","Record not found")
             else:
                 messagebox.showinfo("forgot pass",f"Your Pass={tup[0]}")
             conobj.close()
        e_accn.delete(0,"end")
        e_email.delete(0,"end")
        e_mob.delete(0,"end")
        e_accn.focus()
            
            
        
                 
            

       
    btn_back=Button(frm,text="Back",font=('arial',20,'bold'),bd=5,command=back)
    btn_back.place(relx=0,rely=0)
    
    lbl_accn=Label(frm,text="ACN",font=('arial',20,'bold'),bg='powder blue')
    lbl_accn.place(relx=.3,rely=.1)
     
    e_accn=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_accn.place(relx=.4,rely=.1)
    e_accn.focus()
    lbl_email=Label(frm,text="Email",font=('arial',20,'bold'),bg='powder blue')
    lbl_email.place(relx=.3,rely=.2)
     
    e_email=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_email.place(relx=.4,rely=.2)
    
    lbl_mob=Label(frm,text="Mob.",font=('arial',20,'bold'),bg='powder blue')
    lbl_mob.place(relx=.3,rely=.3)
     
    e_mob=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_mob.place(relx=.4,rely=.3)

    btn_submit=Button(frm,width=7,text="Submit",font=('arial',20,'bold'),bd=5,command=forgot_pass)
    btn_submit.place(relx=.4,rely=.45)
    
    btn_Clear=Button(frm,width=7,text="Clear",font=('arial',20,'bold'),bd=5,command=clear)
    btn_Clear.place(relx=.53,rely=.45)
    
def newuser_screen():
    frm=Frame(Win)
    frm.configure(bg='powder blue')
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)

    def back():
        frm.destroy()
        main_screen()

    def newuser_db():
        name=e_name.get()
        email=e_email.get()
        mob=e_mob.get()
        pwd=e_pass.get()
        gender=e_gender.get()
        acc_type=e_Acc_type.get()
        acn_bal=0
        acc_opendate=dt=time.strftime ("%d %B %Y,%A")
        import sqlite3
        conobj=sqlite3.connect(database="bank.sqlite")
        curobj=conobj.cursor()
        curobj.execute("insert into account(acn_name,acn_pwd,acn_email,acn_mob,acn_bal,acn_opendate,acn_gender,acc_type) values(?,?,?,?,?,?,?,?)",(name,pwd,email,mob,acn_bal,acc_opendate,gender,acc_type))
        conobj.commit()
        conobj.close()
        conobj=sqlite3.connect(database="bank.sqlite")
        curobj=conobj.cursor()
        curobj.execute("select max(acn_no) from account")
        tuple=curobj.fetchone()
        print(tuple[0])
        conobj.commit()
        conobj.close()
        messagebox.showinfo("New user",f"Account created with ACN no={tuple[0]}")
        e_name.delete(0,"end")
        e_email.delete(0,"end")
        e_mob.delete(0,"end")
        e_pass.delete(0,"end")
        e_gender.delete(0,"end")
        e_Acc_type.delete(0,"end")
        



    
    def clear():
        e_name.delete(0,"end")
        e_email.delete(0,"end")
        e_mob.delete(0,"end")
        e_pass.delete(0,"end")
        e_gender.delete(0,"end")
        e_Acc_type.delete(0,"end")        
        e_name.focus()
    

    btn_back=Button(frm,text="Back",font=('arial',20,'bold'),bd=5,command=back)
    btn_back.place(relx=0,rely=0)
    
    lbl_name=Label(frm,text="Name",font=('arial',20,'bold'),bg='powder blue')
    lbl_name.place(relx=.3,rely=.1)
     
    e_name=Entry(frm,font=('arial',18,'bold'),bd=5)
    e_name.place(relx=.4,rely=.1)
    e_name.focus()
    
    lbl_email=Label(frm,text="Email",font=('arial',20,'bold'),bg='powder blue')
    lbl_email.place(relx=.3,rely=.2)
     
    e_email=Entry(frm,font=('arial',18,'bold'),bd=5)
    e_email.place(relx=.4,rely=.2)
    
    lbl_mob=Label(frm,text="Mob.",font=('arial',20,'bold'),bg='powder blue')
    lbl_mob.place(relx=.3,rely=.3)
     
    e_mob=Entry(frm,font=('arial',18,'bold'),bd=5)
    e_mob.place(relx=.4,rely=.3)
    
    lbl_pass=Label(frm,text="Pass",font=('arial',20,'bold'),bg='powder blue')
    lbl_pass.place(relx=.3,rely=.4)
     
    e_pass=Entry(frm,font=('arial',18,'bold'),bd=5)
    e_pass.place(relx=.4,rely=.4)
    
    lbl_gender=Label(frm,text="Gender",font=('arial',20,'bold'),bg='powder blue')
    lbl_gender.place(relx=.3,rely=.5)
     
    e_gender=ttk.Combobox(frm,values=["----Select Gender---","Male","Female","other"],font=('arial',19,'bold'))
    e_gender.place(relx=.4,rely=.5)
    
    lbl_Acc_type=Label(frm,text="Acc Type",font=('arial',19,'bold'),bg='powder blue')
    lbl_Acc_type.place(relx=.3,rely=.59)
    e_Acc_type=ttk.Combobox(frm,values=["-----Select Account Type----","Saving Acc","Current Acc"],font=('arial',19,'bold'))
    e_Acc_type.place(relx=.4,rely=.59)
    
    btn_submit=Button(frm,text="Submit",font=('arial',20,'bold'),bd=5,command=newuser_db)
    btn_submit.place(relx=.4,rely=.7)
    
    btn_Clear=Button(frm,text="Clear",font=('arial',20,'bold'),bd=5,command=clear)
    btn_Clear.place(relx=.55,rely=.7)
    
def welcome_screen():
    frm=Frame(Win)
    frm.configure(bg='powder blue')
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)
    
    def logout():
        frm.destroy()
        main_screen()
    def details():
        ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
        ifrm.configure(bg="white")
        ifrm.place(relx=.2,rely=.1,relwidth=.7,relheight=.55)

        lbl_customer=Label(ifrm,text="Customer Details",font=('arial',20,'bold','underline'),bg='white',bd=1)
        lbl_customer.pack()

        conobj=sqlite3.connect(database="bank.sqlite")
        curobj=conobj.cursor()
        curobj.execute("select acn_opendate,acn_bal,acn_gender,acn_mob,acc_type,acn_email from account where acn_no=?",(gaccn,))
        tup=curobj.fetchone()
        conobj.close()
        lbl_opendate=Label(ifrm,text=f"Open date:- {tup[0]}",font=('arial',16,'bold'),bg='powder blue',bd=1)
        lbl_opendate.place(relx=.19,rely=.12)
        lbl_bal=Label(ifrm,text=f"Balance= {tup[1]}",font=('arial',16,'bold'),bg='white',bd=1)
        lbl_bal.place(relx=.19,rely=.25)
        lbl_gender=Label(ifrm,text=f"Gender:- {tup[2]}",font=('arial',16,'bold'),bg='powder blue',bd=1)
        lbl_gender.place(relx=.19,rely=.38)
        lbl_mob=Label(ifrm,text=f"Mobile no.- {tup[3]}",font=('arial',16,'bold'),bg='white',bd=1)
        lbl_mob.place(relx=.19,rely=.51)
        lbl_Acc_type=Label(ifrm,text=f"Account type:-{tup[4]}",font=('arial',16,'bold'),bg='powder blue',bd=1)
        lbl_Acc_type.place(relx=.19,rely=.64)
        lbl_email=Label(ifrm,text=f"Email:- {tup[5]}",font=('arial',16,'bold'),bg='white',bd=1)
        lbl_email.place(relx=.19,rely=.77)
        
        conobj.close()


    
            
    def update():           
           
        ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
        ifrm.configure(bg="white")        
        ifrm.place(relx=.2,rely=.1,relwidth=.7,relheight=.55)

        conobj=sqlite3.connect(database="bank.sqlite")
        curobj=conobj.cursor()
        curobj.execute("select acn_name,acn_email,acn_mob,acn_pwd from account where acn_no=?",(gaccn,))
        tup=curobj.fetchone()
        conobj.close()
        lbl_customer=Label(ifrm,text="Update Details",font=('arial',20,'bold','underline'),bg='white',bd=1)
        lbl_customer.pack()


        lbl_name=Label(ifrm,text="Name",font=('arial',20,'bold'),bg='powder blue')
        lbl_name.place(relx=.15,rely=.13)
         
        e_name=Entry(ifrm,font=('arial',18,'bold'),bd=5)
        e_name.place(relx=.1,rely=.26)
        e_name.insert(0,tup[0])
        e_name.focus()
        
        lbl_email=Label(ifrm,text="Email",font=('arial',20,'bold'),bg='powder blue')
        lbl_email.place(relx=.6,rely=.13)
         
        e_email=Entry(ifrm,font=('arial',18,'bold'),bd=5)
        e_email.place(relx=.55,rely=.26)
        e_email.insert(0,tup[1])
        lbl_mob=Label(ifrm,text="Mob.",font=('arial',20,'bold'),bg='powder blue')
        lbl_mob.place(relx=.15,rely=.45)
         
        e_mob=Entry(ifrm,font=('arial',18,'bold'),bd=5)
        e_mob.place(relx=.1,rely=.58)
        e_mob.insert(0,tup[2])
        lbl_pwd=Label(ifrm,text="Pass",font=('arial',20,'bold'),bg='powder blue')
        lbl_pwd.place(relx=.6,rely=.45)
         
        e_pwd=Entry(ifrm,font=('arial',18,'bold'),bd=5)
        e_pwd.place(relx=.55,rely=.58)
        e_pwd.insert(0,tup[3])

        def update_db():
            name=e_name.get()
            email=e_email.get()
            mob=e_mob.get()
            pwd=e_pwd.get()
            
            conobj=sqlite3.connect(database="bank.sqlite")
            curobj=conobj.cursor()
            curobj.execute("update  account set acn_name=?,acn_email=?,acn_mob=?,acn_pwd=? where acn_no=?",(name,email,mob,pwd,gaccn))
            conobj.commit()
            conobj.close()
            messagebox.showinfo("UPDATE","Record updated")
            welcome_screen()
        btn_update=Button(ifrm,text="UPDATE",font=('arial',20,'bold'),bd=5,command=update_db)
        btn_update.place(relx=.80,rely=.80)
       
    def withdraw():
        ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
        ifrm.configure(bg="white")
        ifrm.place(relx=.2,rely=.1,relwidth=.7,relheight=.55)

        lbl_customer=Label(ifrm,text="Withdraw",font=('arial',20,'bold','underline'),bg='white',bd=1)
        lbl_customer.pack()

        lbl_amount=Label(ifrm,text="Amount",font=('arial',20,'bold'))
        lbl_amount.place(relx=.2,rely=.2)
         
        e_amount=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        e_amount.place(relx=.4,rely=.2)
        e_amount.focus()
        
        def withdraw_db():
            amount=float(e_amount.get())

            conobj=sqlite3.connect(database="bank.sqlite")
            curobj=conobj.cursor()
            curobj.execute("select acn_bal from account where acn_no=?",(gaccn,))
            tup=curobj.fetchone()
            avail_bal=tup[0]
            conobj.close()
            if avail_bal>=amount:
                conobj=sqlite3.connect(database="bank.sqlite")
                curobj=conobj.cursor()
                curobj.execute("update account set acn_bal=acn_bal-? where acn_no=?",(amount,gaccn))
                conobj.commit()
                conobj.close()
                messagebox.showinfo("Submit","Amount Withdraw Successfuly")
                e_amount.delete(0,"end")
                welcome_screen()
            else:
                messagebox.showinfo("Submit","Insufficient balance")
                e_amount.delete(0,"end")
                
        btn_submit=Button(ifrm,text="Submit",font=('arial',20,'bold'),bd=5,command=withdraw_db)
        btn_submit.place(relx=.4,rely=.5)
    def deposite():
        ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
        ifrm.configure(bg="white")
        ifrm.place(relx=.2,rely=.1,relwidth=.7,relheight=.55)

        lbl_customer=Label(ifrm,text="Deposite",font=('arial',20,'bold','underline'),bg='white',bd=1)
        lbl_customer.pack()
        
        lbl_amount=Label(ifrm,text="Amount",font=('arial',20,'bold'))
        lbl_amount.place(relx=.2,rely=.2)
         
        e_amount=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        e_amount.place(relx=.4,rely=.2)
        e_amount.focus()
        def deposite_db():
            amount=float(e_amount.get())
            conobj=sqlite3.connect(database="bank.sqlite")
            curobj=conobj.cursor()
            curobj.execute("update account set acn_bal=acn_bal+? where acn_no=?",(amount,gaccn))
            conobj.commit()
            conobj.close
            messagebox.showinfo("Submit","Amount Deposited Successfuly")
            e_amount.delete(0,"end")
            welcome_screen()
        btn_submit=Button(ifrm,text="Submit",font=('arial',20,'bold'),bd=5,command=deposite_db)
        btn_submit.place(relx=.4,rely=.5)

    def transfer():
        ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
        ifrm.configure(bg="white")
        ifrm.place(relx=.2,rely=.1,relwidth=.7,relheight=.55)

        lbl_customer=Label(ifrm,text="Transfer",font=('arial',20,'bold','underline'),bg='white',bd=1)
        lbl_customer.pack()
        lbl_amount=Label(ifrm,text="Amount",font=('arial',20,'bold'))
        lbl_amount.place(relx=.2,rely=.2)
         
        e_amount=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        e_amount.place(relx=.37,rely=.2)
        e_amount.focus()
        lbl_to=Label(ifrm,text="To",font=('arial',20,'bold'))
        lbl_to.place(relx=.2,rely=.4)
         
        e_to_acn=Entry(ifrm,font=('arial',17,'bold'),bd=5)
        e_to_acn.place(relx=.37,rely=.4)
        e_amount.focus()
        def transfer_db():
            amt=float(e_amount.get())
            to_acn=e_to_acn.get()
            if to_acn==gaccn:
                messagebox.showwarning("Transfer","To and From ACN can't be same")
                return
            conobj=sqlite3.connect(database="bank.sqlite")
            curobj=conobj.cursor()
            curobj.execute("select acn_bal from account where acn_no=?",(gaccn,))
            tup=curobj.fetchone()
            avail_bal=tup[0]
            conobj.close()

            conobj=sqlite3.connect(database="bank.sqlite")
            curobj=conobj.cursor()
            curobj.execute("select acn_no from account where acn_no=?",(to_acn,))
            tup=curobj.fetchone()
            conobj.close()
            if tup==None:
                messagebox.showwarning("Transfer","Invalid ACN")
                return
            if avail_bal>=amt:
                
                conobj=sqlite3.connect(database="bank.sqlite")
                curobj=conobj.cursor()
                curobj.execute("update account set acn_bal=acn_bal+? where acn_no=?",(amt,to_acn))
                curobj.execute("update account set acn_bal=acn_bal-? where acn_no=?",(amt,gaccn))
                conobj.commit()
                conobj.close()
                messagebox.showinfo("Transfer",f"{amt} Transfer Succesfully to ACN {to_acn}")
                e_amount.delete(0,"end")
                e_to_acn.delete(0,"end")
            else:
                messagebox.showwarning("Transfer","Insufficient Balance")
                e_amount.delete(0,"end")
                e_to_acn.delete(0,"end")
                
                
                           
                
        
        btn_submit=Button(ifrm,text="Submit",font=('arial',20,'bold'),bd=5,command=transfer_db)
        btn_submit.place(relx=.43,rely=.65)

    
    conobj=sqlite3.connect(database="bank.sqlite")
    curobj=conobj.cursor()
    curobj.execute("select acn_name from account where acn_no=?",(gaccn,))
    tup=curobj.fetchone()
    conobj.close()
    lbl_wel=Label(frm,text=f"Welcome,{tup[0]}",font=('arial',20,'bold'),bg='powder blue')
    lbl_wel.place(relx=0,rely=0)

    btn_logout=Button(frm,text="logout",font=('arial',20,'bold'),bd=5,command=logout)
    btn_logout.place(relx=.91,rely=0)

    btn_details=Button(frm,width=10,text="Details",font=('arial',20,'bold'),bd=5,command=details)
    btn_details.place(relx=.0,rely=.1)
    
    btn_update=Button(frm,width=10,text="Update",font=('arial',20,'bold'),bd=5,command=update)
    btn_update.place(relx=.0,rely=.21)
    
    btn_withdraw=Button(frm,width=10,text="Withdraw",font=('arial',20,'bold'),bd=5,command=withdraw)
    btn_withdraw.place(relx=.0,rely=.32)

    btn_deposite=Button(frm,width=10,text="Deposite",font=('arial',20,'bold'),bd=5,command=deposite)
    btn_deposite.place(relx=.0,rely=.43)
    
    btn_transfer=Button(frm,width=10,text="Transfer",font=('arial',20,'bold'),bd=5,command=transfer)
    btn_transfer.place(relx=.0,rely=.54)







main_screen()
Win.mainloop()




