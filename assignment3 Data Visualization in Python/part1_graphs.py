# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 12:56:00 2017

@author: julie
"""


import pylab

def graph1():    
    #x axis is going to be 25 years 1975-200
    #y axis is going to be annual wages for each year
    #10 different lines: will represent each industry
    
    x = list(range(1,27))
    years = []
    for i in range(75, 100): 
        years.append(i)
    years.append("00")
    
    pylab.xticks(x,years)
    
    pylab.title('New York State Annual Wages across 10 Industry Categories')
    pylab.xlabel('Year')
    pylab.ylabel('Average Annual Wage')
    
    pylab.plot(x,parse(0),color='black',label="All Inustry Average")
    pylab.plot(x,parse(1),color='#FFA726',label="Agriculture, Mining & Unclassified") 
    pylab.plot(x,parse(3),color='#FFEB3B',label="Construction") 
    pylab.plot(x,parse(4),color='#9CCC65',label="Manufacturing") 
    pylab.plot(x,parse(5),color='#00796B',label="Transportation & Public Utilities") 
    pylab.plot(x,parse(6),color='#03A9F4',label="Wholesale Trade")
    pylab.plot(x,parse(7),color='#3F51B5',label="Retail Trade") 
    pylab.plot(x,parse(8),color='#BA68C8',label="Finance,  Insurance & Real Estate") 
    pylab.plot(x,parse(9),color='#CE93D8',label="Services") 
    pylab.plot(x,parse(10),color='#F06292',label="Public Administration")
 
    pylab.legend(loc='upper left')
    pylab.show() 
            
    
def parse(n):
    try:
        source = "part0_Quarterly_Census_of_Employment_and_Wages__QCEW__Historical_Annual_Data__1975_-_2000_out.tsv"
        file = open(source, 'r')
    except:
        print("File unable to open. Try again")
    else:  #read & write that shit
        out = []  #out is gonna hold 25 years of wages for one industry
        toprow = True
        for line in file:
            #remove newline 
            line = line.strip("\n")
            #split by tab
            values = line.split("\t")
      
            if toprow==False:
                #if statewide
                if(int(values[0]) == 0):         
                    # cases for each industry
                    if (n == int(values[2])):
                        out.append(values[8])
                        
            else:
                toprow=False
                
        return out
graph1()



