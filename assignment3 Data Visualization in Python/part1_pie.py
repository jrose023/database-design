# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 01:18:57 2017

@author: julie
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 12:56:00 2017

@author: julie
"""


import matplotlib.pyplot as plt

def graph2():    
    #sliceSs are going to be the 9 industries
    #percentages will either be the total wages or employment -- both?
    #pick one year to slice? or add up all years? idk
    
    opt = input("Choose total wages or average employment ('w' or 'e'): ")
    if opt == 'w':
        which = True #true = wages
        title = "New York State Total Wages per Industry in "
    else: 
        which = False
        title = "New York State Employment per Industry in "
        
    year = int(input("Enter year (1975-2000) to view: "))
    
    # Data to plot
    labels = 'Agriculture, Mining & Unclassified','Construction','Manufacturing','Transportation & Public Utilities','Wholesale Trade','Retail Trade','Finance,  Insurance & Real Estate','Services','Public Administration'
    sizes = [parse2(which, year, 1), parse2(which, year, 3),
             parse2(which, year, 4), parse2(which, year, 5),
             parse2(which, year, 6), parse2(which, year, 7),
             parse2(which, year, 8), parse2(which, year, 9),
             parse2(which, year, 10) ]
        
#    print(labels)
#    print(sizes)
    colors = ['#FFA726','#FFEB3B','#00796B','#9CCC65','#03A9F4','#3F51B5','#BA68C8','#CE93D8','#F06292']
#
    explode = (0,0,0,0,0,0,0,0,0)
#     
    # Plot
    plt.title(title + str(year), fontsize=15)
    plt.pie(sizes, 
            colors=colors,
            startangle=140,
            autopct='%2.1f%%')
    plt.legend(labels, loc="best")
    plt.tight_layout()
    plt.axis('equal')
    plt.show()
    
     
def parse2(w,y,n):
    try:
        source = "part0_Quarterly_Census_of_Employment_and_Wages__QCEW__Historical_Annual_Data__1975_-_2000_out.tsv"
        file = open(source, 'r')
    except:
        print("File unable to open. Try again")
    else:  #read & write that shit
        out = 0  #out holds total wages for that year
        toprow = True
        for line in file:
            #remove newline 
            line = line.strip("\n")
            #split by tab
            values = line.split("\t")
      
            if toprow==False:
                #if statewide
                if(int(values[0]) == 0):  
                    #if the year is right
                    if (y == int(values[4])):
                        # if the industry
                        if (n == int(values[2])):
                            #collect Total WAyg
                            if(w): #wages
                                out = int( values[6])
                            else: #employment
                                out = int(values[5])
            else:
                toprow=False
                
        return out
    file.close()
    
    
graph2()
