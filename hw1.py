from align_sequence import align, print_alignment
from read_fasta import read_file

dna = read_file("sequences.txt")

dna_alignment_values = [[0]*len(dna) for i in range(len(dna))]


for i in range(len(dna)-1):
    for j in range(i+1,len(dna)):
        alignment = align(dna[i],dna[j])
        dna_alignment_values[i][j] = alignment[-1][-1]
        dna_alignment_values[j][i] = alignment[-1][-1]

print_alignment(dna_alignment_values)
