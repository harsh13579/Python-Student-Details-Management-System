from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import pymysql
import customtkinter
customtkinter.set_appearance_mode("light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"
class MemberConnect(customtkinter.CTk):
    
    def __init__(self,root):
        self.root = root
        blankSpace = " "
        self.root.title(202 * blankSpace + "Student Details")
        self.root.resizable(width=0,height=0)
        self.root.geometry(f"{1100}x{600}")

        #=======================================================================================#
        StuID=StringVar()
        FirstName=StringVar()
        LastName=StringVar()
        Address=StringVar()
        PoBox=StringVar()
        Gender=StringVar()
        Mobile=StringVar()
        Email=StringVar()
        ClassSec=StringVar()
        Search=StringVar()
        #=======================================================================================#
        def Reset():
            StuID.set("")
            FirstName.set("")
            LastName.set("")
            Address.set("")
            PoBox.set("")
            Gender.set("")
            Mobile.set("")
            Email.set("")

            Search.set("")
        
        def iExit():
            iExit=tkinter.messagebox.askyesno("Connector System","Sure You Want To Exit?")
            if iExit>0:
                root.destroy()
                return
        
        #=======================================================================================#
        MainFrame = Frame(self.root,width=1300,height=700,relief=RIDGE)
        MainFrame.grid()
        
        TitleFrames = Frame(MainFrame,width=1300,height=100,relief=RIDGE)
        TitleFrames.grid(row=0,column=0)
        
        TitleFrame = Frame(TitleFrames,width=1300,height=100,relief=RIDGE)
        TitleFrame.grid(row=0,column=0)
        
        SearchFrames = Frame(MainFrame,width=1300,height=50,relief=RIDGE)
        SearchFrames.grid(row=1,column=0)

        MidFrames = Frame(MainFrame,width=1300,height=500,relief=RIDGE)
        MidFrames.grid(row=3,column=0)
        
        InnerFrame = Frame(MidFrames,width=1300,height=150,pady=4,relief=RIDGE)
        InnerFrame.grid(row=0,column=0)
        
        ButtonFrames = Frame(MidFrames,width=1300,height=50,relief=RIDGE)
        ButtonFrames.grid(row=1,column=0)

        TreeViewFrames = Frame(MidFrames,width=1300,height=420,relief=RIDGE)
        TreeViewFrames.grid(row=2,column=0,padx=20,pady=10)

        

        #=======================================================================================#
        self.lblTitle= customtkinter.CTkLabel(TitleFrame,font=('Arial',40,'bold'),text="Student Information")
        self.lblTitle.grid(row=0,column=0)

        self.lblSchool= customtkinter.CTkLabel(TitleFrame,font=('Arial',60),text="NNGHSS")
        self.lblSchool.grid(row=0,column=1,padx=50)

        #=======================================================================================#
        self.lblTitle= customtkinter.CTkLabel(TitleFrame,font=('Arial',40,'bold'),text="Student Information")
        self.lblTitle.grid(row=0,column=0,pady=20)


        #=======================================================================================#
        self.lblStuID = customtkinter.CTkLabel(InnerFrame, font=('arial', 17, 'bold'), text="Student ID")
        self.lblStuID .grid(row=0, column=0, padx=5, sticky=W) 
        self.txtStuID=customtkinter.CTkEntry(InnerFrame, font=('arial', 12, 'bold'), width=160, textvariable=StuID,
        justify='left')
        self.txtStuID .grid(row=0, column=1)

        self.lblFirstName = customtkinter.CTkLabel(InnerFrame, font=('arial', 17, 'bold'), text="Student's Name")
        self.lblFirstName .grid(row=1, column=0, padx=5, sticky=W) 
        self.txtFirstName=customtkinter.CTkEntry(InnerFrame, font=('arial', 12, 'bold'), width=160, textvariable=FirstName,
        justify='left')
        self.txtFirstName .grid(row=1, column=1)

        self.lblLastName = customtkinter.CTkLabel(InnerFrame, font=('arial', 17, 'bold'), text="Father's Occupation")
        self.lblLastName .grid(row=2, column=0, padx=5, sticky=W) 
        self.txtLastName=customtkinter.CTkEntry(InnerFrame, font=('arial', 12, 'bold'), width=160,textvariable=LastName,
        justify='left')
        self.txtLastName .grid(row=2, column=1)

        self.lblAddress = customtkinter.CTkLabel(InnerFrame, font=('arial', 17, 'bold'), text="Address")
        self.lblAddress .grid(row=0, column=2, padx=30, sticky=W) 
        self.txtAddress=customtkinter.CTkEntry(InnerFrame, font=('arial', 12, 'bold'), width=160,textvariable=Address,
        justify='left')
        self.txtAddress .grid(row=0, column=3)

        self.lblPOBox = customtkinter.CTkLabel(InnerFrame, font=('arial', 17, 'bold'), text="Father's Name")
        self.lblPOBox .grid(row=0, column=4, padx=30,pady=20, sticky=W) 
        self.txtPOBox=customtkinter.CTkEntry(InnerFrame, font=('arial', 12, 'bold'), width=160,textvariable=PoBox,
        justify='left')
        self.txtPOBox .grid(row=0, column=5)

        self.lblGender = customtkinter.CTkLabel(InnerFrame, font=('arial', 17, 'bold'), text="Gender")
        self.lblGender .grid(row=1, column=2, padx=30, sticky=W) 
        self.cboGender= customtkinter.CTkComboBox(InnerFrame,width=160,font=('arial',12,'bold'),state='readonly',
        values=['','Female','Male'],variable=Gender)
        self.cboGender.grid(row=1,column=3)        

        self.lblMobile = customtkinter.CTkLabel(InnerFrame, font=('arial', 17, 'bold'), text="Mobile No.")
        self.lblMobile .grid(row=2, column=2, padx=30,pady=20, sticky=W) 
        self.txtMobile=customtkinter.CTkEntry(InnerFrame, font=('arial', 12, 'bold'), width=160,textvariable=Mobile,
        justify='left')
        self.txtMobile.grid(row=2, column=3,sticky=W)

        self.lblEmail = customtkinter.CTkLabel(InnerFrame, font=('arial', 17, 'bold'), text="Aadhar No.")
        self.lblEmail.grid(row=1, column=4, padx=30, sticky=W) 
        self.txtEmail=customtkinter.CTkEntry(InnerFrame, font=('arial', 12, 'bold'), width=160,textvariable=Email,
        justify='left')
        self.txtEmail .grid(row=1, column=5)


        self.lblClassS = customtkinter.CTkLabel(InnerFrame, font=('arial', 17, 'bold'), text="Class")
        self.lblClassS .grid(row=2, column=4, padx=30, sticky=W) 
        self.cboClassS= customtkinter.CTkComboBox(InnerFrame,width=160,font=('arial',12,'bold'),state='readonly',
        values=['','11A1C','11A1B','11A2','11A3','11B1'],variable=ClassSec)
        self.cboClassS.grid(row=2,column=5)
        #=======================================================================================#
        def addNew():
            #MemRef()
            if StuID.get() == "" or FirstName.get() == "" or PoBox.get() =="":
                tkinter.messagebox.showerror(" Error Check Input","Enter Correct Student Details")
            else:
                sqlCon=pymysql.connect(host="localhost",user="root",password="Harsh@2002Prasad",
                database="studentrecords")
                cur=sqlCon.cursor()
                cur.execute("insert into studentrecords values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                
                StuID.get(),
                FirstName.get(),
                Gender.get(),
                PoBox.get(),
                LastName.get(),
                Mobile.get(),
                Email.get(),
                Address.get(),
                ClassSec.get()
                ))

                sqlCon.commit()
                showRecord()
                sqlCon.close()
                tkinter.messagebox.showinfo("DATA ENTRY","Success")
        
        def showRecord():
            sqlCon=pymysql.connect(host="localhost",user="root",password="Harsh@2002Prasad",
            database="studentrecords")
            cur=sqlCon.cursor()
            cur.execute("select * from studentrecords")
            result=cur.fetchall()   
            if len(result) != 0:
                self.Member_records.delete(*self.Member_records.get_children())
                for row in result:
                    self.Member_records.insert('',END,values =row)
                sqlCon.commit()
            sqlCon.close()

        def searchDB2():
            try:
                sqlCon = pymysql.connect(host="localhost",user="root",password="Harsh@2002Prasad",database="studentrecords")
                cur=sqlCon.cursor()
                cur.execute("select * from studentrecords where LastName='%s'"%Search.get())
                result=cur.fetchall()   
                if len(result) != 0:
                    self.Member_records.delete(*self.Member_records.get_children())
                    for row in result:
                        self.Member_records.insert('',END,values =row)
                sqlCon.commit()
            except:
                tkinter.messagebox.showinfo("DATA ENTRY","No Student Found")
                Search.set("")
            sqlCon.close()

        def searchDB3():
            try:
                sqlCon = pymysql.connect(host="localhost",user="root",password="Harsh@2002Prasad",database="studentrecords")
                cur=sqlCon.cursor()
                cur.execute("select * from studentrecords where ClassS='%s'"%Search.get())
                result=cur.fetchall()   
                if len(result) != 0:
                    self.Member_records.delete(*self.Member_records.get_children())
                    for row in result:
                        self.Member_records.insert('',END,values =row)
                sqlCon.commit()
            except:
                tkinter.messagebox.showinfo("DATA ENTRY","No Student Found")
                Search.set("")
            sqlCon.close()


        def MemberInfo(ev):
            viewInfo =self.Member_records.focus()
            learnerData=self.Member_records.item(viewInfo)
            row= learnerData['values']

            StuID.set(row[0])
            FirstName.set(row[1])
            LastName.set(row[4])
            Address.set(row[7])
            PoBox.set(row[3])
            Gender.set(row[2])
            Mobile.set(row[5])
            Email.set(row[6])
            ClassSec.set(row[8])

        def update():
            sqlCon = pymysql.connect(host="localhost",user="root",password="Harsh@2002Prasad",database="studentrecords")
            cur=sqlCon.cursor()
            cur.execute("update studentrecords set firstname=%s,gender=%s,pobox=%s,lastname=%s,"
            "mobile=%s,email=%s,address=%s,classS=%s where StuID=%s",(
            
            FirstName.get(),
            Gender.get(),
            PoBox.get(),
            LastName.get(),
            Mobile.get(),
            Email.get(),
            Address.get(),
            ClassSec.get(),
            StuID.get() 
            
            ))
            sqlCon.commit()
            showRecord()
            sqlCon.close()
            tkinter.messagebox.showinfo("DATA ENTRY","Updated Successfully")

        def deleteDB():
            sqlCon = pymysql.connect(host="localhost",user="root",password="Harsh@2002Prasad",database="studentrecords")
            cur=sqlCon.cursor()
            cur.execute("delete from studentrecords where StuID=%s",StuID.get())

            sqlCon.commit()
            showRecord()
            sqlCon.close()
            tkinter.messagebox.showinfo("DATA ENTRY","Deleted Successfully")
            Reset()


        def searchDB():
            try:
                sqlCon = pymysql.connect(host="localhost",user="root",password="Harsh@2002Prasad",database="studentrecords")
                cur=sqlCon.cursor()
                cur.execute("select * from studentrecords where StuID='%s'"%Search.get())

                row=cur.fetchone()

                StuID.set(row[0])
                FirstName.set(row[1])
                LastName.set(row[4])
                Address.set(row[7])
                PoBox.set(row[3])
                Gender.set(row[2])
                Mobile.set(row[5])
                Email.set(row[6])
                ClassSec.set(row[8])
                sqlCon.commit()
            except:
                tkinter.messagebox.showinfo("DATA ENTRY","No Student Found")
                Search.set("")
            
            sqlCon.close()

       
        
        
        #=======================================================================================#
        self.txtSearch=customtkinter.CTkEntry(SearchFrames,font=('Arial',12),width=150,textvariable=Search,justify='left')
        self.txtSearch.grid(row=0,column=2,sticky="nsew")
        self.btnSearch= customtkinter.CTkButton(SearchFrames,font=('Arial',15,'bold'),text="Search By StudentID",
        width=20,height=1,command=searchDB).grid(row=0,column=3,padx=5)
        
        self.btnSearch= customtkinter.CTkButton(SearchFrames,font=('Arial',15,'bold'),text="Search By Father's Occupation",
        width=25,height=1,command=searchDB2).grid(row=0,column=4,padx=5)

        self.btnSearch= customtkinter.CTkButton(SearchFrames,font=('Arial',15,'bold'),text="Filter By Class",
        width=25,height=1,command=searchDB3).grid(row=0,column=5,padx=5)
        #=======================================================================================#

        self.btnAddNew= customtkinter.CTkButton(ButtonFrames,fg_color='green',font=('Arial',16,'bold'),
        text="ADD NEW",width=11,height=5,command=addNew).grid(row=0,column=0,padx=10)
        
        self.btnShowRecord= customtkinter.CTkButton(ButtonFrames,fg_color='green',font=('Arial',16,'bold'),
        text="SHOW ALL RECORD",width=11,height=5,command=showRecord).grid(row=0,column=1,padx=10)
        
        self.btnUpdate= customtkinter.CTkButton(ButtonFrames,fg_color='green',font=('Arial',16,'bold'),
        text="UPDATE",width=11,height=5,command=update).grid(row=0,column=2,padx=10)
        
        self.btnDelete= customtkinter.CTkButton(ButtonFrames,fg_color='green',font=('Arial',16,'bold'),
        text="DELETE",width=11,height=5,command=deleteDB).grid(row=0,column=3,padx=10)
        
        self.btnReset= customtkinter.CTkButton(ButtonFrames,fg_color='green',font=('Arial',16,'bold'),
        text="RESET",width=11,height=5,command=Reset).grid(row=0,column=4,padx=10)
        
        self.btnExit= customtkinter.CTkButton(ButtonFrames,fg_color='green',font=('Arial',16,'bold'),
        text="EXIT",width=11,height=5,command=iExit).grid(row=0,column=5,padx=10)
        #=======================================================================================#
        scroll_y=Scrollbar(TreeViewFrames,orient=VERTICAL)

        self.Member_records=ttk.Treeview(TreeViewFrames,height=12,columns=("stuid", "firstname","gender",
        "pobox","lastname","mobile","email","address","classS"),yscrollcommand=scroll_y.set)
        
        scroll_y.pack(side=RIGHT,fill=Y)

        self.Member_records.heading("stuid",text="STUDENT ID")
        self.Member_records.heading("firstname",text="STUDENT NAME")
        self.Member_records.heading("gender",text="GENDER")
        self.Member_records.heading("pobox",text="FATHER's NAME")
        self.Member_records.heading("lastname",text="FATHER's OCCUPATION")
        self.Member_records.heading("mobile",text="MOBILE NO.")
        self.Member_records.heading("email",text="AADHAR No.")
        self.Member_records.heading("address",text="ADDRESS")
        self.Member_records.heading("classS",text="CLASS")

        self.Member_records['show']='headings'

        self.Member_records.column("stuid",width=80)
        self.Member_records.column("firstname",width=100)
        self.Member_records.column("gender",width=60)
        self.Member_records.column("pobox",width=100)
        self.Member_records.column("lastname",width=100)
        self.Member_records.column("mobile",width=100)
        self.Member_records.column("email",width=100)
        self.Member_records.column("address",width=350)
        self.Member_records.column("classS",width=65)

        self.Member_records.pack(fill=BOTH,expand=1)
        self.Member_records.bind("<ButtonRelease-1>",MemberInfo)

        showRecord()  

        #=======================================================================================#

if __name__ == "__main__":
    root =Tk()
    application = MemberConnect(root)
    root.mainloop()