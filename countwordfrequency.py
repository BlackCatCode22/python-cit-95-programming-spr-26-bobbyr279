fname = input('Enter File: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        # idiom: retrieve/create/update counter
        di[w] = di.get(w, 0) + 1
        #print(w, 'new', di[w])
#print(di)

#find the most common word
largest = -1
theWord = None
for k, v in di.items():
    #print(k, v)
    if v > largest:
        largest = v
        theWord = k
print(theWord, largest)
