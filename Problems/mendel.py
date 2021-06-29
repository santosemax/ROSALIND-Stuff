#!/usr/bin/python3
import numpy as np

probList = []

# Part A Function
def probOfMating(array):
    for i in range(len(array)):
            for k in range(len(array)):
                total = array[0] + array[1] + array[2]
                if i != k:
                    prob = (array[i] / total) * (array[k] / (total-1))
                else:
                    prob = (array[i] / total) * ((array[k] - 1) / (total-1))
                probList.append(prob)
    print(probList)
    print(sum(probList))

    # Part B
    


with open("test.txt", "r") as file:
    reader = file.read()

    reader_array = list(map(int, reader.split(" ")))
    

    probOfMating(reader_array)







# Notes:
# Given three integers: k, m, n
#   These represent a population of k + m + n
# k = homozygous dominant for a factor
# m = heterozygous
# n = homozygous recessive


# Any two organisms can mate.
# Return probability that two randomly selected mating organisms will produce
# an indiv possessing a dom allele.
