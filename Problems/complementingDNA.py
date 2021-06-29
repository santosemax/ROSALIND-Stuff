from sys import exit

# Get DNA Strand
dnaStrand = input('Please input your DNA strand here: ')
reversedStrand = dnaStrand[::-1] # Increment throught the string backwards to reverse it (slicing)

for alpha in reversedStrand:
    if alpha == 'A':
        print('T', end="")
    if alpha == 'T':
        print('A', end="")
    if alpha == 'C':
        print('G', end="")
    if alpha == 'G':
        print('C', end="")
print()
