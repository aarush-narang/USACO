"""
ID: Aarush Narang [anarang2]
LANG: PYTHON3
TASK: gift1
"""

def parseFile(): # splits the file into a list of names and a list of groups which include the giver, the money + number of recievers, and the recievers
    with open('gift1.in', 'r') as f:
        lines = f.read().split('\n')

    np = int(lines[0])
    names = lines[1:np+1]
    info = lines[np+1:]
    groups = []
    for i in range(len(info)-1):
        money = info[i+1].split(' ')
        if len(money) == 2:
            groups.append(info[i:i+int(money[1])+2])
    
    return names, groups

def calc(names, groups):
    bank = {}
    for name in names: bank[name] = 0
    for group in groups:
        [money, numOfPeople] = group[1].split(' ') # destructuring the money and number of people
        if int(numOfPeople) == 0: numOfPeople = 1 # prevent divide by zero error
        bank[group[0]] -= int(money)  # subtract the money from the person who gave the gift
        bank[group[0]] += (int(money) % int(numOfPeople)) # add the remainder of the money given to the person who gave the gift

        amt = int(money) // int(numOfPeople) # the amount each person gets
        recievers = group[2:]
        
        for reciever in recievers:
            bank[reciever] += amt

    return bank

def main():
    parsed = parseFile()
    bank = calc(*parsed)

    with open('gift1.out', 'w') as f:
        for name in bank:
            f.write(name + ' ' + str(bank[name]) + '\n')

if __name__ == '__main__':
    main()