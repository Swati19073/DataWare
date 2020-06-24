#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import pandas as pd
import numpy as np


# In[2]:


directory='Datasets/DW/'


# In[3]:


import time


# In[4]:


import datetime
x = datetime.datetime.now()
cur_year=x.year
print(cur_year)


# In[64]:


from datetime import datetime
cur_date=datetime.now()
cur_day=cur_date.day
cur_month=cur_date.month
drop_year=cur_year-5
try:
    connection = mysql.connector.connect(host='localhost', database='dw2',user='root',password='pragyasql')
    
    if(cur_month==12 and cur_day==31):
        queryDelete="Delete from year where year =%s"
        dataDelete=(drop_year,)
        cursor = connection.cursor()
        cursor.execute(queryDelete,dataDelete)
        connection.commit()
        
        queryDelete="Delete from fees where year =%s"
        dataDelete=(drop_year,)
        cursor = connection.cursor()
        cursor.execute(queryDelete,dataDelete)
        connection.commit()
        
        queryDelete="Delete from academics where year =%s"
        dataDelete=(drop_year,)
        cursor = connection.cursor()
        cursor.execute(queryDelete,dataDelete)
        connection.commit()
        
        queryDelete="Delete from extracurricular where year =%s"
        dataDelete=(drop_year,)
        cursor = connection.cursor()
        cursor.execute(queryDelete,dataDelete)
        connection.commit()
        
        
        queryDelete="Delete from reputation where year =%s"
        dataDelete=(drop_year,)
        cursor = connection.cursor()
        cursor.execute(queryDelete,dataDelete)
        connection.commit()
        
        queryDelete="Delete from placement_stats where year =%s"
        dataDelete=(drop_year,)
        cursor = connection.cursor()
        cursor.execute(queryDelete,dataDelete)
        connection.commit()
        
        
        queryDelete="Delete from carrer_progression where passing_year =%s"
        dataDelete=(drop_year,)
        cursor = connection.cursor()
        cursor.execute(queryDelete,dataDelete)
        connection.commit()
        
        queryDelete="Delete from placements where passing_year =%s"
        dataDelete=(drop_year,)
        cursor = connection.cursor()
        cursor.execute(queryDelete,dataDelete)
        connection.commit()
        
        queryDelete="Delete from quality_education where passing_year =%s"
        dataDelete=(drop_year,)
        cursor = connection.cursor()
        cursor.execute(queryDelete,dataDelete)
        connection.commit()
        
        
        queryDelete="Delete from student where passing_year =%s"
        dataDelete=(drop_year,)
        cursor = connection.cursor()
        cursor.execute(queryDelete,dataDelete)
        connection.commit()
        
        
except mysql.connector.Error as error:
    print("Failed to delete records {}".format(error))

finally:
    if (connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")
    
    


# In[23]:


def insert_college(resultSet):
     
    query2 ="Insert into college (college_id,college_name,college_address,college_state,time_stamp) values (%s,%s,%s,%s,%s) "
    
    querySelect1="Select college_id from college"
    cursor = connection.cursor()
    cursor.execute(querySelect1)
    recordsSelect1 = cursor.fetchall()
    cursor.close()
    prev_cid=[]
    for row in recordsSelect1:
        prev_cid.append(row[0])
    if(resultSet[0] not in prev_cid):
        cursor = connection.cursor()
        ts=time.time()
        list1=[ts]
        tuple1=tuple(list1)
        data=resultSet+tuple1
        cursor.execute(query2,data)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into College table")
        cursor.close()
    else:
        querySelect2="Select college_address,college_state from college where college_id = %s "
        valuesSelect2_list=[resultSet[0]]
        valuesSelect2=tuple(valuesSelect2_list)
        cursor = connection.cursor()
        cursor.execute(querySelect2,valuesSelect2)
        recordsSelect2 = cursor.fetchall()
        cursor.close()
        for row in recordsSelect2:
            c_add=row[0]
            c_state=row[1]
        if(c_add!=resultSet[2]):
            print("Updating address")
            queryUpdate1="Update college set college_address=%s where college_id=%s"
            valuesUpdate1_list=[resultSet[2],resultSet[0]]
            valuesUpdate1=tuple(valuesUpdate1_list)
            ts=time.time()
            valuesUpdate1=valuesUpdate1+(ts,)
            cursor = connection.cursor()
            cursor.execute(queryUpdate1,valuesUpdate1)
            connection.commit()
            cursor.close()
        if(c_state!=resultSet[3]):
            print("Updating state")
            queryUpdate2="Update college set college_state=%s where college_id=%s"
            valuesUpdate2_list=[resultSet[3],resultSet[0]]
            valuesUpdate2=tuple(valuesUpdate2_list)
            cursor = connection.cursor()
            cursor = connection.cursor()
            cursor.execute(queryUpdate2,valuesUpdate2)
            connection.commit()
            cursor.close()
            
            queryUpdate3="Update college set time_stamp=%s where college_id=%s"
            ts=time.time()
            tempData=(ts,resultSet[0])
            cursor = connection.cursor()
            cursor = connection.cursor()
            cursor.execute(queryUpdate3,tempData)
            connection.commit()
            cursor.close()
            
            
        querySelect3="Select college_name from college where college_id=%s and time_stamp=(select max(time_stamp) from college group by college_id having college_id=%s) "
        valuesSelect3_list=[resultSet[0],resultSet[0]]
        valuesSelect3=tuple(valuesSelect3_list)
        cursor = connection.cursor()
        cursor.execute(querySelect3,valuesSelect3)
        recordsSelect3 = cursor.fetchall()
        cursor.close()
        for row in recordsSelect3:
            c_name=row[0]
        if(c_name!=resultSet[1]):
            cursor = connection.cursor()
            ts=time.time()
            list1=[ts]
            tuple1=tuple(list1)
            data=resultSet+tuple1
            cursor.execute(query2,data)
            connection.commit()
            print(cursor.rowcount, "Record inserted successfully into College table")
            cursor.close()
  


# In[26]:


try:
    connection = mysql.connector.connect(host='localhost', database='dw2',user='root',password='pragyasql')
    
   

    #     dataInsert=('c_1','Thapar Univeristy','Patiala','Punjab')
#     insert_college(dataInsert)

    
    path=directory+'colleges.csv'
    df_colleges=pd.read_csv(path)
    print(df_colleges.shape)
    results=[]

    for i in range(df_colleges.shape[0]):
        temp=()
        null_count=0
        for j in range(df_colleges.shape[1]):
        
            val=df_colleges.iloc[i,j]
            print(val)
            if(j==0 and pd.isnull(val)):
                break
            if(j==1 and pd.isnull(val)):
                null_count+=1
                querySelect3="Select college_name from college where college_id=%s and time_stamp=(select max(time_stamp) from college group by college_id having college_id=%s) "
                valuesSelect3_list=[df_colleges.iloc[i,0],df_colleges.iloc[i,0]]
                valuesSelect3=tuple(valuesSelect3_list)
                cursor = connection.cursor()
                cursor.execute(querySelect3,valuesSelect3)
                recordsSelect3 = cursor.fetchall()
                n=cursor.count()
                cursor.close()
                for row in recordsSelect3:
                    c_name=row[0]
               
                if(n>0):
                    temp=temp+(c_name,)
                else:
                    val=None
                    temp=temp+(val,)
            if(j==2 and pd.isnull(val)):
                null_count+=1
                querySelect4="Select DISTINCT college_address from college where college_id=%s"
                valuesSelect4_list=[df_colleges.iloc[i,0]]
                valuesSelect4=tuple(valuesSelect4_list)
                cursor = connection.cursor()
                cursor.execute(querySelect4,valuesSelect4)
                recordsSelect4 = cursor.fetchall()
                n=cursor.rowcount
                cursor.close()
                for row in recordsSelect4:
                    c_add=row[0]
                    
                if(n>0):
                    temp=temp+(c_add,)
                else:
                    val=None
                    temp=temp+(val,)
            if(j==3 and pd.isnull(val)):
                null_count+=1
                querySelect5="Select DISTINCT college_state from college where college_id=%s"
                valuesSelect5_list=[df_colleges.iloc[i,0]]
                valuesSelect5=tuple(valuesSelect5_list)
                cursor = connection.cursor()
                cursor.execute(querySelect5,valuesSelect5)
                recordsSelect5 = cursor.fetchall()
                n=cursor.count()
                cursor.close()
                for row in recordsSelect5:
                    c_state=row[0]
                if(n>0):
                    temp=temp+(c_state,)
                else:
                    val=None
                    temp=temp+(val,)
            
            if(null_count==3):
                break
            if(pd.notnull(val)):
                temp=temp+(val,)
        print(temp)
       
        if(len(temp)>0):
            results.append(temp)
    print(results)
    for i in range(len(results)):
        insert_college(results[i])
                
                
        
except mysql.connector.Error as error:
    print("Failed to insert record into College table {}".format(error))

finally:
    if (connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")


# In[37]:


def insert_branch(resultSet):
     
    query2 ="Insert into branch (branch_id,branch_name,time_stamp) values (%s,%s,%s) "
    
    querySelect1="Select branch_id from branch"
    cursor = connection.cursor()
    cursor.execute(querySelect1)
    recordsSelect1 = cursor.fetchall()
    cursor.close()
    prev_bid=[]
    for row in recordsSelect1:
        prev_bid.append(row[0])
    if(resultSet[0] not in prev_bid):
        cursor = connection.cursor()
        ts=time.time()
        list1=[ts]
        tuple1=tuple(list1)
        data=resultSet+tuple1
        cursor.execute(query2,data)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into Branch table")
        cursor.close()
    else:
        querySelect2="Select branch_name from branch where branch_id = %s "
        valuesSelect2_list=[resultSet[0]]
        valuesSelect2=tuple(valuesSelect2_list)
        cursor = connection.cursor()
        cursor.execute(querySelect2,valuesSelect2)
        recordsSelect2 = cursor.fetchall()
        cursor.close()
        for row in recordsSelect2:
            b_name=row[0]
            
        if(b_name!=resultSet[1]):
            print("Updating branch name")
            queryUpdate1="Update branch set branch_name=%s where branch_id=%s"
            
            
            temp_tuple=tuple([resultSet[1],resultSet[0]])
           
            cursor = connection.cursor()
            cursor.execute(queryUpdate1,temp_tuple)
            connection.commit()
            cursor.close()
            
            queryUpdate2="Update branch set time_stamp=%s where branch_id=%s"
            
            ts=time.time()
            temp_tuple=tuple([ts,resultSet[0]])
           
            cursor = connection.cursor()
            cursor.execute(queryUpdate2,temp_tuple)
            connection.commit()
            cursor.close()
            
            
       
  


# In[38]:


try:
    connection = mysql.connector.connect(host='localhost', database='dw2',user='root',password='pragyasql')
    
   

    dataInsert=('b_1','Computer Engineering')
    insert_branch(dataInsert)

    
    path=directory+'branches.csv'
    df_branches=pd.read_csv(path)
    print(df_branches.shape)
    results=[]

    for i in range(df_branches.shape[0]):
        temp=()
        null_count=0
        for j in range(df_branches.shape[1]):
        
            val=df_branches.iloc[i,j]
            print(val)
            if(j==0 and pd.isnull(val)):
                null_count+=1
                break
            if(j==1 and pd.isnull(val)):
                null_count+=1
                break
            if(pd.notnull(val)):
                temp=temp+(val,)
        print(temp)
       
        if(len(temp)>0 and null_count==0):
            results.append(temp)
    print(results)
    for i in range(len(results)):
        insert_branch(results[i])
                
                
        
except mysql.connector.Error as error:
    print("Failed to insert record into Branch table {}".format(error))

finally:
    if (connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")


# In[8]:





# In[9]:


def insert_year(resultSet):
     
    query2 ="Insert into year (year) values (%s) "
    
    querySelect1="Select year from year"
    cursor = connection.cursor()
    cursor.execute(querySelect1)
    recordsSelect1 = cursor.fetchall()
    cursor.close()
    prev_years=[]
    for row in recordsSelect1:
        prev_years.append(row[0])
    
        
    if(resultSet[0] not in prev_years and type(resultSet[0]!=type("abc")) and int(resultSet[0])<cur_year and int(resultSet[0])>=cur_year-6 ):
        cursor = connection.cursor()
       
        data=tuple([int(resultSet[0])])
        cursor.execute(query2,data)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into year table")
        cursor.close()
  
  


# In[10]:


try:
    connection = mysql.connector.connect(host='localhost', database='dw2',user='root',password='pragyasql')
    
   

     #dataInsert=tuple([2015])
#     insert_year(dataInsert)

    
    path=directory+'years.csv'
    df_years=pd.read_csv(path)
    print(df_years.shape)
    results=[]

    for i in range(df_years.shape[0]):
        
        new_df=pd.to_numeric(df_years.iloc[:,0],errors='coerce')
        
        val=new_df.iloc[i]
        if(pd.isnull(val)):
            break
        else:
            temp_list=[val]
            data=tuple(temp_list)
            results.append(temp_list)
    print(results)
    for i in range(len(results)):
        insert_year(results[i])
                
                
        
except mysql.connector.Error as error:
    print("Failed to insert record into year table {}".format(error))

finally:
    if (connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")


# In[11]:


def insert_fee(resultSet):
    query2 ="Insert into fees (college_id,year,tuition_fee,hostel_fee,mess_fee,security_fee,other)values (%s,%s,%s,%s,%s,%s,%s) "
    
    querySelect1="Select college_id from college"
    cursor = connection.cursor()
    cursor.execute(querySelect1)
    recordsSelect1 = cursor.fetchall()
    cursor.close()
    valid_cid=[]
    
    for row in recordsSelect1:
        valid_cid.append(row[0])
    if(resultSet[0] not in valid_cid):
        print("Not a valid college id. Enter college first.")
        return
        
    querySelect2="Select year from year"
    cursor = connection.cursor()
    cursor.execute(querySelect2)
    recordsSelect2 = cursor.fetchall()
    cursor.close()
    valid_years=[]
    for row in recordsSelect2:
        valid_years.append(row[0])
    y=int(resultSet[1])
    if(y>=cur_year or y<=cur_year-6 ):
        print("Not a valid year")
        return
    elif (int(resultSet[1]) not in valid_years):
        print("Enter year first")
        return
    
    else:
        columns=['tuition_fee','hostel_fee','mess_fee','security_fee','other']
        for j in range(7):
            if(j>1 and resultSet[j]==0):
                querySelect2="Select "+columns[j-2]+" from fees where college_id=%s and year=(Select max(year) from fees where year < %s group by college_id having college_id =%s)"
                valuesSelect2=(resultSet[0],resultSet[1],resultSet[0])
                cursor = connection.cursor()
                cursor.execute(querySelect2,valuesSelect2)
                recordsSelect2 = cursor.fetchall()
                for row in recordsSelect2:
                    missing_val=row[0]
                if(cursor.rowcount!=0):
                    resultSet_list=list(resultSet)
                    resultSet_list[j]=missing_val
                    resultSet=tuple(resultSet_list)
                cursor.close()
        
        querySelect="Select tuition_fee,hostel_fee,mess_fee,security_fee,other from fees where college_id=%s and year=%s"
        selectTuple=(resultSet[0],resultSet[1])
        cursor = connection.cursor()
        cursor.execute(querySelect,selectTuple)
        records_fees = cursor.fetchall()
        flags=[]
        count_fees=-1
        count_fees=cursor.rowcount
            
        for row in records_fees:
            
            tuition=row[0]
            hostel=row[1]
            mess=row[2]
            security=row[3]
            other=row[4]
#             print(tuition)
#             print(resultSet[3])
#             print(hostel)
#             print(resultSet[4])
#             print(mess)
#             print(resultSet[5])
#             print(other)
#             print(resultSet[6])
            if(tuition !=resultSet[2] or hostel!=resultSet[3] or mess!=resultSet[4] or security!=resultSet[5] or other!=resultSet[6]):
                cur_flag=1
                    
            else:
                cur_flag=0
            flags.append(cur_flag)   
                    
        cursor.close()
        #print(count_fees)   
        #print(flags)
        if(0 in flags and count_fees!=-1):
            print("duplicate record") #all values are same
            return
        else: #HANDLE THIS 
            if(count_fees!=-1):
                print("Duplicate dimensions found")
                option=int(input("Enter 1 to retain this version and 2 to drop"))
                if(option==1):
                    print("Updating entry")
                    queryUpdate1="Update fees set tuition_fee= %s where college_id =%s and year=%s"
                    dataUpdate1=(resultSet[2],resultSet[0],resultSet[1])
                    cursor = connection.cursor()
                    cursor.execute(queryUpdate1,dataUpdate1)
                    connection.commit()
                    cursor.close()
                    
                    queryUpdate2="Update fees set hostel_fee=%s where college_id =%s and year=%s"
                    dataUpdate2=(resultSet[3],resultSet[0],resultSet[1])
                    cursor = connection.cursor()
                    cursor.execute(queryUpdate2,dataUpdate2)
                    connection.commit()
                    cursor.close()
                    
                    queryUpdate3="Update fees set mess_fee=%s where college_id =%s and year=%s"
                    dataUpdate3=(resultSet[4],resultSet[0],resultSet[1])
                    cursor = connection.cursor()
                    cursor.execute(queryUpdate3,dataUpdate3)
                    connection.commit()
                    cursor.close()
                    
                    queryUpdate4="Update fees set security_fee=%s where college_id =%s and year=%s"
                    dataUpdate4=(resultSet[5],resultSet[0],resultSet[1])
                    cursor = connection.cursor()
                    cursor.execute(queryUpdate4,dataUpdate4)
                    connection.commit()
                    cursor.close()
                    
                    queryUpdate5="Update fees set other=%s where college_id =%s and year=%s"
                    dataUpdate5=(resultSet[6],resultSet[0],resultSet[1])
                    cursor = connection.cursor()
                    cursor.execute(queryUpdate5,dataUpdate5)
                    connection.commit()
                    cursor.close()
                    return
                    
                    
                    
                    
                else:
                    return
            else:
                cursor = connection.cursor()
                cursor.execute(query2,resultSet)
                connection.commit()
                print(cursor.rowcount, "Record inserted successfully into fees table")
                cursor.close()
                return
        
        
    


# In[12]:


try:
    connection = mysql.connector.connect(host='localhost', database='dw2',user='root',password='pragyasql')
    
   

    dataInsert=('c_3',2017,35,45000,25000,10000,8000)
    insert_fee(dataInsert)

    
    path=directory+'fees.csv'
    df_fees=pd.read_csv(path)
    print(df_fees.shape)
    results=[]
  
            
    
    
    for i in range(df_fees.shape[0]):
        
        temp=()
        null_count=0
        for j in range(df_fees.shape[1]):
            
            if(j>0):
                val=pd.to_numeric(df_fees.iloc[i,j],errors='coerce')
            else:
                val=df_fees.iloc[i,j]
            
            
            
            if((j==0 or j==1) and pd.isnull(val)):
               
                break
            elif(pd.isnull(val) and j>1):
                null_count+=1
                val=0
               
            if(j!=0 and pd.notnull(val)):
                val=int(val)
                
            temp=temp+(val,)
        if(len(temp)==7 and null_count<5):
            results.append(temp)
    print(results)
    for i in range(len(results)):
        insert_fee(results[i])
            
           
                
                
        
except mysql.connector.Error as error:
    print("Failed to insert record into fees table {}".format(error))

finally:
    if (connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")


# In[13]:


def insert_academics(resultSet):
    query2 ="Insert into academics (college_id,year,branch_id,seats,faculty,cutoff)values (%s,%s,%s,%s,%s,%s) "
    
    querySelect1="Select college_id from college"
    cursor = connection.cursor()
    cursor.execute(querySelect1)
    recordsSelect1 = cursor.fetchall()
    cursor.close()
    valid_cid=[]
    
    for row in recordsSelect1:
        valid_cid.append(row[0])
    if(resultSet[0] not in valid_cid):
        print("Not a valid college id. Enter college first.")
        return
        
    querySelect2="Select year from year"
    cursor = connection.cursor()
    cursor.execute(querySelect2)
    recordsSelect2 = cursor.fetchall()
    cursor.close()
    valid_years=[]
    for row in recordsSelect2:
        valid_years.append(row[0])
    y=int(resultSet[1])
    if(y>=cur_year or y<=cur_year-6 ):
        print("Not a valid year")
        return
    elif (int(resultSet[1]) not in valid_years):
        print("Enter year first")
        return
    
    else:
        querySelect2="Select branch_id from branch"
        cursor = connection.cursor()
        cursor.execute(querySelect2)
        recordsSelect2 = cursor.fetchall()
        cursor.close()
        valid_bid=[]
    
        for row in recordsSelect2:
            valid_bid.append(row[0])
        if(resultSet[2] not in valid_bid):
            print("Not a valid branch id. Enter branch first.")
            return
  
        columns=['seats','faculty','cutoff']
        for j in range(3,6):
            print(j)
            if(resultSet[j]==-1):
                querySelect2="Select "+columns[j-3]+" from academics where college_id=%s and branch_id =%s and year=(Select max(year) from academics where year < %s group by college_id having college_id =%s)"
                valuesSelect2=(resultSet[0],resultSet[2],resultSet[1],resultSet[0])
                cursor = connection.cursor()
                cursor.execute(querySelect2,valuesSelect2)
                recordsSelect2 = cursor.fetchall()
                for row in recordsSelect2:
                    missing_val=row[0]
                if(cursor.rowcount!=0):
                    resultSet_list=list(resultSet)
                    resultSet_list[j]=missing_val
                    resultSet=tuple(resultSet_list)
                cursor.close()
        
        querySelect="Select seats,faculty,cutoff from academics where college_id=%s and branch_id=%s and year=%s"
        selectTuple=(resultSet[0],resultSet[2],int(resultSet[1]))
        cursor = connection.cursor()
        cursor.execute(querySelect,selectTuple)
        records_academics = cursor.fetchall()
        flags=[]
        count_records=-1
        count_records=cursor.rowcount
            
        for row in records_academics:
            
            seats=row[0]
            faculty=row[1]
            cutoff=row[2]
#             print(tuition)
#             print(resultSet[3])
#             print(hostel)
#             print(resultSet[4])
#             print(mess)
#             print(resultSet[5])
#             print(other)
#             print(resultSet[6])
            if(seats !=resultSet[3] or faculty!=resultSet[4] or cutoff!=resultSet[5] ):
                cur_flag=1
                    
            else:
                cur_flag=0
            flags.append(cur_flag)   
                    
        cursor.close()
        #print(count_fees)   
        #print(flags)
        if(0 in flags and count_records!=-1):
            print("duplicate")
            return
        else:
            if(count_records>0):
                print("Duplicate dimensions found")
                option=int(input("Enter 1 to retain this version and 2 to drop"))
                if(option==1):
                    print("Updating entry")
                    queryUpdate1="Update academics set seats= %s where college_id =%s and year=%s and branch_id=%s"
                    dataUpdate1=(resultSet[3],resultSet[0],resultSet[1],resultSet[2])
                    cursor = connection.cursor()
                    cursor.execute(queryUpdate1,dataUpdate1)
                    connection.commit()
                    cursor.close()
                    
                    queryUpdate2="Update academics set faculty=%s where college_id =%s and year=%s and branch_id=%s"
                    dataUpdate2=(resultSet[4],resultSet[0],resultSet[1],resultSet[2])
                    cursor = connection.cursor()
                    cursor.execute(queryUpdate2,dataUpdate2)
                    connection.commit()
                    cursor.close()
                    
                    queryUpdate3="Update academics set cutoff=%s where college_id =%s and year=%s and branch_id=%s"
                    dataUpdate3=(resultSet[5],resultSet[0],resultSet[1],resultSet[2])
                    cursor = connection.cursor()
                    cursor.execute(queryUpdate3,dataUpdate3)
                    connection.commit()
                    cursor.close()
                    
                    
                    
                    
                    
                    
                else:
                    return
            else:
                cursor = connection.cursor()
                cursor.execute(query2,resultSet)
                connection.commit()
                print(cursor.rowcount, "Record inserted successfully into academics table")
                cursor.close()
                return
        
    


# In[14]:


try:
    connection = mysql.connector.connect(host='localhost', database='dw2',user='root',password='pragyasql')
    
   

    dataInsert=('c_1', 2019, 'b_1', -1, 53.0, 9500.0)
    insert_academics(dataInsert)

    
    path=directory+'academics.csv'
    df_academics=pd.read_csv(path)
    print(df_academics.shape)
    results=[]
  
            
    
    
    for i in range(df_academics.shape[0]):
        
        temp=()
        null_count=0
        for j in range(df_academics.shape[1]):
            
            if(j>2):
                val=pd.to_numeric(df_academics.iloc[i,j],errors='coerce')
            elif (j==1):
                val=int(df_academics.iloc[i,j])
            
            else:
                val=df_academics.iloc[i,j]
            
            
            
            if((j==0 or j==1 or j==2) and pd.isnull(val)):
               
                break
            elif(pd.isnull(val) and (j==3 or j==4)):
                null_count+=1
                val=-1
            elif(pd.isnull(val) and j==5):
                null_count+=1
                val=0
               
            
                
            temp=temp+(val,)
        if(len(temp)==6 and null_count<3):
            results.append(temp)
    print(results)
    for i in range(len(results)):
        insert_academics(results[i])
            
           
                
                
        
except mysql.connector.Error as error:
    print("Failed to insert record into academics table {}".format(error))

finally:
    if (connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")


# In[74]:


def insert_extra(resultSet):
    query2 ="Insert into extracurricular (college_id,year,clubs,societis,fests,sports,audi)values (%s,%s,%s,%s,%s,%s,%s) "
    
    querySelect1="Select college_id from college"
    cursor = connection.cursor()
    cursor.execute(querySelect1)
    recordsSelect1 = cursor.fetchall()
    cursor.close()
    valid_cid=[]
    
    for row in recordsSelect1:
        valid_cid.append(row[0])
    if(resultSet[0] not in valid_cid):
        print("Not a valid college id. Enter college first.")
        return
        
    querySelect2="Select year from year"
    cursor = connection.cursor()
    cursor.execute(querySelect2)
    recordsSelect2 = cursor.fetchall()
    cursor.close()
    valid_years=[]
    for row in recordsSelect2:
        valid_years.append(row[0])
    y=int(resultSet[1])
    if(y>=cur_year or y<=cur_year-6 ):
        print("Not a valid year")
        return
    elif (int(resultSet[1]) not in valid_years):
        print("Enter year first")
        return
    
    else:
        
        columns=['clubs','societis','fests','sports','audi']
        for j in range(2,7):
            
            if(resultSet[j]==-1):
                querySelect2="Select "+columns[j-2]+" from extracurricular where college_id=%s and year=(Select max(year) from extracurricular where year < %s group by college_id having college_id =%s)"
                valuesSelect2=(resultSet[0],resultSet[1],resultSet[0])
                cursor = connection.cursor()
                cursor.execute(querySelect2,valuesSelect2)
                recordsSelect2 = cursor.fetchall()
                for row in recordsSelect2:
                    missing_val=row[0]
                if(cursor.rowcount!=0):
                    resultSet_list=list(resultSet)
                    resultSet_list[j]=missing_val
                    resultSet=tuple(resultSet_list)
                cursor.close()
        
        querySelect="Select clubs,societis,fests,sports,audi from extracurricular where college_id=%s and year=%s"
        selectTuple=(resultSet[0],int(resultSet[1]))
        cursor = connection.cursor()
        cursor.execute(querySelect,selectTuple)
        records_academics = cursor.fetchall()
        flags=[]
        count_records=-1
        count_records=cursor.rowcount
            
        for row in records_academics:
            
            
            clubs=row[0]
            society=row[1]
            fests=row[2]
            sports=row[3]
            audi=row[4]
#             print(tuition)
#             print(resultSet[3])
#             print(hostel)
#             print(resultSet[4])
#             print(mess)
#             print(resultSet[5])
#             print(other)
#             print(resultSet[6])
            if(clubs !=resultSet[2] or society!=resultSet[3] or fests!=resultSet[4] or sports!=resultSet[5] or audi!=resultSet[6] ):
                cur_flag=1
                    
            else:
                cur_flag=0
            flags.append(cur_flag)   
                    
        cursor.close()
        #print(count_fees)   
        #print(flags)
        if(0 in flags and count_records!=-1):
            print("duplicate")
            return
        else:
            if(count_records>0):
                print("Duplicate dimensions found")
                option=int(input("Enter 1 to retain this version and 2 to drop"))
                if(option==1):
                    print("Updating entry")
                    queryUpdate1="Update extracurricular set clubs= %s where college_id =%s and year=%s "
                    dataUpdate1=(resultSet[2],resultSet[0],resultSet[1])
                    cursor = connection.cursor()
                    cursor.execute(queryUpdate1,dataUpdate1)
                    connection.commit()
                    cursor.close()
                    
                    queryUpdate2="Update extracurricular set societis= %s where college_id =%s and year=%s "
                    dataUpdate2=(resultSet[3],resultSet[0],resultSet[1])
                    cursor = connection.cursor()
                    cursor.execute(queryUpdate2,dataUpdate2)
                    connection.commit()
                    cursor.close()
                    
                    queryUpdate3="Update extracurricular set fests= %s where college_id =%s and year=%s "
                    dataUpdate3=(resultSet[4],resultSet[0],resultSet[1])
                    cursor = connection.cursor()
                    cursor.execute(queryUpdate3,dataUpdate3)
                    connection.commit()
                    cursor.close()
                    
                    queryUpdate4="Update extracurricular set sports= %s where college_id =%s and year=%s "
                    dataUpdate4=(resultSet[5],resultSet[0],resultSet[1])
                    cursor = connection.cursor()
                    cursor.execute(queryUpdate4,dataUpdate4)
                    connection.commit()
                    cursor.close()
                    
                    queryUpdate5="Update extracurricular set audi= %s where college_id =%s and year=%s "
                    dataUpdate5=(resultSet[6],resultSet[0],resultSet[1])
                    cursor = connection.cursor()
                    cursor.execute(queryUpdate5,dataUpdate5)
                    connection.commit()
                    cursor.close()
                    
                    
                    
                    
                    
                    
                else:
                    return
            else:
                cursor = connection.cursor()
                cursor.execute(query2,resultSet)
                connection.commit()
                print(cursor.rowcount, "Record inserted successfully into extracurricular table")
                cursor.close()
                return
        
    


# In[78]:


try:
    connection = mysql.connector.connect(host='localhost', database='dw2',user='root',password='pragyasql')
    
   

    dataInsert=('c_2',2017,-1,26,-1,1,1)
    insert_extra(dataInsert)

    
    path=directory+'extra.csv'
    df_extra=pd.read_csv(path)
    print(df_extra.shape)
    results=[]
  
            
    
    
    for i in range(df_extra.shape[0]):
        
        temp=()
        null_count=0
        for j in range(df_extra.shape[1]):
            
            if(j>0):
                val=pd.to_numeric(df_extra.iloc[i,j],errors='coerce')
            else:
                val=df_extra.iloc[i,j]
            
            
            
            if((j==0 or j==1) and pd.isnull(val)):
               
                break
            elif(pd.isnull(val) and j>1):
                null_count+=1
                val=-1
               
            if(j!=0 and pd.notnull(val)):
                val=int(val)
                
            temp=temp+(val,)
        if(len(temp)==7 and null_count<5):
            results.append(temp)
    print(results)
    for i in range(len(results)):
        insert_extra(results[i])
            
           
                
                
        
except mysql.connector.Error as error:
    print("Failed to insert record into extracurricular table {}".format(error))

finally:
    if (connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")


# In[15]:


def insert_rating(resultSet):
    query2 ="Insert into reputation (college_id,year,rating)values (%s,%s,%s) "
    
    querySelect1="Select college_id from college"
    cursor = connection.cursor()
    cursor.execute(querySelect1)
    recordsSelect1 = cursor.fetchall()
    cursor.close()
    valid_cid=[]
    
    for row in recordsSelect1:
        valid_cid.append(row[0])
    if(resultSet[0] not in valid_cid):
        print("Not a valid college id. Enter college first.")
        return
        
    querySelect2="Select year from year"
    cursor = connection.cursor()
    cursor.execute(querySelect2)
    recordsSelect2 = cursor.fetchall()
    cursor.close()
    valid_years=[]
    for row in recordsSelect2:
        valid_years.append(row[0])
    y=int(resultSet[1])
    if(y>=cur_year or y<=cur_year-6 ):
        print("Not a valid year")
        return
    elif (int(resultSet[1]) not in valid_years):
        print("Enter year first")
        return
    
    else:
        if(resultSet[2]==-1):
            querySelect2="Select rating from reputation where college_id=%s and year=(Select max(year) from reputation where year < %s group by college_id having college_id =%s)"
            valuesSelect2=(resultSet[0],resultSet[1],resultSet[0])
            cursor = connection.cursor()
            cursor.execute(querySelect2,valuesSelect2)
            recordsSelect2 = cursor.fetchall()
            for row in recordsSelect2:
                missing_val=row[0]
            if(cursor.rowcount!=0):
                resultSet_list=list(resultSet)
                resultSet_list[2]=missing_val
                resultSet=tuple(resultSet_list)
            cursor.close()
        
        querySelect="Select rating from reputation where college_id=%s and year=%s"
        selectTuple=(resultSet[0],int(resultSet[1]))
        cursor = connection.cursor()
        cursor.execute(querySelect,selectTuple)
        records_rating = cursor.fetchall()
        
        count_records=-1
        count_records=cursor.rowcount
        cur_flag=-1    
        for row in records_rating:
            
            rating=row[0]
            if(rating !=resultSet[2] ):
                cur_flag=1
                    
            else:
                cur_flag=0
            
        if(cur_flag==0 and count_records==1):
            print("duplicate")
            return
        else:
            if(count_records>0):
                print("Duplicate dimensions found")
                option=int(input("Enter 1 to retain this version and 2 to drop"))
                if(option==1):
                    print("Updating entry")
                    queryUpdate1="Update reputatin set rating= %s where college_id =%s and year=%s"
                    dataUpdate1=(resultSet[2],resultSet[0],resultSet[1])
                    cursor = connection.cursor()
                    cursor.execute(queryUpdate1,dataUpdate1)
                    connection.commit()
                    cursor.close()
                    
                  
                else:
                    return
            else:
                if(resultSet[2]!=-1):
                    cursor = connection.cursor()
                    cursor.execute(query2,resultSet)
                    connection.commit()
                    print(cursor.rowcount, "Record inserted successfully into reputation table")
                    cursor.close()
                    return
                else:
                    print("rating missing")
        
    


# In[39]:


try:
    connection = mysql.connector.connect(host='localhost', database='dw2',user='root',password='pragyasql')
    
   

    #dataInsert=('c_1', 2019, 4)
    #insert_rating(dataInsert)

    
    path=directory+'reputation.csv'
    df_reputation=pd.read_csv(path)
    print(df_reputation.shape)
    results=[]
    for i in range(df_reputation.shape[0]):
        
        temp=()
        
        for j in range(df_reputation.shape[1]):
            
            if(j==1 or j==2):
                val=pd.to_numeric(df_reputation.iloc[i,j])
                if (j==1 and pd.notnull(val)):
                    val=int(val)
            
            else:
                val=df_reputation.iloc[i,j]
            
            
            
            if((j==0 or j==1 ) and pd.isnull(val)):
               
                break
            elif(j==2 and (val >5  or val<5)):
                break
                
            elif(pd.isnull(val)):
                
                val=-1
            temp=temp+(val,)
        if(len(temp)==3):
            results.append(temp)
    print(results)
    for i in range(len(results)):
        insert_rating(results[i])
            
           
                
                
        
except mysql.connector.Error as error:
    print("Failed to insert record into reputation table {}".format(error))

finally:
    if (connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")


# In[39]:


def insert_students(values):
    query_ins= "insert into student (roll_number, college_id, passing_year, student_name, degree,time_stamp) values(%s,%s,%s,%s,%s,%s)"
    clg_ids=[]
    ans=[]
    query="select college_id from college"
    cursor=connection.cursor()
    cursor.execute(query)
    records=cursor.fetchall()
    for row in records:
        clg_ids.append(row[0])
    
    roll_no=[]
    query1="select roll_number from student"
    cursor1=connection.cursor()
    cursor1.execute(query1)
    records1=cursor1.fetchall()
#     print(clg_ids)
    for row in records1:
        roll_no.append(row[0])
    if values[0] not in roll_no:
        if values[1] in clg_ids:
            if (cur_year-int(values[2])<=5 and cur_year-int(values[2])>=1):
                cursor = connection.cursor()
                ts=time.time()
                list1=[ts]
                tuple1=tuple(list1)
                data=values+tuple1
                cursor.execute(query_ins,data)
                 
                connection.commit()
                print(cursor.rowcount, "Record inserted successfully into students table")
                cursor.close()
            else:
                print("Enter the value of year for last five years")
    else:
        if values[1] in clg_ids:
            if (cur_year-int(values[2])<=5 and cur_year-int(values[2])>=1):
                querySelect2="Select passing_year,student_name, degree from student where roll_number = %s and college_id = %s"
                valuesSelect2_list=[values[0],values[1]]
                valuesSelect2=tuple(valuesSelect2_list)
                cursor = connection.cursor()
                cursor.execute(querySelect2,valuesSelect2)
                records2 = cursor.fetchall()
                cursor.close()
                s_py=''
                s_sn=''
                s_deg=''
                for r in records2:
                    s_py=int(r[0])
                    print(s_py)
                    s_sn=r[1]
                    s_deg=r[2]
                if s_py!=values[2]:
                    print("Updating passing year")
                    queryUpdate1="Update student set passing_year = %s where roll_number = %s and college_id = %s"
                    valuesUpdate1_list=[int(values[2]),values[0],values[1]]
                    valuesUpdate1=tuple(valuesUpdate1_list)
                   
                    cursor = connection.cursor()
                    cursor.execute(queryUpdate1,valuesUpdate1)
                   
                    connection.commit()
                    cursor.close()
                    
                    queryUpdate4="Update student set time_stamp=%s where roll_number = %s and college_id = %s"
                    ts=time.time()
                    tempData=(ts,values[0],values[1])
                    cursor = connection.cursor()
                    cursor = connection.cursor()
                    cursor.execute(queryUpdate4,tempData)
                    connection.commit()
                    cursor.close()
                    
                    
                    
                    
                if(s_sn!=values[3]):
                    print("Updating name")
                    queryUpdate2="Update student set student_name = %s where roll_number = %s and college_id = %s"
                    valuesUpdate2_list=[values[3],values[0],values[1]]
                    valuesUpdate2=tuple(valuesUpdate2_list)
                   
                    cursor = connection.cursor()
                    cursor = connection.cursor()
                    cursor.execute(queryUpdate2,valuesUpdate2)
                    connection.commit()
                    cursor.close()
                    
                    
                    queryUpdate4="Update student set time_stamp=%s where roll_number = %s and college_id = %s"
                    ts=time.time()
                    tempData=(ts,values[0],values[1])
                    cursor = connection.cursor()
                    cursor = connection.cursor()
                    cursor.execute(queryUpdate4,tempData)
                    connection.commit()
                    cursor.close()
                if(s_deg!=values[4]):
                    print("Updating degree")
                    queryUpdate3="Update student set degree = %s where roll_number = %s and college_id = %s"
                    valuesUpdate3_list=[values[4],values[0],values[1]]
                    valuesUpdate3=tuple(valuesUpdate3_list)
                    
                    cursor = connection.cursor()
                    cursor = connection.cursor()
                    cursor.execute(queryUpdate3,valuesUpdate3)
                    connection.commit()
                    cursor.close()
                    
                    queryUpdate4="Update student set time_stamp=%s where roll_number = %s and college_id = %s"
                    ts=time.time()
                    tempData=(ts,values[0],values[1])
                    cursor = connection.cursor()
                    cursor = connection.cursor()
                    cursor.execute(queryUpdate4,tempData)
                    connection.commit()
                    cursor.close()
                    
    


# In[19]:


try:
    connection = mysql.connector.connect(host='localhost', database='dw2',user='root',password='pragyasql')
    
   

    dataInsert=('101411028','c_3', 2018 ,'Pragya','Btech')
    insert_students(dataInsert)
    
    
except mysql.connector.Error as error:
    print("Failed to insert record into student table {}".format(error))

finally:
    if (connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")


# In[20]:


def insert_placements(results):
    query_ins="insert into placements(roll_number, college_id, passing_year,company_name,profile, package) values(%s,%s,%s,%s,%s,%s)"
    query="select roll_number,college_id,passing_year from student";
    cursor=connection.cursor()
    cursor.execute(query)
    records=cursor.fetchall()
    list_of_tuples=[]
    for row in records:
        list_of_tuples.append(row)
        
        
    query1="select roll_number,college_id,passing_year,company_name, profile, package from placements";
    cursor=connection.cursor()
    cursor.execute(query1)
    records1=cursor.fetchall()
    list_of_all_tuples=[]
    for row in records1:
        list_of_all_tuples.append(row)
    if pd.isnull(results[3]) and pd.isnull(results[4]) and pd.isnull(results[5]):
        print("Cannot insert all the null values")
    elif pd.isnull(results[2]):
        print("Year cannot be null")
    elif results in list_of_all_tuples:
        print("Duplicate rows")
    else:
        tup=(results[0],results[1],results[2])
        if tup in list_of_tuples:
            ans=int(input("Enter 1 to update the row or 0 to drop the row : "))
            if ans ==1:
                queryDel="Delete from placements where roll_number=%s and college_id= %s and passing_year= %s"
                cursor1=connection.cursor()
                cursor1.execute(queryDel,tup)
                print(cursor1.rowcount, "Record deleted successfully from Placements table")
                cursor1.close()
                cursor = connection.cursor()
                cursor.execute(query_ins,results)
                connection.commit()
                print(cursor.rowcount, "Record inserted successfully into Placements table")
                cursor.close()
            else:
                print("New record is ignored")
                
        else:
            print("Cannot enter data because of foreign key constraints")
            

            
        
        
        
        


# In[27]:



try:
    connection = mysql.connector.connect(host='localhost', database='dw2',user='root',password='pragyasql')
    
   

    dataInsert=('MT19070','c1',2018,"Google","SDE",30)
    insert_placements(dataInsert)
    
except mysql.connector.Error as error:
    print("Failed to insert record into placements table {}".format(error))

finally:
    if (connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")


# In[28]:


def insert_quality_edu(results):
    query_ins="insert into quality_education(roll_number, college_id, passing_year,satisfaction) values(%s,%s,%s,%s)"
    query="select roll_number,college_id,passing_year from student";
    cursor=connection.cursor()
    cursor.execute(query)
    records=cursor.fetchall()
    list_of_tuples=[]
    for row in records:
        list_of_tuples.append(row)
        
    query1="select roll_number,college_id,passing_year, satisfaction from quality_education";
    cursor=connection.cursor()
    cursor.execute(query1)
    records1=cursor.fetchall()
    list_of_all_tuples=[]
    for row in records1:
        list_of_all_tuples.append(row)
    if pd.isnull(results[2]):
        print("Year cannot be null")
    elif pd.isnull(results[3]):
        print("Cannot insert all the null values")
    elif(results[3]>5 or results[3]<1):
        print("Enter the satisfaction in range of 1 to 5")
    elif results in list_of_all_tuples:
        print("Duplicate rows")
    else:
        tup=(results[0],results[1],results[2])
        if tup in list_of_tuples:
            ans=int(input("Enter 1 to update the row or 0 to drop the row : "))
            if ans ==1:
                queryDel="Delete from quality_education where roll_number=%s and college_id= %s and passing_year= %s"
                cursor1=connection.cursor()
                cursor1.execute(queryDel,tup)
                print(cursor1.rowcount, "Record deleted successfully from quality education table")
                cursor.close()
                cursor = connection.cursor()
                cursor.execute(query_ins,results)
                connection.commit()
                print(cursor.rowcount, "Record inserted successfully into Quality Education table")
                cursor.close
            else:
                print("New record is ignored")
        else:
            print("Cannot enter data because of foreign key constraints")
            


# In[29]:


try:
    connection = mysql.connector.connect(host='localhost', database='dw2',user='root',password='pragyasql')
    
   

    dataInsert=('MT19073','c1',2018,3)
    insert_quality_edu(dataInsert)
    
except mysql.connector.Error as error:
    print("Failed to insert record into Quality Education table {}".format(error))

finally:
    if (connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")


# In[33]:


def insert_career_prog(results):
    query_ins="insert into carrer_progression(roll_number, college_id, passing_year,overall_satisfaction) values(%s,%s,%s,%s)"
    query="select roll_number,college_id,passing_year from student";
    cursor=connection.cursor()
    cursor.execute(query)
    records=cursor.fetchall()
    list_of_tuples=[]
    for row in records:
        list_of_tuples.append(row)
        
    query1="select roll_number,college_id,passing_year, overall_satisfaction from carrer_progression";
    cursor=connection.cursor()
    cursor.execute(query1)
    records1=cursor.fetchall()
    list_of_all_tuples=[]
    for row in records1:
        list_of_all_tuples.append(row)
    if pd.isnull(results[2]):
        print("Year cannot be null")
    elif pd.isnull(results[3]):
        print("Cannot insert all the null values")
    elif(results[3]>5 or results[3]<1):
        print("Enter the satisfaction in range of 1 to 5")
    elif results in list_of_all_tuples:
        print("Duplicate rows")
    else:
        tup=(results[0],results[1],results[2])
        if tup in list_of_tuples:
            ans=int(input("Enter 1 to update the row or 0 to drop the row : "))
            if ans ==1:
                queryDel="Delete from carrer_progression where roll_number=%s and college_id= %s and passing_year= %s"
                cursor1=connection.cursor()
                cursor1.execute(queryDel,tup)
                print(cursor1.rowcount, "Record deleted successfully from career progression table")
                cursor.close()
                cursor = connection.cursor()
                cursor.execute(query_ins,results)
                connection.commit()
                print(cursor.rowcount, "Record inserted successfully into career progression table")
                cursor.close
            else:
                print("New record is ignored")
        else:
            print("Cannot enter data because of foreign key constraints")
            


# In[34]:


try:
    connection = mysql.connector.connect(host='localhost', database='dw2',user='root',password='pragyasql')
    
   

    dataInsert=('MT19073','c1',2018,2)
    insert_career_prog(dataInsert)
    
except mysql.connector.Error as error:
    print("Failed to insert record into Career Progression table {}".format(error))

finally:
    if (connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")


# In[21]:


def insert_place_stats():
    query="select college_id from college";
    cursor=connection.cursor()
    cursor.execute(query)
    records=cursor.fetchall()
    cids=[]
    for row in records:
        cids.append(row[0])
    cids=list(set(cids))
#     print(cids)
    query5="select year from year";
    cursor5=connection.cursor()
    cursor5.execute(query5)
    records5=cursor5.fetchall()
    uni_year=[]
    for row in records5:
        uni_year.append(row[0])
    uni_year=list(set(uni_year))
    print(uni_year)
    
    for i in cids:
        max_pkg={}
        sum_pkg={}
        
        count_year={}
        tup=(i,)
        query1="select passing_year,package from placements where college_id = %s"
        cursor1=connection.cursor()
        cursor1.execute(query1,tup)
        records=cursor1.fetchall()
        print(records)
        print(cursor1.rowcount, "Record selected")
        cursor1.close()
        for row in records:
            max_pkg[row[0]]=0
            sum_pkg[row[0]]=0
            count_year[row[0]]=0
        for row in records:
            x=max_pkg[row[0]]
            if(row[1]>x):
                max_pkg[row[0]]=row[1]
            sum_pkg[row[0]]+=row[1]
            count_year[row[0]]+=1
        
        
        for y in sum_pkg:
            if(count_year[y]!=0):
                sum_pkg[y]/=count_year[y]
        queryInsert="insert into placement_stats (college_id,year,highest_package,avg_package) values (%s,%s,%s,%s)"
        
        for y in sum_pkg:
            tempTuple=(i,)
            tempTuple=tempTuple+(y,max_pkg[y],sum_pkg[y])
            print(tempTuple)
            cursor2=connection.cursor()
            cursor2.execute(queryInsert,tempTuple)
            connection.commit()
            cursor2.close()
        
        


# In[22]:


try:
    connection = mysql.connector.connect(host='localhost', database='dw2',user='root',password='pragyasql')
    
    insert_place_stats()
    
except mysql.connector.Error as error:
    print("Failed to insert record into Placement Stats table {}".format(error))

finally:
    if (connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")


# In[ ]:




