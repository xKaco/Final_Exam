import math
import sys


def main():

    SUM = 0;            ## sum of temperatures
    AMOUNT = 0;         ## AMOUNT of tempteratures
    NUM = 0;            ## number 

    temperature = eval(sys.argv[1])
    file = open('sensor_temp.txt', 'r')
      
    
    for line in file.read().split('\n')[2:-1]: ##reads the line and splits after the number is read
        AMOUNT  += 1    ##inrement by 1 for each line 
        SUM += eval(line)   ##add them together 
        if eval(line) < temperature:        
           NUM += 1     ## keep track of values under temperature (sys.argv[1])
    
    
    
    AVG = SUM / AMOUNT
    print "             CPE 422/522 Final Exam                  "

    print "Number of Temperatures: ", AMOUNT
    print "Average Temperature: ", AVG
    print "Number of Temperatures below",temperature,"C : ", NUM


if __name__ == "__main__":   ## needed for python script when using functions? 
    main()
