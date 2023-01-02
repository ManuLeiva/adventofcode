import re

def openFile():
    f = open("day5/day5data.txt", "r")
    return f.read().splitlines()

def processlines(lines):
    cranelen = 0
    pattern1 = re.compile(r"(\s+(\d\s+)+)", re.IGNORECASE)
     
    for line in lines:
        if pattern1.match(line):
            cranelen = int(line.split()[-1])
            break
    crane = [''] * cranelen
    
    for line in lines:
        x = iter(line)
        for id,(character1,character2) in enumerate(zip(x,x)):
            if character1 == '[':
                crane[id//2] = crane[id//2] + character2
        if pattern1.match(line):
            break
    #print(crane)
    moves = False
    movement = []
    for line in lines:
        if moves:
            arrtemp = line.split()
            movement.append([int(arrtemp[1]),int(arrtemp[3]),int(arrtemp[5])])
        if line == '':
            moves = True
    return cranelen, crane, movement

def main():
    cranelen, crane, movement = processlines(openFile())

