def readdata():
    f = open("day4/day4data.txt", "r")
    return f.read().splitlines()

def main():
    count = 0
    alldata = readdata()
    long = len(alldata)
    for n in range(0,long):
        sepbycoma = alldata[n].split(',') #separate the input by the comma
        print(sepbycoma)
        sepbydash1 = sepbycoma[0].split('-') #separate the 1st chunk by the dash
        sepbydash2 = sepbycoma[1].split('-') #separate the 2nd chunk by the dash
        #print(sepbydash1[0], sepbydash2[0]) #this is a and b 
        #print(sepbydash1[1], sepbydash2[1]) # this is c and d
        a = int(sepbydash1[0])
        c = int(sepbydash1[1])
        b = int(sepbydash2[0])
        d = int(sepbydash2[1])
        print(a, c, b, d)
        if a == b and c == d: # a = c, b = d
            print("hola")
            count = count+1
        elif a > b and c < d: # a > c, b < d
            count = count+1
        elif a > b and c == d: # a > c, b = d
            count = count+1
        elif a < b and c > d: # a < c, b > d
            count = count+1
        elif a < b and c == d: # a < c, b = d
            count = count+1
        elif a == b and c > d: # a = c, b > d
            count = count+1
        elif a == b and c < d: # a = c, b < d
            count = count+1
        else:
            print(":(")
    print(count)
main()