#!/usr/bin/python3

# Declare empty lists to store line 1 & 2
line1, line2, HammingDistance = [], [], 0

# Open File
with open("test.txt", "r") as file:
    reader = file.read().splitlines()

    # Iterate through each indiv line
    for i in range(len(reader[0])):
        line1 += reader[0][i]
        line2 += reader[1][i]
        
        # Check if chars are matching
        if line1[i] != line2[i]:
            HammingDistance += 1

print(HammingDistance)
