"""
Данный модуль демонстрирует преимущества работы с массивами данных, показывая насколько проще и
эффективней было бы выполнение задачи "Матрица воплоти" из module_2_5 с применением numpy.
"""

import numpy as np
from time import time

start_py = time()


def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        graph = []
        for j in range(m):
            graph.append(value)
        matrix.append(graph)
    return matrix


get_matrix(5000, 5000, 5000)

end_py = time()

start_np = time()


def np_matrix(n, m, value):
    matrix = np.full((n, m), value)
    return matrix


np_matrix(5000, 5000, 5000)

end_np = time()

print(f'Время работы get_matrix: {end_py - start_py:.6f} сек.\n'
      f'Время работы np_matrix: {end_np - start_np:.6f} сек.')
