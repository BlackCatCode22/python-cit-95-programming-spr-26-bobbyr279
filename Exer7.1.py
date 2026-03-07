# open is file handle to open file but does not actually read file
fh = open('mbox-short.txt')

# use for loop to read through all characters in loops
for lx in fh:
    # rstrip() to strip the character from the right hand side, to throw away non-printing characters
    ly = lx.rstrip()
    # upper() prints characters to all upper case
    print(ly.upper())
