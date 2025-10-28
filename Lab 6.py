# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 19:14:43 2025

@authors: Yoana Lazarova and Guila Amar
"""

# Part 3 – Understanding and preparing the data

#2) 
import pandas as pd
import seaborn as sb

World_Dem=pd.read_csv('wdi_wide.csv')

#3)  
print(World_Dem.info())
#How many empty values for the column “Physicians” and  “Population”?
#Physiciens: 10 empty values (217-207=10) and Population: 0 empty values 


#4) 
print(World_Dem.nunique())

#5)
print(World_Dem.describe()) 
#What exactly does the output of this function provide?
#It give us a simple statistical analysis of the numerical values--> mean,sd,min,max etc.

#6) 
World_Dem['GNI per capital']= World_Dem['GNI']/ World_Dem['Population'] 
World_Dem['GNI per capital']= World_Dem['GNI per capital'].round(2) 

#7)
#a) 
print(World_Dem['Region'].value_counts())

#b)
print(World_Dem['High Income Economy'].value_counts())


#8)

#9)

#Part 4 - Visualizing statistical relationships

#1)

#2)

#3)

#4)

#5)

#6)

#a)
#b)
#c)