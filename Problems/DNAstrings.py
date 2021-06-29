# Get Dataset
dnaString = input("Please input DNA string here: ");

# Initialize Counter
A, C, G, T = 0, 0, 0, 0

# Loop
for letter in dnaString:
    if letter == "A":
        A += 1
    elif letter == "C":
        C += 1
    elif letter == "G":
        G += 1
    elif letter == "T":
        T += 1
    else:
        print("Invalid String")

print(f'{A} {C} {G} {T}')
