def readdata():
    f = open("day5/day5data.txt", "r")
    return f.read().splitlines()

def main():
    alldata = readdata()
    print((alldata[0]))
    print(alldata[1])
    print(alldata[2])
    x = alldata[3].split()
    print(x[0])

main()