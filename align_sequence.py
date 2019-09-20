
def align(seq1, seq2, process = None):
    matrix = [[0]*(len(seq2)+1) for i in range(len(seq1)+1)]
    for i in range(len(seq1)+1):
        for j in range(len(seq2)+1):
            if i == 0:
                matrix[i][j] = j*-3
            elif j == 0:
                matrix[i][j] = i*-3
            else:
                d = -2
                if seq1[i-1] == seq2[j-1]:
                    d = 1
                left = matrix[i-1][j] - 3
                up = matrix[i][j-1] - 3
                diag = matrix[i-1][j-1] + d
                matrix[i][j] = max([left,up,diag])
    if process is not None:
        return process.memory_info()[0]/1000000
    return matrix

def print_matrix(alignment_matrix,seq1,seq2):
    first_sequence = ""
    second_sequence = ""
    gap_line = ""
    i = len(alignment_matrix)-1
    j = len(alignment_matrix[0])-1
    while i > 0 or j > 0:
        # print("i:",i,"j:",j)
        # print(first_sequence)
        # print(gap_line)
        # print(second_sequence)
        current = alignment_matrix[i][j]
        if i > 0 and current - alignment_matrix[i-1][j] == -3:
            first_sequence = seq1[i-1] + first_sequence
            second_sequence = "-" + second_sequence
            gap_line = " " + gap_line
            i -= 1
            # print(1)
        elif current - alignment_matrix[i][j-1] == -3:
            first_sequence = "-" + first_sequence
            second_sequence = seq2[j-1] + second_sequence
            gap_line = " " + gap_line
            j -= 1
            # print(2)
        elif i > 0 and j > 0 and current - alignment_matrix[i-1][j-1] == 1:
            first_sequence = seq1[i-1] + first_sequence
            second_sequence = seq2[j-1] + second_sequence
            gap_line = "|" + gap_line
            j -= 1
            i -= 1
            # print(3)
        elif i > 0 and j > 0 and current - alignment_matrix[i-1][j-1] == -2:
            first_sequence = seq1[i-1] + first_sequence
            second_sequence = seq2[j-1] + second_sequence
            gap_line = " " + gap_line
            j -= 1
            i -= 1
            # print(4)
        else:
            i -= 1
            j -= 1
            print(5)
    print("\nThe alignment is:")
    for i in range(len(first_sequence)//70+1):
        if len(first_sequence) < (i+1)*70:
            print(first_sequence[i*70:].rstrip())
            print(gap_line[i*70:].rstrip())
            print(second_sequence[i*70:].rstrip())
        else:
            print(first_sequence[i*70:(i+1)*70].rstrip())
            print(gap_line[i*70:(i+1)*70].rstrip())
            print(second_sequence[i*70:(i+1)*70].rstrip())

def print_alignment_matrix(matrix):
    for i in range(len(matrix)):
        if i == 0:
            for j in range(len(matrix[0])+1):
                print(str(j).zfill(4), end =" ")
            print()
        print(str(i+1).zfill(4), end =" ")
        for j in range(len(matrix[0])):
            print(str(matrix[i][j]).zfill(4), end =" ")
        print()