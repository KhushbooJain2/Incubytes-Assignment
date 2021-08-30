import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                    'Server=DESKTOP-MKEVRNV\SQLExpress;'
                    'Database=Incubytes;'
                    'Trusted_Connection=yes;')

cursor = conn.cursor()

s=input('Enter Country:')
cursor.execute("SELECT Customer_Name,Customer_ID,Customer_Open_Date,Last_Consulted_Date,Vaccination_Type,Doctor_Consulted,State,Country,Post_Code,Date_of_Birth,Active_Customer FROM tbl_customerdetails where Country like '"+s+"' ")
f = open('demo.txt', 'a')

for row in cursor:
    f.write(str(row.Customer_Name +"|"+row.Customer_ID+"|"+row.Customer_Open_Date.replace('-', '')+"|"+row.Last_Consulted_Date.replace('-', '')+"|"+row.Vaccination_Type.strip()+"|"+row.Doctor_Consulted.strip()+"|"+row.State.strip()+"|"+row.Country.strip()+"|"))
    f.write(str(row.Post_Code))
    f.write(str("|"+row.Date_of_Birth.replace('-', '')+"|"+row.Active_Customer +"\n"))
f.close()

f1 = open("demo.txt" )
print("output:")
print(f1.read())
f1.close()