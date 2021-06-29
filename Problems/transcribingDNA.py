from sys import exit

# Get DNA String
dnaString = input("Please input your DNA string here: ")

# Iterate through
for alpha in dnaString:
    if alpha == 'T':
        print('U', end="")
    elif alpha == 'G' or 'U' or 'C':
        print(alpha, end="")
    else:
        print('Invalid String')
        exit(1)
print()
