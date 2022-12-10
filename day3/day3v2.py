#function to open
def readdata():
    f = open("day3/day3data.txt", "r")
    return f.read().splitlines()

def main():
    c=0
    finalvalue = 0
    lines = readdata()
    #print(alldata)
    #longitud = len(alldata)
    #for n in range(longitud):
    x = iter(lines)
    for arr1,arr2,arr3 in zip(x,x,x):
        for letter in arr1:
            if letter in arr2:
                if letter in arr3:
                    print(letter)
                    value = (ord(letter)) 
                    #print(value)
                    if ord(letter) < 96:
                        total = value - 38
                    else:
                        total = value - 96
                    finalvalue = finalvalue + total
                    print(finalvalue)
                    break
main()


