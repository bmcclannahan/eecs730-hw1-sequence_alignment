from align_sequence import align, print_matrix, print_alignment_matrix
from read_fasta import read_file
import time

import os
import psutil

dna = read_file("sequences.txt")
pid = os.getpid()
py = psutil.Process(pid)

dna = read_file("sequences.txt")

def find_family_dna_sequences():
    dna_alignment_values = [[0]*len(dna) for i in range(len(dna))]
    time_values = [[0]*len(dna) for i in range(len(dna))]

    for i in range(len(dna)-1):
        for j in range(i+1,len(dna)):
            start = time.time()
            alignment = align(dna[i],dna[j])
            end = time.time()
            dna_alignment_values[i][j] = alignment[-1][-1]
            dna_alignment_values[j][i] = alignment[-1][-1]
            time_values[i][j] = round(100*(end-start))/100

    time_sum = 0
    for i in range(10):
        time_sum += sum(time_values[i])

    print("Alignment Matrix")
    print_alignment_matrix(dna_alignment_values)

    print("\nTime cost of each alignment")
    print_alignment_matrix(time_values)

    print("\nAverage time:",round(time_sum/.45)/100)

    family_dict = {key: False for key in [0,1,2,3,4,5,6,7,8,9]}
    for i in range(len(dna)):
        positive_count = 0
        #print("i: " + str(i))
        for j in range(len(dna)):
            if dna_alignment_values[i][j] > -300:
                positive_count += 1
            #print("j: " + str(j) + ", positive_count: " + str(positive_count))
        if positive_count >= 3:
            family_dict[i] = True

    print("Sequences ", end="")
    for i in range(10):
        if family_dict[i]:
            print(i+1,end=" ")
    print("are in the same family.")

def profile_sequences():
    mem_values = [[0]*len(dna) for i in range(len(dna))]

    for i in range(len(dna)-1):
        for j in range(i+1,len(dna)):
            mem_values[i][j] = round(align(dna[i],dna[j],py))

    mem_sum = 0
    for i in range(10):
        mem_sum += sum(mem_values[i])

    print("\nMax Memory used for each alignment")
    print_alignment_matrix(mem_values)

    print("\nAverage time:",round(mem_sum/.045)/1000)

find_family_dna_sequences()
profile_sequences()
print_matrix(align(dna[0],dna[1]),dna[0],dna[1])