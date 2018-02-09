# -*- coding: utf-8 -*-
"""
Spyder Editor
"""

'''
combining the 138 CSV files into one file
data categories:
    year
    name
    frequency
    sex
tack year onto the data into one file

'''



import csv

def main():
    
    print("Welcome to the Social Security Name Dataset.")
    try:
        start = int(input("Enter start year between 1880 and 2016 to learn about a decade: \n"))
    except:
        print("Invalid year selection! Try again.")
    else:
        if start < 1880 or start > 2016:
            print("Invalid year selection! Try again.")
        else:
            #make a new file to hold output
            target = "names_out" + str(start) + "to" + str(start+10) + ".txt"
            out = open(target, 'w')
            writer = csv.writer(out, delimiter = ",")        
            lines_read,lines_written = 0,0
            
            #write the header column
            writer.writerow(['name','sex','frequency','year'])
            lines_written += 1
                
            #get the correct file name for this decade
            for i in range(start, start+10):
                year = str(i)
                source = "yob" + year + ".txt"
                   
                #open file
                try:
                    file = open(source, 'r')
                except:
                    print("File could not open. Try again!")
                    break
                
                #write to output file
                else:
                    for line in file:
                        lines_read += 1
                        #remove newline 
                        line = line.strip("\n")
                        
                        #split by comma
                        values = line.split(',')
                        
                        if ((values[0] != 'Unknown') or (values[0] != 'baby')) and (int(values[2]) >= 500):
                            #add new data field to array
                            values.extend([year]) 
                            
                            print(values)
                    
                            #write to output file
                            writer.writerow(values)
                            lines_written += 1
                        
                    file.close()
            out.close()
                
main()













