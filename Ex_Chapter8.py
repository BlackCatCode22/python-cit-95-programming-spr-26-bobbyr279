han = open('mbox-short.txt')

for line in han:
    line = line.rstrip()
    wds = line.split()
    # Guardian pattern if line does not have 3 words then skip to prevent lines that have From but no more words after
    if len(wds) < 3:
        continue
    # find lines that start with From else skip
    if wds[0] != 'From':
        continue
    # print the third word in line
    print(wds[2])

