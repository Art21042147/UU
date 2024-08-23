def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        graph = []
        for j in range(m):
            graph.append(value)
        matrix.append(graph)    
    return matrix


result1 = get_matrix(2, 5, 15)
result2 = get_matrix(4, 3, 41)
result3 = get_matrix(3, 6, 26)
print(result1)
print(result2)
print(result3)