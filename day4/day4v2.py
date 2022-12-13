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
        a = int(sepbydash1[0])
        c = int(sepbydash1[1])
        b = int(sepbydash2[0])
        d = int(sepbydash2[1])
        print(a, c, b, d)
        if a > b and a > d: # a = c, b = d
            print("1")
            count = count+1
        elif c < b and c < b: # a > c, b < d
            print("2")
            count = count+1
        
        else:
            print(":(")
    print(long)
    print(count)
    print(long-count)
main()