#function to open
def readdata():
    f = open("day2/day2data.txt", "r")
    return f.read().splitlines()

def main():
    pointsA = 0
    i=0
    #dict config for the 2nd excersise
    newdict={
        "A Y" : "4",
        "A X" : "3",
        "A Z" : "8",
        "B Y" : "5",
        "B X" : "1",
        "B Z" : "9",
        "C Y" : "6",
        "C X" : "2",
        "C Z" : "7"
    }
    a = readdata()
    solution = 0
    #with the loop we provide the key for the dict
    #we receive the value and add in the counter for the final solution
    for i in a:
        points = newdict.get(i)
        solution = int(solution) + int(points)
        xxx = 0
    print(solution)

main()