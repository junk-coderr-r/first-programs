#turns a number to binary, just breaks if you put in a negative number because im too lazy to fix it
saved = []

def binaryconvert():
    initial = int(input("Give a number you'd like to turn to binary "))

    x = initial

    binary = []

    while x > 0:
        rem = x % 2
        binary.append(rem)
        x //= 2
        print(x, rem)

    backwards = binary[::-1]
    backwards = ''.join(str(x) for x in backwards)
    print(backwards)
    save = int(input("Would you like to save this input? 1 to save, 2 to close."))

    if save == 1:
        finished = str(initial) + ' = ' + backwards
        saved.append(finished)
        print(saved)
        binaryconvert()
    else:
        exit()
binaryconvert()
