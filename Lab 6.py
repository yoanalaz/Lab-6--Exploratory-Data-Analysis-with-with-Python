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
World_Dem['GNI per capita']= World_Dem['GNI']/ World_Dem['Population'] 
World_Dem['GNI per capita']= World_Dem['GNI per capita'].round(2) 

#7)
#a) 
print(World_Dem['Region'].value_counts())

#b)
print(World_Dem['High Income Economy'].value_counts())


#8) 

#9)

#Part 4 - Visualizing statistical relationships



#1) “Is there any association between GNI per capita and life expectancy?
#By taking a look at both scatter graphs(female and male), both increase their life expectency as their GNI per capita increase and eventually stagnates at a certain point., because as we know life is not eternal. 

sb.relplot(data= World_Dem, x= 'GNI per capita' ,y= 'Life expectancy, female')
sb.relplot(data= World_Dem, x= 'GNI per capita' ,y= 'Life expectancy, male')

#2) Does the association between GNI per capita and life expectancy vary by region?
#Yes, it does. For exemple, we see that in Africa the income stays low compared to the other regions aswell as the life expectancy.
#However, in Europe, the incomes are much higher and the life expectancy is between 75 and 80 +. 

sb.relplot(data= World_Dem, x= 'GNI per capita' ,y= 'Life expectancy, female', hue='Region')
sb.relplot(data= World_Dem, x= 'GNI per capita' ,y= 'Life expectancy, male', hue='Region')

#3) Why can't we see the area representing a standard deviation in the plot? 
#Because the data used for the line plot has already been summarized, 
#meaning that each value of GNI per capita has only one mean life expectancy value for there are no multiple data points per x for Seaborn to calculate the sd from.

sb.relplot(data= World_Dem, x= 'GNI per capita' ,y= 'Life expectancy, female', hue= 'Region', kind='line', errorbar='sd')
sb.relplot(data= World_Dem, x= 'GNI per capita' ,y= 'Life expectancy, male', hue= 'Region', kind='line', errorbar='sd')

#4)   
sb.lmplot(data= World_Dem, x= 'GNI per capita' ,y= 'Life expectancy, female', hue= 'Region')
sb.lmplot(data= World_Dem, x= 'GNI per capita' ,y= 'Life expectancy, male', hue= 'Region')

#5)

#6)

#a)
#b)
#c)