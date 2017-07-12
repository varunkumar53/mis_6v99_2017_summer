
# coding: utf-8

# In[100]:


# Importing the necessary library #

import requests
import os
import zipfile
import openpyxl
import sqlite3
import glob


# In[101]:

# ************************** CSV FILE PART ***************************************** #

# Link To Download the CSV Flat Files #

CSV_URL="https://data.medicare.gov/views/bg9k-emty/files/0a9879e0-3312-4719-a1db-39fd114890f1?content_type=application%2Fzip%3B%20charset%3Dbinary&filename=Hospital_Revised_Flatfiles.zip"

# Request the response of the CSV_URL #

r=requests.get(CSV_URL)

# Create a 'Staging' Directory #

staging_dir_name="staging"
os.mkdir(staging_dir_name)

# Create a Path for the ZipFile #

zip_file_name=os.path.join(staging_dir_name,"DownLoadCSV.zip")

# Create "DownLoadCSV.zip" and the write the contents of the URL in the ZipFile #

ZipFile=open(zip_file_name,"wb")
ZipFile.write(r.content)
ZipFile.close()

# To UnZip all the CSV Files in the Staging table #

z=zipfile.ZipFile(zip_file_name,'r')
z.extractall(staging_dir_name)
z.close()


# In[102]:

# ************************** EXCEL FILE PART ***************************************** #

# Link To Download the EXCEL File #

EXCEL_URL="http://kevincrook.com/utd/hospital_ranking_focus_states.xlsx"

# Request the response of the EXCEL_URL #

r=requests.get(EXCEL_URL)

# Create "hospital_ranking_focus_states.xlsx" and the write the contents of the URL in the ZipFile #

xf=open("hospital_ranking_focus_states.xlsx","wb")
xf.write(r.content)
xf.close()



# In[103]:

## Open hospital_ranking_focus_states.xlsx ##

wb=openpyxl.load_workbook("hospital_ranking_focus_states.xlsx")

## Print the Sheets Names in the WorkBook  ##


for sheet in wb.get_sheet_names():
    print(sheet)
    
       
## Assign Sheet Names to respective sheets ##

sheet1=wb.get_sheet_by_name("Hospital National Ranking")
sheet2=wb.get_sheet_by_name("Focus States")



i=2
StatesList=[]
while sheet2.cell(row=i,column=1).value!=None:
    #print(sheet2.cell(row=i,column=1).value,"|",sheet2.cell(row=i,column=2).value)
    State=[sheet2.cell(row=i,column=1).value]
    StatesList=StatesList+State
    i+=1

StatesList.insert(0, "Nationwide")


# In[104]:

wb=openpyxl.Workbook()

wb.remove_sheet(wb.get_sheet_by_name('Sheet'))



Sheets=0

while Sheets<11:
    
    sheet_1=wb.create_sheet(StatesList[Sheets])
    i=1
    head=0
    Headers=["Provider ID","Hospital Name","City","State","County"]
    while i<6:

        sheet_1.cell(row=1,column=i,value=Headers[head])
        i=i+1
        head=head+1
    Sheets+=1

wb.save("hospital_ranking.xlsx")


# In[105]:

wb=openpyxl.Workbook()

wb.remove_sheet(wb.get_sheet_by_name('Sheet'))



Sheets=0

while Sheets<11:
    
    sheet_1=wb.create_sheet(StatesList[Sheets])
    i=1
    head=0
    Headers=["Measure ID","Measure Name","Minimum","Maximum","Average","Standard Deviation"]
    while i<7:

        sheet_1.cell(row=1,column=i,value=Headers[head])
        i=i+1
        head=head+1
    Sheets+=1

wb.save("measures_statistics.xlsx")



# In[106]:

conn=sqlite3.connect("medicare_hospital_compare.db")


# In[ ]:



