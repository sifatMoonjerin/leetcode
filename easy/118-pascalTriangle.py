def generate(numRows):
    pascalTriangle = []

    if numRows == 0:
        return pascalTriangle

    for i in range(numRows):
        row = [1]*(i+1)
        for j in range(1, i):
            row[j] = pascalTriangle[i-1][j]+pascalTriangle[i-1][j-1]
        pascalTriangle.append(row)

    return pascalTriangle


print(generate(6))
