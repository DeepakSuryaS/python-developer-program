def lcs(s1, s2):
    # matrix creation
    mat = [["" for x in range(len(s2))] for x in range(len(s1))]
    print(mat)
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                if i == 0 or j == 0:
                    mat[i][j] = s1[i]
                else:
                    mat[i][j] = mat[i-1][j-1] + s1[i]
            else:
                mat[i][j] = max(mat[i-1][j], mat[i][j-1], key=len)

    comm_seq = mat[-1][-1]

    return len(comm_seq), comm_seq

print(lcs("ABCBDAB", "BDCABA"))  
