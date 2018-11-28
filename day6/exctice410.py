
spam = ['apples','bananas','tofu','cats']

def tango(someList):
    result = ''
    for i in range(len(someList)):
        if i == len(someList) - 1:
            result = result + ' and ' +someList[i]
        else:
            result = result + someList[i] + ', '
    return result

print(tango(spam))
