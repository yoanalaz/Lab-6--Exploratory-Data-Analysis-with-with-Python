# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 19:14:43 2025

@authors: Yoana Lazarova and Guila Amar
"""

# Part 3 – Understanding and preparing the data

#2) 
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

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
table = pd.crosstab(World_Dem['Region'],World_Dem['High Income Economy'])
print(table)
print()


#9)
filtered_data = World_Dem[World_Dem['Life expectancy, female'] > 80] # filters out the countries where female life expectancy is less than 80

print(filtered_data['Country Name'])

#Part 4 - Visualizing statistical relationships



#1) “Is there any association between GNI per capita and life expectancy?
#By taking a look at both scatter graphs(female and male), both increase their life expectency as their GNI per capita increase
#and eventually stagnates at a certain point., because as we know life is not eternal. 

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


#5.0 Is there a relationship between life expentancy and the number of physiciens? Is it similar for males and females?

# Reshape Data to have 2 seperate colomns for each value (male and female ) to be able to split life expectancy between genders in graphs using 'col'.
cols_to_melt= ['Life expectancy, male','Life expectancy, female']
World_Dem= World_Dem.melt(
    id_vars=[col for col in World_Dem.columns if col not in cols_to_melt], # Keep intact all the other colomns using a conditional.
   value_vars=cols_to_melt,
   var_name='Gender',             #new column name for the old column headers
   value_name='Life expectancy'  # new columm name for the values
)   

#Clean up the Gender columm
World_Dem['Gender']=World_Dem['Gender'].replace({'Life expectancy, male':'Male', 'Life expectancy, female': 'Female'})

#Plot the graphs side by side 
sb.relplot(data= World_Dem, x='Physicians', y='Life expectancy', col= 'Gender')

#Answer: Yes, as the number of physicians increase (professionals in healt care), the life expecancy of both males and females increase.
#However compared to the males, females display visually on the graph a higher life expectancy than males, which makes sense because it is know that woman generaly live longer than man.

#5.1 Is there a relationship between female education and females in representation in politcs and does it vary across regions? 
sb.relplot(data=World_Dem, x='Tertiary education, female', y= 'Women in national parliament', col='Region')

#Answer: We observe that usually as the number of women are educated, the number of women present in the national parliment usually increases, but it really depends on the region. 
#For exemple, in Africa this correlation seems less important, because there is less women in general that has access to tertiary education, but there is a big presence of women in politics.  

#5.2 Is there a relationship between population size and greenhouse gas emissions?
sb.relplot(data=World_Dem,x='Population', y= 'Greenhouse gas emissions', col='Region')

#Answer: Yes, there is positive correlation; gas emissions increase with population increase. It is lowest in Africa and higuest in America. 
    
#5.3 Do wealthier countries (higher capita) produce fewer gas emissions per capita?

# Compute GNI per capita if not already present
if "GNI per capita" not in World_Dem.columns:
    World_Dem["GNI per capita"] = World_Dem["GNI"] / World_Dem["Population"]

# Compute emissions per capita
World_Dem["Emissions per capita"] = World_Dem["Greenhouse gas emissions"] / World_Dem["Population"]

# Plot relationship
sb.set(style="whitegrid")
plot1 = sb.lmplot(data=World_Dem,x="GNI per capita",y="Emissions per capita",hue="Region",)


plt.title("Relationship between Wealth and Emissions per Capita")
plt.xlabel("GNI per Capita (USD)")
plt.ylabel("Emissions per Capita")
plt.show()
#Answer:
    
#5.4 Does tourism depend on population size or economic wealth of a country?

#Answer: 
    
#5.5 Is there a smaller gap in education between males and females in high income economies?
World_Dem['Education Gap']= World_Dem['Tertiary education, male']-World_Dem['Tertiary education, female']
sb.relplot( data= World_Dem, x='GNI', y= 'Education Gap',hue='High Income Economy', col='Region')

#Answer: In general, yes there is in fact a smaller gap in education in high income economies such as in America, Asia and Oceania. However, it seems to be the opposite in Europe, where the gap is higher for high income economies (in orange).
    
#6)

#a)
#b)
#c)