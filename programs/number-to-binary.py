#turns a number to binary, just breaks if you put in a negative number because im too lazy to fix it

x = int(input("Give a number you'd like to turn to binary "))

binary = []

while x > 0:
    rem = x % 2
    binary.append(rem)
    x //= 2
    print(x, rem)

backwards = binary[::-1]
backwards = ''.join(str(x) for x in backwards)
print(backwards)
exit()
