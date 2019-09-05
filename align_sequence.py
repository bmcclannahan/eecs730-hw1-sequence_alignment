
def align(seq1, seq2):
    matrix = [[0]*(len(seq2)+1) for i in range(len(seq1)+1)]
    for i in range(len(seq1)+1):
        for j in range(len(seq2)+1):
            if i == 0:
                matrix[i][j] = j
            elif j == 0:
                matrix[i][j] = i
            else:
                d = -2
                if seq1[i-1] == seq2[j-1]:
                    d = 1
                left = matrix[i-1][j] - 3
                up = matrix[i][j-1] - 3
                diag = matrix[i-1][j-1] + d
                matrix[i][j] = max([left,up,diag])
    return matrix

def print_alignment(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(str(matrix[i][j]).zfill(4), end =" ")
        print()