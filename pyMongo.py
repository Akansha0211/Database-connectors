#!/usr/bin/env python
# coding: utf-8

# <img src="https://d24cdstip7q8pz.cloudfront.net/t/ineuron1/content/common/images/final%20logo.png" height=60 alt-text="iNeuron.ai logo">

# ## 19.3.2 Open MongoDB compass to visually see what each python commands does
# 
# You'll see below screen -
# 
# > ![first screen](mongo_img/compass/c1.JPG)

# ### STEP 1: Create a DB

# In[2]:


import pymongo


# In[2]:


# DEFAULT_CONNECTION_URL = "mongodb://localhost:27017/"
# DB_NAME = "iNeuron"

# # Establish a connection with mongoDB
# client = pymongo.MongoClient(DEFAULT_CONNECTION_URL)

# # Create a DB
# dataBase = client[DB_NAME]


# In[ ]:





# ### Check for databases already present

# In[7]:


client = pymongo.MongoClient("mongodb://localhost:27017")
client.list_database_names()


# ---
# 
# ### Paste the default URL in highlighted area of the Compass tool as shown below and click on connect
# default URL for local system:- 
# ```
# mongodb://localhost:27017/
# ```
# 
# > ![new connection](mongo_img/compass/c2.JPG)
# 
# after you press connect you'll see the following screen which contains already existing databases
# 
# > ![new connection](mongo_img/compass/c3.JPG)
# 
# 
# **NOTE** you'll not see your database untill or unless you have created first document inside it. So at present we don't have any document in our DB its name is not visible here 
# 
# You can also create a database by clicking on CREATE DATABSE button. You'll see a below screen (But we'll see eveyrthing using python)
# 
# > ![new connection](mongo_img/compass/c4.JPG)

# In[ ]:


# lets see what the existing list of DBs -

client.list_database_names()


# In[ ]:





# ### Database created but collection still not added 

# In[18]:


client = pymongo.MongoClient("mongodb://localhost:27017")
client.list_database_names()
DB_NAME = "iNeuron"
dataBase = client[DB_NAME]


# In[19]:


client.list_database_names()


# ### Check whether a Database is presnt in Database list

# In[20]:


def checkExistence_DB(DB_NAME, client):
    DB_List = client.list_database_names()
    if DB_NAME in DB_List:
        print(f"DB: '{DB_NAME}' EXISTS")
        return True
    print(f"DB: '{DB_NAME}' NOT PRESENT OR NO COLLECTION PRESENT IN IT YET")
    return False
_ = checkExistence_DB(DB_NAME, client)


# In[ ]:





# In[4]:


# let's verify whether we have our database in the list or not 
# we'll use the following function:-

# def checkExistence_DB(DB_NAME, client):
#     """It verifies the existence of DB"""
#     DBlist = client.list_database_names()
#     if DB_NAME in DBlist:
#         print(f"DB: '{DB_NAME}' exists")
#         return True
#     print(f"DB: '{DB_NAME}' not yet present OR no collection is present in the DB")
#     return False


# _ = checkExistence_DB(DB_NAME=DB_NAME, client=client)


# ### STEP 2: Create a collection

# In[5]:





# In[ ]:





# In[21]:


Collection_name = "iNeuron_Products"
collection = dataBase[Collection_name]


# In[22]:


client.list_database_names()


# In[23]:


def checkExistence_Col(Collection_name, DB_NAME, db):
    collection_list = db.list_collection_names()
    if Collection_name in collection_list:
        print(f"'{Collection_name}' present in DB '{DB_NAME}'")
        return True
    print("Collection '{Collection_name}' in database '{DB_NAME}' exists")
    return True
_= checkExistence_Col(Collection_name, DB_NAME, dataBase)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


# COLLECTION_NAME = "iNeuron_Products"
# collection = dataBase[COLLECTION_NAME]


# In[6]:


# let's verify whether we have our database in the list or not 
# we'll use the following function:-

# def checkExistence_COL(COLLECTION_NAME, DB_NAME, db):
#     """It verifies the existence of collection name in a database"""
#     collection_list = db.list_collection_names()
    
#     if COLLECTION_NAME in collection_list:
#         print(f"Collection:'{COLLECTION_NAME}' in Database:'{DB_NAME}' exists")
#         return True
    
#     print(f"Collection:'{COLLECTION_NAME}' in Database:'{DB_NAME}' does not exists OR \n\
#     no documents are present in the collection")
#     return False


# _ = checkExistence_COL(COLLECTION_NAME=COLLECTION_NAME, DB_NAME=DB_NAME, db=dataBase)


# ### STEP 3: Insert a record in the collection

# In[ ]:





# In[24]:


record ={'companyName':'iNeuron',
        'product':'Affordable AI',
        'courseOffered':'ML and its deployment'}
collection.insert_one(record)


# In[7]:


# record = {'companyName': 'iNeuron',
#          'product': 'Affordable AI',
#          'courseOffered': 'Deep Learning for Computer Vision'}

# collection.insert_one(record)


# In[26]:


_= checkExistence_Col(Collection_name, DB_NAME, dataBase)


# In[25]:


# _ = checkExistence_COL(COLLECTION_NAME=COLLECTION_NAME, DB_NAME=DB_NAME, db=dataBase)


# Now you can verify in Compass that iNeuron DB exists: -
# 
# > ![verify Db](mongo_img/compass/c5.JPG)
# > **NOTE**: You may need to click refresh button if your DB is not visible here.
# 
# You'll find collection name here- 
# > ![verify Collection](mongo_img/compass/c6.JPG)
# 
# Verify your inserted record with a unique id which is given by mongoDB by default -
# > ![check inserted document](mongo_img/compass/c7.JPG)
# 
# Let's reverify whether our database and collection exists or not by using the function that we have defined before.

# In[9]:


# # Verify DATABASE
# _ = checkExistence_DB(DB_NAME=DB_NAME, client=client)


# In[10]:


# # Verify COLLECTION
# _ = checkExistence_COL(COLLECTION_NAME=COLLECTION_NAME, DB_NAME=DB_NAME, db=dataBase)


# ### STEP 4: Insert multiple records
# 

# In[32]:


list_records = [
    {'companyName':'Amazon',
    'product':'Echo dot',
    'prize':4500
    },
    {
        'companyName':'Amazon',
        'product':'Alexa',
        'prize':6000
    }
]


# In[33]:


_= checkExistence_Col(Collection_name, DB_NAME, dataBase)


# In[ ]:





# In[36]:


rec = collection.insert_many(list_records)


# In[37]:


print(rec.inserted_ids)


# In[11]:



# list_of_records = [
#     {'companyName': 'iNeuron',
#      'product': 'Affordable AI',
#      'courseOffered': 'Machine Learning with Deployment'},
    
#     {'companyName': 'iNeuron',
#      'product': 'Affordable AI',
#      'courseOffered': 'Deep Learning for NLP and Computer vision'},
    
#     {'companyName': 'iNeuron',
#      'product': 'Master Program',
#      'courseOffered': 'Data Science Masters Program'}
# ]

# rec = collection.insert_many(list_of_records)


# In[12]:


# # lets print he unique ID that of the record that we have inserted -
# inserted_IDs = rec.inserted_ids

# for idx, unique_ids in enumerate(inserted_IDs):
#     print(f"{idx}. {unique_ids}")


# We can verify the inserted records by refreshing our compass document-
# 
# > ![inserted list of records](mongo_img/compass/c8.JPG)

# You can override the default unique Id by giving a user defined as shown below -
# 

# In[ ]:





# In[39]:


Coll_name = "iNeuron_Faculties"
faculites = dataBase[Coll_name]
records_into = [
    {
        "name":"Sudhanshu",
        "companyName":"iNeuron",
    }
]
rec_inserted = faculites.insert_many(records_into)


# In[40]:


print(rec_inserted.inserted_ids)


# In[44]:


find_first_record = faculites.find_one()

print(f"The first record of collection: \n{Collection_name} is=\n{find_first_record}")


# In[ ]:





# In[13]:


# COLLECTION_NAME = "iNeuron_Faculties"
# faculties = dataBase[COLLECTION_NAME]

# list_of_records_user_defined_id = [
#     {"_id": "1",
#     "companyName": "iNeuron",
#     "Faculty": "Sudhanshu Kumar"},
#     {"_id": "2",
#     "companyName": "iNeuron",
#     "Faculty": "Virat Sagar"},
# ]

# faculties_record = faculties.insert_many(list_of_records_user_defined_id)


# refresh the Compass tool and you'll see a fresh collection is created by name iNeuron_Faculties
# and this time _id is defined by us. Refer the highlighted portion of the image below:- 
#     
# > ![unique_id](mongo_img/compass/c9.JPG)
# 
# > **NOTE**: Make sure the \_id of the records that you insert are unique other wise you'll get a _BulkWriteError_ which comes because of duplicate key

# ### STEP 5: Find method in MongoDB

# In[26]:


# find_first_record = faculties.find_one()

# print(f"The first record of collection: \n{COLLECTION_NAME} is=\
# \n{find_first_record}")


# In[43]:


# find_first_record = faculites.find_one()

# print(f"The first record of collection: \n{Collection_name} is=\
# \n{find_first_record}")


# In[27]:


# # find all the record at once present in thr record with all the fields
# all_record = faculties.find()

# for idx, record in enumerate(all_record):
#     print(f"{idx}: {record}")


# In[28]:


# # find all the record at once present in the record with SPECIFIC fields
# all_record = faculties.find({}, {"Faculty"})

# for idx, record in enumerate(all_record):
#     print(f"{idx}: {record}")


# ### STEP 6: Query or filter out data in MongoDB

# In[32]:


query1 = {"_id": '1'}

results = faculties.find(query1)
for data in results:
    print(data)


# In[33]:


query2 = {"_id": {"$gt": "1"}}

results = faculties.find(query2)
for data in results:
    print(data)


# ### STEP 7: Delete one or many documents in MongoDB

# In[37]:


# Lets add some random data in faculties
random_data = [
    {'_id': '3', 'companyName': 'iNeuron', 'Faculty': 'XYZ'},
    {'_id': '4', 'companyName': 'iNeuron', 'Faculty': 'ABC'},
    {'_id': '5', 'companyName': 'iNeuron', 'Faculty': 'PQR'},
]

faculties.insert_many(random_data)


# In[38]:


# Lets delete one document in faculties
query_to_delete = {"Faculty": "XYZ"}

faculties.delete_one(query_to_delete)


# In[40]:


# lets delete multiple record
multi_query_to_delete = {"_id": {"$gte": "4"}}

faculties.delete_many(multi_query_to_delete)


# > **NOTE**: In order to delete all the documents present in the collection you can just pass and empty dictionary as shown below: -
# ```python
# faculties.delete_many({})
# ```

# ### STEP 8: Drop the entire collection

# In[45]:


faculites.drop()


# In[50]:


# Lets verify if the collection exists or not after dropping it
COLLECTION_NAME = "iNeuron_Faculties"
DB_NAME = "iNeuron"
_ = checkExistence_Col(Collection_name, DB_NAME, dataBase)


# ### STEP 9: Update

# In[47]:


COLLECTION_NAME = "iNeuron_Products"

products = dataBase[COLLECTION_NAME]

all_record = products.find()

for idx, record in enumerate(all_record):
    print(f"{record}\n")


# In[49]:


present_data = {'courseOffered': 'Machine Learning with Deployment'}
new_data = {"$set":{'courseOffered': 'ML and DL with Deployment'}}


# In[50]:


products.update_one(present_data, new_data)


# In[51]:


all_record = products.find()

for idx, record in enumerate(all_record):
    print(f"{record}\n")


# In[62]:


present_data = {'companyName': 'iNeuron'}
new_data = {"$set": {'companyName': 'iNeuron.ai'}}


# In[64]:


products.update_many(present_data, new_data)

all_record = products.find()

for idx, record in enumerate(all_record):
    print(f"{record}\n")


# ### STEP 9: Set limit to view N records

# In[66]:


N_records = 3

N_record = products.find().limit(N_records)

for idx, record in enumerate(N_record):
    print(f"{record}\n")

