def print_mat(a):
    for i in range(len(a)):
        for j in range(len(a)):
            print(a[i][j], end=' ')
        print()

def matrix_to_graph(matrix):
    graph = []
    for i in range(len(matrix)):
        graph.append([])

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 1 and matrix[j][i] == 1:
                graph[i].append(j)
    return graph

def graph_to_matrix(graph_list):
    matrix = [[0 for j in range(len(graph_list))] for i in range(len(graph_list))]

    for i in range(len(graph_list)):
        for j in graph_list[i]:
            matrix[i][j] = 1
            matrix[j][i] = 1
