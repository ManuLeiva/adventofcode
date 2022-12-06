#function to open
def readdata():
    f = open("day1/day1data.txt", "r")
    return f.read().splitlines()

#main funciton for the excersise
def main():
    #results from 1st function added into variable
    resultfunction = readdata()
    #variables needed
    totalline = 0
    totalline1=0
    thelist=[]
    #we iterate all the values from the file
    #1st we check the non empty lines
    for line in resultfunction:
        if line != '':
            #we sum what we have and had
            totalline = totalline + int(line)
            #adding to a list for 2nd excersise
            thelist.append(totalline)
        else:
            #save the highest value
            if totalline > totalline1:
                totalline1 = totalline
                #reset the counter
                totalline=0
            else:
                #reset the counter
                totalline=0
    print(totalline1, "final") #final result
    thelist.sort()
    for i in range (3):
        var1=thelist[-1]
        var2=thelist[-2]
        var3=thelist[-3]
    finalv=var1+var2+var3
    print(finalv)#summ the 3 highest values
main()

