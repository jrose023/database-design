# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 00:51:10 2017

@author: julie
"""


#gets rid of unnecessary data columns
#will re-scrub for the graphing 
def scrub():
    
    print("Quarterly Census of NYS Employment & Wage Data.")
    #open the file
    try:
        source = "part0_Quarterly_Census_of_Employment_and_Wages__QCEW__Historical_Annual_Data__1975_-_2000.tsv"
        file = open(source, 'r')
    except:
        print("File unable to open. Try again")
    else:  #read & write that shit
    
        #make a new file to hold output
        target = source[:-4] + "_out.tsv"
        out = open(target, 'w') 
        
        for line in file:
            #remove newline 
            line = line.strip("\n")
            #split by tab
            values = line.split("\t")
            
            
#           0 State FIPS, 1 County FIPS, 2 County Name,
#           3 Industry, 4 Industry Title, 5 Year,
#           6 Reporting Units, 7 Average Employment, 8 Average Annual Wages,
#           9 Total Wages, 10 Average Weekly Wages
            
            #remove state fips number and reporting units
            values.pop(6)
            values.pop(0)

#           0 County FIPS, 1 County Name,
#           2 Industry, 3 Industry Title, 4 Year,
#           5 Average Employment, 6 Average Annual Wages,
#           7 Total Wages, 8 Average Weekly Wages
            
            #switch the order of last 3 columns to 
            #total wages | avg weekly | average annual
            #because that makes more logical sense, says me
            weekly = values.pop(8)
            total = values.pop(7)
            values.insert(6, total)
            values.insert(7, weekly)
        
            #for reference:
            #the avg weekly = total wages / avg monthly employment / 52
            #the avg yearly = total wages / avg monthly employment
                                
            #write to output file
            new_line = ""
            for v in values:
                 new_line+=v+"\t"
            out.write(new_line + "\n")
                
        file.close()
        out.close()
         