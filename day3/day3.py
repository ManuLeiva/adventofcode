#function to open
def readdata():
    f = open("day3/day3data.txt", "r")
    return f.read().splitlines()

def main():
    c=0
    finalvalue = 0
    alldata = readdata()
    print(alldata)
    longitud = len(alldata)
    for n in range(longitud):
        valor = alldata[n]
        a1 = valor[:len(valor)//2]
        a2 = valor[len(valor)//2:]
        #print(a1)
        #print(a2)
        for letter in a1:
            if letter in a2:
                #print(letter)     
                value = (ord(letter)) 
                #print(value)
                if ord(letter) < 96:
                    total = value - 38
                else:
                    total = value - 96
                finalvalue = finalvalue + total
                #print(finalvalue)
                break 
main()


