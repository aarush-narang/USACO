"""
ID: Aarush Narang [anarang2]
LANG: PYTHON3
TASK: ride
"""

def readInput():
    fin = open('ride.in', 'r')
    comet = fin.readline().strip()
    group = fin.readline().strip()
    cometNum = 1
    groupNum = 1

    for cchar in comet: cometNum *= (ord(cchar.lower()) - 96)
    for gchar in group: groupNum *= (ord(gchar.lower()) - 96)

    return cometNum % 47 == groupNum % 47

def main():
    res = readInput()

    with open('ride.out', 'w') as f:
        if res: f.write('GO\n')
        else: f.write('STAY\n')

if __name__ == '__main__':
    main()