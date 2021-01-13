#Importing functions and connecting python to MySQL
import tkinter as tt
from tkinter import messagebox 
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="password")
mycursor=mydb.cursor()

"For this prototype to function efficiently the required tables and databases must be present in the system prior to running the code."
"To create the required DB and relation please run the codes from lines 11 to 14 separately"
#Creating database and relations in MySQL
'''mycursor.execute('create database bloodbankk')'''
mycursor.execute('use bloodbankk')
'''mycursor.execute('create table registration(ID integer,name varchar(25), age integer,gender varchar(10),bloodgroup varchar(10), phone_no integer, address varchar(50), city varchar(25), country varchar(25),email_id varchar(50), password varchar(50))' )
mycursor.execute('create table requestblood(Patient_ID integer,Patient_name varchar(25), Patient_age integer,Patient_gender varchar(10),Patient_bloodgroup varchar(10),Hospital_name varchar(50),date_of_requirement date,units_required integer,Hospital_address varchar(50),contact_no integer)' )
'''

#First page
window = tt.Tk()
window.title("Blood Bank")
window.geometry("500x400")

#First page labels
heading = tt.Label(window, text="BLOOD BANK").grid(row=0, column=1)

#First page windows
def homeWind():
    homeWind = tt.Toplevel(window)
    homeWind.title("Home")
    homeWind.geometry("800x600")
    hwlb1=tt.Label(homeWind,text='Who can donate blood? \n ->The donor must be in good health. \n ->Donor must weigh atleast 110 pounds. \n ->Donor must be 17 years or older. \n').pack()
    hwlb2=tt.Label(homeWind,text='Blood Platelets Donation: \n What is a platelets donation? \n It is a special type of blood donation where the platelets are collected through a device called Apheresis machine or \n Cell Separator, which separate the platelet cells from the rest of blood components.\n').pack()
    hwlb3=tt.Label(homeWind,text='What is the importance of donating platelets?\n Platelets are important to save the lives of many patients including \n ->Patients injured in accidents, burns and major surgeries such as open heart surgery and organ transplantation \n ->Patients who suffer from a decreased number of  platelets  such as cancer patients especially those receiving chemotherapy \n ->Patients who have a bone marrow transplant \n ->Patients with severe bleeding such as women in childbirth and premature infants. \n').pack()                
    hwlb4=tt.Label(homeWind,text=' Who is eligible for Platelet Donation?\n Those eligible for platelets donations:\n Are those in good general health\n Age between 18-65 years\n With body weight of more than 50 kg\n Have not taken aspirin or any medication that contains aspirin compound or antibiotics during the past days.\n Have a hemoglobin level from (13-18 grams per deciliter)\n Have a platelet count between (150 to 450 thousand). \n').pack()
    hwlb5=tt.Label(homeWind,text='What is the process of donating platelets through the device for separating blood components?\n The device withdraws blood from the donors body and separates it to its components, keeps the platelets \n in a side bag and then returns the rest of the blood components to the body of the donor, \n This process takes about one hour amid careful monitoring and follow-up by qualified nurses. \n\n How many platelets can be collected at each donation? And how many times can a healthy individual donate? \n The volume of platelets that can be donated in normal conditions ranges from 250 to 300 milliliters \n  A person must wait a minimum of 56 days between whole blood donations. \n  For platelet donation, healthy people who meet the requirements of the donation can donate every 72 hours \n Note: Laboratory tests will be conducted on the donor before donation to confirm the number of platelets in body and concentration \n of red blood cells in the blood so that you can donate using the technique of automatically separating blood components. \n').pack()
                     
def register():             
    window = tt.Tk()
    window.title('Donor Registration')
    window.geometry("600x500")
    label = tt.Label( window,text = "Registration Page").place(x=140,y=0)
    
    namelb = tt.Label(window,text = "Name").place(x = 30,y = 50)
    nametb = tt.Entry(window)
    nametb.place(x = 120, y = 50)
    
    agelb = tt.Label(window,text = "Age").place(x = 30,y = 70)
    agetb = tt.Entry(window)
    agetb.place(x = 120, y = 70)
    
    genderlb=tt.Label(window,text='Gender').place(x=30,y=90)
    gen=tt.IntVar(window)
    mgen=tt.Radiobutton(window,text='Male',variable=gen,state='normal',value=1)
    mgen.place(x=120,y=90)
    fgen=tt.Radiobutton(window,text='Female',variable=gen,state='normal',value=2)
    fgen.place(x=120,y=110)
    
    bldgrplb=tt.Label(window,text='Blood Group').place(x=30,y=140)
    b=tt.StringVar(window)
    bldgrp=['A+','A-','B+','B-','AB+','AB-','O+','O-']
    bldgrplist=tt.OptionMenu(window,b,*bldgrp)
    bldgrplist.place(x=120,y=140)
    b.set('Select Blood Group')
    
    phnolb=tt.Label(window,text='Phone Number').place(x=30,y=170)
    phnotb = tt.Entry(window)
    phnotb.place(x = 120, y = 170)
    
    addresslb=tt.Label(window,text='Address').place(x=30,y=190)
    addresstb = tt.Entry(window)
    addresstb.place(x = 120, y = 190)
    
    citylb=tt.Label(window,text='City').place(x=30,y=210)
    citytb = tt.Entry(window)
    citytb.place(x = 120, y = 210)
    
    countrylb=tt.Label(window,text='Country').place(x=30,y=230)
    countrytb = tt.Entry(window)
    countrytb.place(x = 120, y = 230)
    
    emaillb=tt.Label(window,text='Email').place(x=30,y=250)
    emailtb = tt.Entry(window)
    emailtb.place(x = 120, y = 250)
    
    passwordlb=tt.Label(window,text='Password').place(x=30,y=280)
    passwordtb = tt.Entry(window)
    passwordtb.place(x = 120, y = 280)
    
    def donorid():
            mycursor.execute('select * from registration')
            mydata=mycursor.fetchall()
            nid=mycursor.rowcount
            return nid
    
    def click():
        if gen.get()==1:
            gender='Male'
        elif gen.get()==2:
            gender='Female'
        bloodgroup=b.get()
        name=nametb.get()
        age=agetb.get()
        password=passwordtb.get()
        phno=phnotb.get()
        city=citytb.get()
        address=addresstb.get()
        dID=donorid()+1
        country=countrytb.get()
        email=emailtb.get()
        
        msgbox=tt.messagebox.showinfo('','registration successful '+nametb.get()+'!')
        myquery="insert into registration(ID,name,age,gender,bloodgroup,phone_no,address,city,country,email_id,password) values({0},'{1}',{2},'{3}','{4}',{5},'{6}','{7}','{8}','{9}','{10}')".format(dID,name,age,gender,bloodgroup,phno,address,city,country,email,password)
        mycursor.execute(myquery)
        mydb.commit()
    
    registerbutton=tt.Button(window,text='Submit',command=click).place(x=100,y=300)
    window.mainloop()

def requestblood():
    window = tt.Tk()
    window.title('Recipient Registration')
    window.geometry("600x500")
    label = tt.Label( window,text = "Recipient Registration").place(x=140,y=0)
    
    pnamelb = tt.Label(window,text = "Patient Name").place(x = 30,y = 50)
    pnametb = tt.Entry(window)
    pnametb.place(x = 120, y = 50)
    
    pagelb = tt.Label(window,text = "Patient Age").place(x = 30,y = 70)
    pagetb = tt.Entry(window)
    pagetb.place(x = 120, y = 70)
    
    pgenderlb=tt.Label(window,text='Patient Gender').place(x=30,y=90)
    pgen=tt.IntVar(window)
    pmgen=tt.Radiobutton(window,text='Male',variable=pgen,state='normal',value=1)
    pmgen.place(x=120,y=90)
    pfgen=tt.Radiobutton(window,text='Female',variable=pgen,state='normal',value=2)
    pfgen.place(x=120,y=110)
    
    pbldgrplb=tt.Label(window,text='Patient Blood Group').place(x=30,y=140)
    pb=tt.StringVar(window)
    pbldgrp=['A+','A-','B+','B-','AB+','AB-','O+','O-']
    pbldgrplist=tt.OptionMenu(window,pb,*pbldgrp)
    pbldgrplist.place(x=150,y=140)
    pb.set('Select Blood Group')

    hospitalnamelb=tt.Label(window,text='Hospital Name').place(x=30,y=170)
    hospitalnametb = tt.Entry(window)
    hospitalnametb.place(x = 150, y = 170)
    
    datelb=tt.Label(window,text='Date of Requirement').place(x=30,y=210)
    datetb = tt.Entry(window)
    datetb.place(x = 150, y = 210)
    datetb.insert(0,"YYYY-MM-DD")
    
    unitslb=tt.Label(window,text='No. of Units Required').place(x=30,y=190)
    unitstb = tt.Entry(window)
    unitstb.place(x = 150, y = 190)
    
    hospitaladdresslb=tt.Label(window,text='Hospital Address').place(x=30,y=230)
    hospitaladdresstb = tt.Entry(window)
    hospitaladdresstb.place(x = 150, y = 230)
    
    contactphnolb=tt.Label(window,text='Contact phone no.').place(x=30,y=250)
    contactphnotb = tt.Entry(window)
    contactphnotb.place(x = 150, y = 250)
    
    def Patientid():
            mycursor.execute('select * from requestblood')
            mydata=mycursor.fetchall()
            nid=mycursor.rowcount
            return nid

    def click():
        if pgen.get()==1:
            gender='Male'
        elif pgen.get()==2:
            gender='Female'

        bloodgroup=pb.get()
        age=pagetb.get()
        name=pnametb.get()
        hname=hospitalnametb.get()
        dor=datetb.get()
        units=unitstb.get()
        PID=Patientid()+1
        haddress=hospitaladdresstb.get()
        contact=contactphnotb.get()

        msgbox=tt.messagebox.showinfo('','request successful !')
        myquery="insert into requestblood(Patient_ID,Patient_name,Patient_age,Patient_gender,Patient_bloodgroup,Hospital_name,date_of_requirement,units_required,Hospital_address,contact_no) values({0},'{1}',{2},'{3}','{4}','{5}','{6}',{7},'{8}',{9})".format(PID,name,age,gender,bloodgroup,hname,dor,units,haddress,contact)
        mycursor.execute(myquery)
        mydb.commit()
    requestbutton=tt.Button(window,text='Submit',command=click).place(x=100,y=300)
    window.mainloop()

def searchdonor():
    window = tt.Tk()
    window.title('Search for Donor')
    window.geometry("600x500")
    label = tt.Label( window,text = "Search Donor").place(x=140,y=0)

    searchlb=tt.Label(window,text='Select Blood Group',font=(20)).place(x=30,y=60)
    search=tt.StringVar(window)
    searchbldgrp=['A+','A-','B+','B-','AB+','AB-','O+','O-']
    searchbldgrplist=tt.OptionMenu(window,search,*searchbldgrp)
    searchbldgrplist.place(x=190,y=60)

    def searchresult():
        s=search.get()
        mycursor.execute("select name,age,gender,phone_no from registration where bloodgroup='{0}'".format(s))
        mydata=mycursor.fetchall()
        nrec=mycursor.rowcount
        l1=tt.Label(window,text='Search results:'+s)
        l1.place(x=30,y=150)
        if nrec==0:
            l1=tt.Label(window,text='no records found')
            l1.place(x=30,y=170)
        else:
            n=0
            p=170
            l3=tt.Label(window,text='sno.  name      age    gender   phone_no ')
            l3.place(x=30,y=170)
            
            for i in mydata:
                y=''
                n=n+1
                y=str(n)+'        '
                for j in i:
                    y=y+str(j)+'    '
                p=p+20
                tt.Label(window,text=y).place(x=30,y=p)
                
    def clearsearch():
        tt.Label(window,text=' ',height=100,width=100).place(x=30,y=170)   
    clear=tt.Button(window,text='Clear Search',command=clearsearch).place(x=130,y=100)
    result=tt.Button(window,text='Search',command=searchresult).place(x=80,y=100)

def abtusWind():
    abtusWind = tt.Toplevel(window)
    abtusWind.title("About Us")
    abtusWind.geometry("600x500")
    abtusLbl = tt.Label(abtusWind, text="Blood banking includes tasks related to blood collection, processing, testing, separation, and storage. \n Please visit one of the two locations below:\n Blood Donor Center at Hamad Medical Corporation, next to Hamad General Hospital\n Official Working Hours:\n Sunday to Thursday: 7am to 7pm\n Saturday: 8am to 8pm\n The new blood donor center next to HMC’s Ambulatory Care Center\n Working Hours:\n Sunday to Thursday: 7am to 1pm\n For more information, please contact the Center on: 44391081/44391082\n Thank you for your support and cooperation\n Blood Donation Center\n Hamad Medical Corporation").pack()

def loginWind():
    loginWind = tt.Toplevel(window)
    loginWind.title("login")
    loginWind.geometry("600x500")

    name_var=tt.StringVar()
    pass_var=tt.StringVar()

    def lgop():
        lgop = tt.Toplevel(loginWind)
        lgop.title("Login Output")
        lgop.geometry("600x500")

        U=usnme.get()
        P=passwd.get()
        name_var.set("")
        pass_var.set("")

        mycursor.execute("select* from registration where name='{}' and password='{}'".format(U,P))
        lop= mycursor.fetchall()
        n=mycursor.rowcount
        mycursor.execute("desc registration")
        col=mycursor.fetchall()
        r=2
        q=2
        if n==0:
            nmlbl= tt.Label(lgop, text="Incorrect password or username entered. Please try again").grid(row=0, column=0)
        else:
            nmlbl= tt.Label(lgop, text="Donor Details").grid(row=0, column=0)
            for x in col:
                y=x[0]
                colbl= tt.Label(lgop, text=y).grid(row=r, column=0)
                r+=1
            for i in lop:
                for j in i:
                    nmlbl= tt.Label(lgop, text=j).grid(row=q, column=14)
                    q=q+1
      

    usnmL = tt.Label(loginWind, text="Username").grid(row=0, column=0)
    usnme = tt.Entry(loginWind, textvariable=name_var)
    usnme.grid(row=0, column=1)

    passwdL = tt.Label(loginWind, text="Password").grid(row=1, column=0)
    passwd = tt.Entry(loginWind, textvariable=pass_var)
    passwd.grid(row=1, column=1)
 
    lgopBttn = tt.Button(loginWind, text="Login", command=lgop).grid(row=5, column=5)    

        
#First page buttons
homeBttn = tt.Button(window, text="Home", command=homeWind).grid(row=1, column=0)      
blavilBttn = tt.Button(window, text="Recipient Registration", command=requestblood).grid(row=1, column=1)
srchdonBttn = tt.Button(window, text="Search Donor", command=searchdonor).grid(row=1, column=2)
loginBttn = tt.Button(window, text="Login", command=loginWind).grid(row=2, column=0)
regisBttn = tt.Button(window, text="Donor Registration", command=register).grid(row=2, column=1)
abtusBttn = tt.Button(window, text="About us", command=abtusWind).grid(row=2, column=2)
