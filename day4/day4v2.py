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
        if a == b and c == d: # a = c, b = d
            print("1")
            count = count+1
        elif a > b and c < d: # a > c, b < d
            print("2")
            count = count+1
        elif a > b and c == d: # a > c, b = d
            print("3")
            count = count+1
        elif a < b and c > d: # a < c, b > d
            print("4")
            count = count+1
        elif a < b and c == d: # a < c, b = d
            print("5")
            count = count+1
        elif a == b and c > d: # a = c, b > d
            print("6")
            count = count+1
        elif a == b and c < d: # a = c, b < d
            print("7")
            count = count+1
        elif a == d and b < a:
            print("8")
            count = count+1
        elif a < b and c == b:
            print("9")
            count = count+1
        elif a<b and b<c:
            print("10")
            count = count+1
        elif a > b and c > d and a >= d:
            print("11")
            count = count+1
        elif a == c and b == d:
            count = count+1
        else:
            print(":(")
    print(count)
main()