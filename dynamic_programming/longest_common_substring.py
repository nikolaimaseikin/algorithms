def longest_common_substring(str1: str, str2: str) -> int:
    solution_table = [[0 for i in range(len(str2))] for i in range(len(str1))]
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                solution_table[i][j] =  solution_table[i-1][j-1] + 1
    return solution_table

solution_table = longest_common_substring('fish','hish')
for row in solution_table:
    for col in row:
        print(col, end=" ")
    print()

