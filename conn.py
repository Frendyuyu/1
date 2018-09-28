import pyodbc
data={}
countn=0
DBfile = r"D:\wwwroot\DB\Material.accdb;"  # 数据库文件
conn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + DBfile)

cursor = conn.cursor()
SQL = "SELECT * from Dri;"
for row in cursor.execute(SQL):
    data[countn]= row
    countn = countn + 1
    print (row)
print(type(row))

cursor.close()
conn.close()

print ("===============================================")
print (row)
print ("===============================================")
print (data)
print ("===============================================")
print (countn)

inp_val = int(input("输入序号："))
if inp_val <countn or inp_val ==countn:
    print (data[inp_val])
