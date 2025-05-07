import datetime
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

class Gcash:
    def __init__(self, root):
        self.root = root
        self.root.title("GCASH MANAGEMENT SYSTEM")
        self.root.geometry("1540x800+0+0")
        
        self.TRANSACTIONSTYPE=StringVar()
        self.MOBILENUMBER=StringVar()
        self.AMOUNT=StringVar()
        self.PAYMENTFEE=StringVar()
        self.DATE=StringVar()
        self.REFERENCENO=StringVar()

        def calculate_payment_fee(event=None):
            try:
                amount = float(self.AMOUNT.get())
                payment_fee = amount / 100
                self.PAYMENTFEE.set(payment_fee)
            except ValueError:
                messagebox.showerror("Error", "Invalid amount")

        def populate_date(event=None):
            self.DATE.set(datetime.datetime.now().strftime('%Y-%m-%d'))

        def iRECORDDATA():
            TRANSACTIONSTYPE = self.TRANSACTIONSTYPE.get()
            MOBILENUMBER = self.MOBILENUMBER.get()
            AMOUNT = self.AMOUNT.get()
            PAYMENTFEE = self.PAYMENTFEE.get()
            DATE = self.DATE.get()  
            REFERENCENO = self.REFERENCENO.get()

            if len(MOBILENUMBER) != 11:
                messagebox.showerror("Error", "Mobile number should be 11 digits")
                return
            if len(REFERENCENO) != 13:
                messagebox.showerror("Error", "Reference number should be 13 digits")
                return

            try:
                datetime.datetime.strptime(DATE, '%Y-%m-%d')
            except ValueError:
                messagebox.showerror("Error", "Incorrect date format. Please use YYYY-MM-DD")
                return

            conn = mysql.connector.connect(host="localhost", user="root", password="", database="Gcash")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO TRANSACTIONS VALUES (%s, %s, %s, %s, %s, %s)",
                        (TRANSACTIONSTYPE, MOBILENUMBER, AMOUNT, PAYMENTFEE, DATE, REFERENCENO))
            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "Transaction added successfully")
            fatch_data()
                
        def iUPDATEDATA():
            TRANSACTIONSTYPE = self.TRANSACTIONSTYPE.get()
            MOBILENUMBER = self.MOBILENUMBER.get()
            AMOUNT = self.AMOUNT.get()
            PAYMENTFEE = self.PAYMENTFEE.get()
            DATE = self.DATE.get()
            REFERENCENO = self.REFERENCENO.get()
            
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="Gcash")
            cursor = conn.cursor()
            cursor.execute("UPDATE TRANSACTIONS ""SET TRANSACTIONSTYPE='" + TRANSACTIONSTYPE + "', ""MOBILENUMBER='" + MOBILENUMBER + "', ""AMOUNT='" + AMOUNT + "', ""PAYMENTFEE='" + PAYMENTFEE + "', ""DATE='" + DATE + "' " "WHERE REFERENCENO='" + REFERENCENO + "'")
            
            conn.commit()
                
            messagebox.showinfo("Success", "Transaction Updated successfully")
            fatch_data()
            conn.close()
            
                
        def fatch_data():
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="Gcash")
            cursor = conn.cursor()
            cursor.execute("select * from TRANSACTIONS")
            rows = cursor.fetchall()  
            if len(rows)!=0:
                self.transactions_table.delete(*self.transactions_table.get_children())
                for i in rows:
                    self.transactions_table.insert("", END, values=i)
                conn.commit()
            conn.close()

            
        def get_cursor(event=""):
            cursor_row=self.transactions_table.focus()
            content= self.transactions_table.item(cursor_row)
            row= content["values"]
            self.TRANSACTIONSTYPE.set(row[0])
            self.MOBILENUMBER.set(row[1])
            self.AMOUNT.set(row[2])
            self.PAYMENTFEE.set(row[3])
            self.DATE.set(row[4])
            self.REFERENCENO.set(row[5])
            
        def iTRANSACTIONS():
            self.txtInformation.insert(END,"\n  TRANSACTION TYPE:\t\t "+self.TRANSACTIONSTYPE.get()+"\n")    
            self.txtInformation.insert(END,"  MOBILE NUMBER:\t\t      "+self.MOBILENUMBER.get()+"\n")
            self.txtInformation.insert(END,"  AMOUNT:\t\t          "+self.AMOUNT.get()+"\n")
            self.txtInformation.insert(END,"  PAYMENT FEE:\t\t          "+self.PAYMENTFEE.get()+"\n")
            self.txtInformation.insert(END,"  DATE:\t\t          "+self.DATE.get()+"\n")
            self.txtInformation.insert(END,"  REFERENCE NO:\t\t        "+self.REFERENCENO.get()+"\n")
            
        def iDELETE():
            if not self.REFERENCENO.get():
                messagebox.showerror("Error", "Please select a transaction to delete")
                return

            if messagebox.askyesno("Delete", "Are you sure you want to delete this transaction?"):
                conn = mysql.connector.connect(host="localhost", user="root", password="", database="Gcash")
                cursor = conn.cursor()    
                cursor.execute("DELETE FROM TRANSACTIONS WHERE REFERENCENO='" + self.REFERENCENO.get() + "'")
                conn.commit()
                conn.close()
                fatch_data()
                messagebox.showinfo("Delete", "Record has been deleted successfully")


        def iCLEAR():
            self.TRANSACTIONSTYPE.set("")
            self.MOBILENUMBER.set("")
            self.AMOUNT.set("")
            self.PAYMENTFEE.set("")
            self.DATE.set("")
            self.REFERENCENO.set("")
            self.txtInformation.delete("1.0",END)
            
        def iEXIT():
            iEXIT=messagebox.askyesno("Gcash Management System","Confirm you want to Exit?")
            if iEXIT>0:
                root.destroy()
                return
            
  
        #=================================== Title =======================================
                
        lbtitle = Label(self.root, bd = 20, relief = RIDGE, text = "GCASH MANAGEMENT SYSTEM", fg = "#3366FF", bg = "white", font =("calibiri", 50, "bold"))
        lbtitle.pack(side = TOP, fill = X)
        
        #=================================== Dataframe =======================================
        Dataframe = Frame (self.root, bd = 20, relief = RIDGE)
        Dataframe.place(x = 0, y = 130, width = 1530, height = 400)
        
        
        DataframeLeft = LabelFrame(Dataframe, bd = 10, padx = 20, relief = RIDGE,  fg = "#003366",
                                                                font = ("Calibiri", 27, "bold"),text = " TRANSACTIONS ")
        DataframeLeft.place(x = 0, y = 5, width = 980, height = 350)                                                        
        
        DataframeRight = LabelFrame(Dataframe, bd = 10, padx = 20, relief = RIDGE, fg = "#003366",
                                                                font = ("Calibiri", 20, "bold"),text = " INFORMATION ")
        DataframeRight.place(x = 990, y = 5, width = 500, height = 350)                                                   
        
        #=================================== Buttons frame =======================================

        Buttonframe = Frame(self.root, bd = 20, relief = RIDGE)
        Buttonframe.place(x = 0, y = 530, width = 1530, height = 70)

        #=================================== Details frame =======================================

        Detailsframe = Frame(self.root, bd = 20, relief = RIDGE)
        Detailsframe.place(x = 0, y = 600, width = 1530, height = 190)

        #=================================== DataframeLeft =======================================

        TRANSACTIONSTYPE = Label(DataframeLeft, fg = "green", text = "CASH IN OR OUT ", font = ("Calibiri", 18, "bold"), padx = 8, pady = 15)
        TRANSACTIONSTYPE.grid(row = 0, column = 0)
        
        comTRANSACTIONSTYPE= ttk.Combobox(DataframeLeft,textvariable=self.TRANSACTIONSTYPE, state = "readonly",
                                    font = ("Calibiri", 18, "bold"),width = 33)
        comTRANSACTIONSTYPE["values"]= ("CASH IN", "CASH OUT")
        comTRANSACTIONSTYPE.grid(row = 0, column  = 1)
        
        MOBILENUMBER = Label(DataframeLeft, font=("Calibiri", 18, "bold"), text="MOBILE NUMBER:", padx=3)
        MOBILENUMBER.grid(row=1, column=0, sticky=W)
        comMOBILENUMBER = Entry(DataframeLeft, textvariable=self.MOBILENUMBER, font=("Calibiri", 14, "bold"), width=35)
        comMOBILENUMBER.grid(row=1, column=1)
        
        AMOUNT = Label(DataframeLeft, font=("Calibiri", 18, "bold"), text="AMOUNT:", padx=3)
        AMOUNT.grid(row=2, column=0, sticky=W)
        comAMOUNT = Entry(DataframeLeft, textvariable=self.AMOUNT, font=("Calibiri", 14, "bold"), width=35)
        comAMOUNT.grid(row=2, column=1)
        comAMOUNT.bind("<KeyRelease>", calculate_payment_fee)  # Binding to calculate payment fee
        
        PAYMENTFEE = Label(DataframeLeft, font=("Calibiri", 18, "bold"), text="PAYMENT FEE:", padx=3)
        PAYMENTFEE.grid(row=3, column=0, sticky=W)
        comPAYMENTFEE = Entry(DataframeLeft,textvariable=self.PAYMENTFEE,  font=("Calibiri", 14, "bold"), width=35)
        comPAYMENTFEE.grid(row=3, column=1)
        
        DATE = Label(DataframeLeft, font=("Calibiri", 18, "bold"), text="DATE", padx=3)
        DATE.grid(row=4, column=0, sticky=W)
        comDATE = Entry(DataframeLeft,textvariable=self.DATE, font=("Calibiri", 14, "bold"), width=35)
        comDATE.grid(row=4, column=1)
        comDATE.bind("<FocusIn>", populate_date)  # Binding to populate date
        
        REFERENCENO = Label(DataframeLeft, font=("Calibiri", 18, "bold"), text="REFERENCE NO:", padx=3)
        REFERENCENO.grid(row=5, column=0, sticky=W)
        comREFERENCENO = Entry(DataframeLeft, textvariable=self.REFERENCENO, font=("Calibiri", 14, "bold") ,width=35)
        comREFERENCENO.grid(row=5, column=1)
        
        
        
        #=================================== DataframeRight =======================================
        self.txtInformation = Text(DataframeRight, font=("Calibiri", 15, "bold"), width=40, height=11, padx=2, pady=8)
        self.txtInformation.grid(row = 0, column = 0)
        
        #=================================== Buttons =======================================
        btnTransactions=Button(Buttonframe, text="TRANSACTIONS", bg="green", fg="white" ,font=("Calibiri", 12, "bold"), width=24, padx=2, pady=8, command=iTRANSACTIONS)
        btnTransactions.grid(row=0, column=0)

        btnRecordData=Button(Buttonframe,  text="RECORD DATA", bg="green", fg="white",font=("Calibiri", 12, "bold"), width=24, padx=2, pady=8, command=iRECORDDATA)
        btnRecordData.grid(row=0, column=2)
        
        btnUpdate=Button(Buttonframe,  text="UPDATE", bg="green", fg="white",font=("Calibiri", 12, "bold"), width=24, padx=2, pady=8 ,command=iUPDATEDATA)
        btnUpdate.grid(row=0, column=3)
        
        btnDelete=Button(Buttonframe,  text="DELETE", bg="green", fg="white",font=("Calibiri", 12, "bold"), width=24, padx=2, pady=8, command=iDELETE)
        btnDelete.grid(row=0, column=4)
        
        btnClear=Button(Buttonframe,  text="CLEAR", bg="green", fg="white",font=("Calibiri", 12, "bold"), width=23, padx=2, pady=8, command=iCLEAR)
        btnClear.grid(row=0, column=5)
        
        btnExit=Button(Buttonframe,  text="EXIT", bg="green", fg="white",font=("Calibiri", 12, "bold"), width=23, padx=2, pady=8, command=iEXIT)
        btnExit.grid(row=0, column=6)
        
        
        #=================================== Scrollbar =======================================
        scroll_x = ttk.Scrollbar(Detailsframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe, orient=VERTICAL)
        self.transactions_table = ttk.Treeview(Detailsframe, column=("TRANSACTIONTYPE", "MOBILENUMBER", "AMOUNT", "PAYMENTFEE","DATE","REFERENCENO" ), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x=ttk.Scrollbar(command=self.transactions_table.xview)
        scroll_y=ttk.Scrollbar(command=self.transactions_table.yview)
        
        self.transactions_table.heading("TRANSACTIONTYPE", text="TRANSACTION TYPE")
        self.transactions_table.heading("MOBILENUMBER", text="MOBILE NUMBER")
        self.transactions_table.heading("AMOUNT", text="AMOUNT")
        self.transactions_table.heading("PAYMENTFEE", text="CHARGE")
        self.transactions_table.heading("DATE", text="DATE")
        self.transactions_table.heading("REFERENCENO", text="REFERENCE NO")
        
        self.transactions_table["show"]="headings"
        
        self.transactions_table.column("TRANSACTIONTYPE", width = 100)
        self.transactions_table.column("MOBILENUMBER", width = 100)
        self.transactions_table.column("AMOUNT", width = 100)
        self.transactions_table.column("PAYMENTFEE", width = 100)
        self.transactions_table.column("DATE", width = 100)
        self.transactions_table.column("REFERENCENO", width = 100)
        
        self.transactions_table.pack(fill=BOTH, expand=1)
        self.transactions_table.bind("<ButtonRelease-1>", get_cursor)
        
        fatch_data()
        
        #=================================== Functionality Declaration =======================================
        

        
if __name__ == "__main__":
    root = Tk()
    ob = Gcash(root)
    root.mainloop()
