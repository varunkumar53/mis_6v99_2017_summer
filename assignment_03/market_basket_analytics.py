
# coding: utf-8

# In[1]:

import requests
import pandas as pd
import numpy as np
import re
from itertools import combinations


# In[2]:

# ************************** Download the training dataset ***************************************** #

# Link To Download the training dataset #

training_datalink="http://kevincrook.com/utd/market_basket_training.txt"

# Request the response of the training dataset #

r=requests.get(training_datalink)

# Create "market_basket_training.txt" and the write the contents of the URL in the TextFile #

training_dataset=open("market_basket_training.txt","wb")
training_dataset.write(r.content)
training_dataset.close()


# In[3]:

# ************************** Download the training dataset ***************************************** #

# Link To Download the test dataset #

test_datalink="http://kevincrook.com/utd/market_basket_test.txt"

# Request the response of the test dataset #

r=requests.get(test_datalink)

# Create "market_basket_test.txt" and the write the contents of the URL in the TextFile #

test_dataset=open("market_basket_test.txt","wb")
test_dataset.write(r.content)
test_dataset.close()


# In[4]:

# Creating a dataframe using the  training_dataset #

ColNames = ["A", "B", "C", "D","E"]
Train_DataFrame = pd.read_csv('market_basket_training.txt', sep=",", names = ColNames,index_col=0)


# In[5]:

support=0.000001
# Step to convert into 1s,0s dataframe based on occurence from the tea #
OnesZeros_DataFrame=pd.get_dummies(Train_DataFrame.unstack().dropna()).groupby(level=1).sum()
# To get the shape(dimensions) of the dataframe #
RowLength,ColumnLength  =OnesZeros_DataFrame.shape
pattern = []
for NoOfCombinations in range(0, ColumnLength+1):
    for cols in combinations(OnesZeros_DataFrame, NoOfCombinations):
        NoOfOccurences = OnesZeros_DataFrame[list(cols)].all(axis=1).sum()
        Probability=float(NoOfOccurences)/RowLength
        pattern.append([",".join(cols), Probability])
sdf = pd.DataFrame(pattern, columns=["Pattern", "Support"])
Support_DataFrame=sdf[sdf.Support >= support]


# In[6]:

TwoProductBundle=Support_DataFrame.loc[Support_DataFrame['Pattern'].str.len() ==7]
ThreeProductBundle=Support_DataFrame.loc[Support_DataFrame['Pattern'].str.len() ==11]
FourProductBundle=Support_DataFrame.loc[Support_DataFrame['Pattern'].str.len() ==15]


# In[11]:

TestData_File = open( "market_basket_test.txt", "r" )
Output_File = open("market_basket_recommendations.txt", "w")
lines = []
Products=[]
for line in TestData_File:
    Products=(line[4:-1])
    ProductsList = re.sub("[^\w]", " ",  Products).split()
    #print(ProductsList)
    if len(ProductsList)==1:
        x=TwoProductBundle.loc[TwoProductBundle['Pattern'].str.contains(ProductsList[0])]
        y=x.loc[x['Support'].idxmax()]
        my_list = y.values[0]
        my_list = my_list.split(",")
        if ProductsList[0]==my_list[0]:
            #text_file = open("demo_numpy.txt", "w")
            #strr =(line[:4],my_list[1])
            Output_File.write(line[:4]+my_list[1]+ "\n" )
            #text_file.close()
        else:
            #text_file = open("demo_numpy.txt", "w")
            Output_File.write(line[:4]+my_list[0]+ "\n" )
            #text_file.close()
            
            
            
    elif len(ProductsList)==2:
        x=ThreeProductBundle.loc[ThreeProductBundle['Pattern'].str.contains(ProductsList[0])]
        y=x.loc[x['Pattern'].str.contains(ProductsList[1])]
        if y.shape[0]!=0:
            z=y.loc[y['Support'].idxmax()]
            my_list = z.values[0]
            my_list = my_list.split(",")
            if (ProductsList[0]==my_list[0] and ProductsList[1]==my_list[1]) :
                Output_File.write(line[:4]+my_list[2]+ "\n" )
            elif (ProductsList[0]==my_list[0] and ProductsList[1]==my_list[2]):
                Output_File.write(line[:4]+my_list[1]+ "\n" )
            elif (ProductsList[0]==my_list[1] and ProductsList[1]==my_list[2]):
                Output_File.write(line[:4]+my_list[0]+ "\n" )
        else:
            if 'P04' in ProductsList: ProductsList.remove('P04')
            if 'P08' in ProductsList: ProductsList.remove('P08')
            x=TwoProductBundle.loc[TwoProductBundle['Pattern'].str.contains(ProductsList[0])]
            y=x.loc[x['Support'].idxmax()]
            my_list = y.values[0]
            my_list = my_list.split(",")
            if ProductsList[0]==my_list[0]:
                #text_file = open("demo_numpy.txt", "w")
                #strr =(line[:4],my_list[1])
                Output_File.write(line[:4]+my_list[1]+ "\n" )
                #text_file.close()
            else:
                #text_file = open("demo_numpy.txt", "w")
                Output_File.write(line[:4]+my_list[0]+ "\n" )
                
            
    elif len(ProductsList)==3:
        x=FourProductBundle.loc[FourProductBundle['Pattern'].str.contains(ProductsList[0])]
        y=x.loc[x['Pattern'].str.contains(ProductsList[1])]
        z=y.loc[y['Pattern'].str.contains(ProductsList[2])]
        #print(z)
        if z.shape[0]!=0:
            #print("3")
            w=z.loc[z['Support'].idxmax()]
            my_list = w.values[0]
            my_list = my_list.split(",")
            if (ProductsList[0]==my_list[0] and ProductsList[1]==my_list[1] and ProductsList[2]==my_list[2]) :
                Output_File.write(line[:4]+my_list[3]+ "\n" )
            elif (ProductsList[0]==my_list[0] and ProductsList[1]==my_list[2] and ProductsList[2]==my_list[3]) :
                Output_File.write(line[:4]+my_list[1]+ "\n" )
            elif (ProductsList[0]==my_list[0] and ProductsList[1]==my_list[1] and ProductsList[2]==my_list[3]) :
                Output_File.write(line[:4]+my_list[2]+ "\n" )
            elif (ProductsList[0]==my_list[1] and ProductsList[1]==my_list[2] and ProductsList[2]==my_list[3]) :
                Output_File.write(line[:4]+my_list[0]+ "\n" )
        else:
            if 'P04' in ProductsList: ProductsList.remove('P04')
            if 'P08' in ProductsList: ProductsList.remove('P08')
            if len(ProductsList)==3:
                x=ThreeProductBundle.loc[ThreeProductBundle['Pattern'].str.contains(ProductsList[0])]
                y=x.loc[x['Pattern'].str.contains(ProductsList[1])]
                if y.shape[0]!=0:
                    z=y.loc[y['Support'].idxmax()]
                    my_list = z.values[0]
                    my_list = my_list.split(",")
                    if (ProductsList[0]==my_list[0] and ProductsList[1]==my_list[1]) :
                        Output_File.write(line[:4]+my_list[2]+ "\n" )
                    elif (ProductsList[0]==my_list[0] and ProductsList[1]==my_list[2]):
                        Output_File.write(line[:4]+my_list[1]+ "\n" )
                    elif (ProductsList[0]==my_list[1] and ProductsList[1]==my_list[2]):
                        Output_File.write(line[:4]+my_list[0]+ "\n" )
                else:
                    x=TwoProductBundle.loc[TwoProductBundle['Pattern'].str.contains(ProductsList[0])]
                    y=x.loc[x['Support'].idxmax()]
                    my_list = y.values[0]
                    my_list = my_list.split(",")
                    if ProductsList[0]==my_list[0]:
                        #text_file = open("demo_numpy.txt", "w")
                        #strr =(line[:4],my_list[1])
                        Output_File.write(line[:4]+my_list[1]+ "\n" )
                        #text_file.close()
                    else:
                        #text_file = open("demo_numpy.txt", "w")
                        Output_File.write(line[:4]+my_list[0]+ "\n" )
                    
                
                    
TestData_File.close()
Output_File.close()




