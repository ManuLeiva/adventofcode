def readdata():
    f = open("day5/day5data.txt", "r")
    return f.read().splitlines()

def main():
    alldata = readdata()
    for line in alldata:
        x = iter(line)
        for id,(character1,character2) in enumerate(zip(x,x)):
              if character1 == '[':
                crane[id//2] = crane[id//2] + character2

main()