import numpy as np
Lambda = 0.4
# Початкова матриця
matrix = np.array([[43, 22, 42, 49, 45],
                   [41, 37, 40, 38, 42],
                   [39, 48, 37, 42, 36],
                   [37, 29, 32, 58, 41]])
Normalize = np.array([[0, 1,0,0.45,0,0],
                      [0.33333333, 0.42307692,0.2,1 ,0.33333333,0],
                      [0.66666667,0,0.5,0.8,1,0],
                      [1,0.73076923,1,0,0.44444444,0]])
matrix_valda = np.zeros((4, 6))
rows, cols = matrix.shape
Normalized_matrix = np.zeros((rows, cols))

# Нормалізація
for j in range(cols):  # Проходимо по кожному стовпцю
    col_min = np.min(matrix[:, j])  # Мінімальне значення у стовпці
    col_max = np.max(matrix[:, j])  # Максимальне значення у стовпці
    for i in range(rows):  # Проходимо по кожному рядку
        Normalized_matrix[i, j] = (col_max - matrix[i, j]) / (col_max - col_min)

# Виведення результату
print(Normalized_matrix)
print('')
for i in range(rows):
    Normalize[i][5] = min(Normalized_matrix[i])
print("Песимізм Вальда")
print(Normalize)
print("Критерій Оптимізму")
for i in range(rows):
    Normalize[i][5] = max(Normalized_matrix[i])
print(Normalize)
print("Критерій Лапласа")
for i in range(rows):
    Normalize[i][5] = sum(Normalized_matrix[i])/cols
print(Normalize)
print("Критерій Гурвіца")
for i in range(rows):
    Normalize[i][5] = (Lambda * max(Normalized_matrix[i])) + ((1-Lambda) * min(Normalized_matrix[i]))
print(Normalize)
# Критерій севіджа
rows, cols = Normalized_matrix.shape
for j in range(cols):  # Проходимо по кожному стовпцю
    col_min = np.min(Normalized_matrix[:, j])  # Мінімальне значення у стовпці
    col_max = np.max(Normalized_matrix[:, j])  # Максимальне значення у стовпці
    for i in range(rows):  # Проходимо по кожному рядку
        Normalize[i, j] = (col_max - Normalized_matrix[i, j])
for i in range(rows):
    Normalize[i][5] = 0
for i in range(rows):
    Normalize[i][5] = max(Normalize[i])
print("Критерій севіджа")
print(Normalize)