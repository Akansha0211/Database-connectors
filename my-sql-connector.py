#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector as connection


# In[2]:


mydb = connection.connect(host="localhost", user="root", passwd = "h0212", use_pure=True)


# In[3]:


print(mydb.is_connected())


# In[4]:


mydb.close()


# ### Will reduce error string

# In[5]:


try:
    mydb = connection.connect(host="localhost", user="root", passwd="h012", use_pure=True)
    print(mydb.is_connected())
    mydb.close()
except Exception as e:
    mydb.close()
    print(str(e))
    


# In[6]:


try:
    mydb = connection.connect(host="localhost", user="root", passwd="h0212", use_pure=True)
    print(mydb.is_connected())
    mydb.close()
except Exception as e:
    mydb.close()
    print(str(e))
    


# ### Will print a DB names

# In[7]:


mydb = connection.connect(host="localhost", user="root", passwd="h0212", use_pure=True)
cursor = mydb.cursor()
cursor.execute("Show databases")
cursor.fetchall()


# In[8]:


type(cursor.fetchall())


# In[9]:


mydb.close()
print(mydb.is_connected())


# ### Fetchal() retuns dbnames in list 

# In[10]:


mydb = connection.connect(host="localhost", user="root", passwd="h0212", use_pure=True)
cursor = mydb.cursor()
cursor.execute("Show Databases")
db_name = cursor.fetchall()
for i in db_name:
    print(i)


# In[11]:


mydb.close()


# In[11]:





# In[12]:


mydb = connection.connect(host="localhost", user="root", passwd="h0212", use_pure=True)
cursor = mydb.cursor()
cursor.execute("Create Database AKTest")


# In[ ]:





# In[14]:


query = "Create database PracticeSQL;"
cursor = mydb.cursor()
cursor.execute(query)
print("Database created!!")
mydb.close()


# In[16]:


mydb = connection.connect(host="localhost", user="root",database="akansha", passwd="h0212",use_pure=True)
query = "Create table studentRecords(studentId INT(10) AUTO_INCREMENT PRIMARY KEY, FirstName Varchar(60),LastName Varchar(60),RegsitrationDate DATE ,Class Varchar(10),Section Varchar(10))"
cursor = mydb.cursor()
cursor.execute(query)
print("Table StudentRecords created!!")
mydb.close()


# In[25]:


try:
    mydb = connection.connect(host="localhost", database="akansha", user="root", passwd="h0212", use_pure=True)
#     print(mydb.is_connected())
    cursor = mydb.cursor()
    cursor.execute("Select * from StudentRecords")
    for i in cursor.fetchall():
        print(i)
    mydb.close()
except Exception as e:
    mydb.close()
    print(str(e))


# In[ ]:


# studentId INT(10) AUTO_INCREMENT PRIMARY KEY
# FirstName Varchar(60)
# LastName Varchar(60)
# RegsitrationDate DATE
# Class Varchar(10)
# Section Varchar(10)


# In[33]:


mydb = connection.connect(host="localhost", database="akansha", user="root", passwd="h0212", use_pure=True)
print(mydb.is_connected())
query="Insert into StudentRecords Values(96,'Akansha','Saxena','2021-02-15','ML','A')"
cursor = mydb.cursor()
cursor.execute(query)
print("Values inserted into table StudentRecords of db akansha")
# necessary to write this if you are writing data into database
mydb.commit(); 
mydb.close()


# ### Writing data with same primary key will give Integrity Error

# In[36]:


try:
    mydb = connection.connect(host="localhost", database="akansha", user="root", passwd="h0212", use_pure=True)
    print(mydb.is_connected())
    query="Insert into StudentRecords Values(96,'Akansha','Saxena','2021-02-15','ML','A')"
    cursor = mydb.cursor()
    cursor.execute(query)
    print("Values inserted into table StudentRecords of db akansha")
    # necessary to write this if you are writing data into database
    mydb.commit(); 
    mydb.close()
except Exception as e:
    mydb.close()
    print(str(e))
    


# In[ ]:





# In[34]:


try:
    mydb = connection.connect(host="localhost", database="akansha", user="root", passwd="h0212", use_pure=True)
#     print(mydb.is_connected())
    cursor = mydb.cursor()
    cursor.execute("Select * from StudentRecords")
    for i in cursor.fetchall():
        print(i)
    mydb.close()
except Exception as e:
    mydb.close()
    print(str(e))


# In[43]:


mydb = connection.connect(host="localhost", database="akansha", user="root", passwd="h0212", use_pure=True)
mydb.is_connected()
cursor = mydb.cursor()
cursor.execute("Select StudentId from StudentRecords")
for i in cursor.fetchall():
    print(i)


# In[ ]:





# In[ ]:





# In[46]:


# import csv
# with open("glass.data", "r") as f :
#     glass_data = csv.reader(f, delimiter="\n")
#     print(glass_data)
#     for i in enumerate(glass_data):
# #         print(i)
#         for list in (line[1]):
#             cursor.execute("INSERT INTO GlassData")

    


# In[ ]:





# In[ ]:





# In[5]:


# import mysql.connector as connection

# try:
#     mydb = connection.connect(host="localhost",user="root", passwd="mysql",use_pure=True)
#     # check if the connection is established

#     query = "SHOW DATABASES"

#     cursor = mydb.cursor() #create a cursor to execute queries
#     cursor.execute(query)
#     print(cursor.fetchall())

# except Exception as e:
#     mydb.close()
#     print(str(e))


# In[4]:


# import mysql.connector as connection

# try:
#     mydb = connection.connect(host="localhost", user="root", passwd="mysql",use_pure=True)
#     # check if the connection is established
#     print(mydb.is_connected())

#     query = "Create database Student;"
#     cursor = mydb.cursor() #create a cursor to execute queries
#     cursor.execute(query)
#     print("Database Created!!")
#     mydb.close()
# except Exception as e:
#     mydb.close()
#     print(str(e))


# In[6]:


# import mysql.connector as connection

# try:
#     mydb = connection.connect(host="localhost", database = 'Student',user="root", passwd="mysql",use_pure=True)
#     # check if the connection is established
#     print(mydb.is_connected())

#     query = "CREATE TABLE StudentDetails (Studentid INT(10) AUTO_INCREMENT PRIMARY KEY,FirstName VARCHAR(60)," \
#             "LastName VARCHAR(60), RegistrationDate DATE,Class Varchar(20), Section Varchar(10))"

#     cursor = mydb.cursor() #create a cursor to execute queries
#     cursor.execute(query)
#     print("Table Created!!")
#     mydb.close()
# except Exception as e:
#     mydb.close()
#     print(str(e))


# In[7]:


# import mysql.connector as connection

# try:
#     mydb = connection.connect(host="localhost", database = 'Student',user="root", passwd="mysql",use_pure=True)
#     # check if the connection is established
#     print(mydb.is_connected())
#     query = "INSERT INTO StudentDetails VALUES ('1132','Sachin','Kumar','1997-11-11','Eleventh','A')"

#     cursor = mydb.cursor() #create a cursor to execute queries
#     cursor.execute(query)
#     print("Values inserted into the table!!")
#     mydb.commit()
#     mydb.close()
# except Exception as e:
#     mydb.close()
#     print(str(e))


# In[8]:


# import mysql.connector as connection


# try:
#     mydb = connection.connect(host="localhost", database = 'GlassData',user="root", passwd="mysql",use_pure=True)
#     #check if the connection is established
#     print(mydb.is_connected())
#     query = "Select * from GlassData;"
#     cursor = mydb.cursor() #create a cursor to execute queries
#     cursor.execute(query)
#     for result in cursor.fetchall():
#         print(result)
#     mydb.close() #close the connection


# except Exception as e:
#     #mydb.close()
#     print(str(e))


# In[9]:


# import mysql.connector as connection
# import pandas as pandas

# try:

#     mydb = connection.connect(host="localhost", database='Student', user="root", passwd="mysql", use_pure=True)
#     # check if the connection is established
#     print(mydb.is_connected())
#     query = "UPDATE studentdetails SET FirstName = 'Kumar', LastName = 'Gaurav' WHERE Studentid = 1122"
#     cursor = mydb.cursor()  # create a cursor to execute queries
#     cursor.execute(query)
#     mydb.commit()

#     #let's check if the value is updated in the table.
#     query = "Select * from studentdetails where Studentid=1122;"
#     cursor = mydb.cursor()  # create a cursor to execute queries
#     cursor.execute(query)
#     for result in cursor.fetchall():
#         print(result)

#     mydb.close()  # close the connection

# except Exception as e:
#     #mydb.close()
#     print(str(e))


# In[10]:


# import mysql.connector as connection
# import pandas as pandas

# try:

#     mydb = connection.connect(host="localhost", database='GlassData', user="root", passwd="mysql", use_pure=True)
#     # check if the connection is established
#     print(mydb.is_connected())
#     query = "Select * from GlassData;"
#     result_dataFrame = pandas.read_sql(query,mydb)
#     print(result_dataFrame)

#     mydb.close()  # close the connection

# except Exception as e:
#     #mydb.close()
#     print(str(e))


# In[44]:


# import mysql.connector as connection


# try:
#     mydb = connection.connect(host="localhost", database = 'GlassData',user="root", passwd="mysql",use_pure=True)
#     #check if the connection is established
#     print(mydb.is_connected())
#     query = "Select * from GlassData;"
#     cursor = mydb.cursor() #create a cursor to execute queries
#     cursor.execute(query)
#     for result in cursor.fetchall():
#         print(result)
#     mydb.close() #close the connection


# except Exception as e:
#     #mydb.close()
#     print(str(e))


# In[45]:


import mysql.connector as connection

# try:

#     mydb = connection.connect(host="localhost", database='Student', user="root", passwd="mysql", use_pure=True)
#     # check if the connection is established
#     print(mydb.is_connected())
#     query = "DELETE FROM studentdetails WHERE Studentid = 1122"
#     cursor = mydb.cursor()  # create a cursor to execute queries
#     cursor.execute(query)
#     mydb.commit()

#     #let's check if the value is updated in the table.
#     query = "Select * from studentdetails where Studentid=1122;"
#     cursor = mydb.cursor()  # create a cursor to execute queries
#     cursor.execute(query)
#     for result in cursor.fetchall():
#         print(result)

#     mydb.close()  # close the connection

# except Exception as e:
#     #mydb.close()
#     print(str(e))


# In[14]:


# import mysql.connector as connection
# import pandas as pandas
# import csv

# try:
#     mydb = connection.connect(host="localhost", user="root", passwd="mysql",use_pure=True)
#     #check if the connection is established
#     print(mydb.is_connected())
#     #create a new database
#     query = "Create database GlassData;"
#     cursor = mydb.cursor() #create a cursor to execute queries
#     cursor.execute(query)
#     print("Database Created!!")
#     mydb.close() #close the connection

#     #Establish a new connection to the database created above
#     mydb = connection.connect(host="localhost", database = 'GlassData',user="root", passwd="mysql", use_pure=True)

#     #create a new table to store glass data
#     query = "CREATE TABLE IF NOT EXISTS GlassData (Index_Number INT(10),RI float(10,5), Na float(10,5), Mg float(10,5),Al float(10,5)," \
#             " Si float(10,5), K float(10,5), Ca float(10,5), Ba float(10,5), Fe float(10,5), Class INT(5))"
#     cursor = mydb.cursor()  # create a cursor to execute queries
#     cursor.execute(query)
#     print("Table Created!!")

#     #read from the file
#     with open('glass.data', "r") as f:
#         next(f)
#         glass_data = csv.reader(f, delimiter="\n")
#         for line in enumerate(glass_data):
#             for list_ in (line[1]):
#                 cursor.execute('INSERT INTO GlassData values ({values})'.format(values=(list_)))
#     print("Values inserted!!")
#     mydb.commit()
#     cursor.close()
#     mydb.close()

# except Exception as e:
#     #mydb.close()
#     print(str(e))


# In[50]:


import csv
with open('glass.data', "r") as f:
    data = csv.reader(f, delimiter="\n")
    print(data)
    for line in enumerate(data):
        print(line)


# In[ ]:




