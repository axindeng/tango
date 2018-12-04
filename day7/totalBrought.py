allGuests = {   'Alice':{'apple':5,'pretzels':12},
                'Bob':{'ham sandwiches':3,'apple':2},
                'Carol':{'cups':3,'apple pies':1}}

def totalBorught(guests,item):
    numBrought = 0
    for k,v in guests.items():
        numBrought = numBrought + v.get(item,0)
    return numBrought

print('Number of things being brought:')
for i in ['apple','cups','cakes','ham sandwiches','apple pies','pretzels']:
    print(' - ' + i + ': ' + str(totalBorught(allGuests,i)))

