def readdata():
    f = open("day5/day5data.txt", "r")
    return f.read().splitlines()

def main():
    alldata = readdata()
    longitud = len(alldata)
    for i in range(0,longitud):
        numero=0
        splitthat = 2
        d = alldata[i]
        separation = d.split(d[1])
        print("HOola",separation)
        for i in d:#iterate through the full line to detect the letter
            print(i)
            # numero = numero+1
            # if i == "[":
            #     letra = d[numero]
            #     print(letra)
            # elif i == "1":
            #     print("hola")
    numbers = alldata[3].split()
    print(numbers[0])
    print(numbers[1])
    print(numbers[2])
main()