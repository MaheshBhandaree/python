import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="Mahesh@123",database="employeedata")
mycursor = mydb.cursor()
mycursor.execute("Insert into student values(1,'mahesh','math')")
for i in mycursor:
    print(i)

