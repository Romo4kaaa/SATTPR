import numpy as np

K = 7
Lambda = 0.25
p = np.array([0.1, 0.2, 0.25, 0.35, 0.1])
# Платіжна матриця
Payment_matrix = np.array([[180, 140, 7  , 217, 232],
                           [420, 190, 140, 220, 100],
                           [81 , 315, 35 ,  49, 250],
                           [220,   7, 9  , 610, 201]])

Criterions = np.array([[180, 140, 7  , 217, 232 , 0.0],  # [6][0]
                       [420, 190, 140, 220, 100 , 0],  # [6][1]
                       [81 , 315, 35 ,  49, 250 , 0],  # [6][2]
                       [220,   7, 9  , 610, 201 , 0]])# [6][3]

row , col = Payment_matrix.shape
print("Платіжна матриця")
print(Payment_matrix)
print("Критерій песимізму")
for i in range(row):
 Criterions[i][5] = min(Payment_matrix[i])
print(Criterions)
print("Критерій оптимізму")
for i in range(row):
 Criterions[i][5] = max(Payment_matrix[i])
print(Criterions)
print("Критерій Баеса-Лапласа")
for i in range(row):
    Criterions[i][5] = (Payment_matrix[i][0] * p[0]) + (Payment_matrix[i][1] * p[1]) + (Payment_matrix[i][2] * p[2]) + (Payment_matrix[i][3] * p[3]) + (Payment_matrix[i][4] * p[4])
print(Criterions)
print("Критерій Гурвіца")
for i in range(row):
    Criterions[i][5] = (max(Payment_matrix[i]) * Lambda) + (min(Payment_matrix[i]) * (1 - Lambda))
print(Criterions)
print("Критерій Лапласа")
for i in range(row):
    Criterions[i][5] = sum(Payment_matrix[i]) / col
print(Criterions)
print("Критерій Холджа-Лемана")
for i in range(row):
    Criterions[i][5] = ((1 - Lambda) * min(Payment_matrix[i])) + (Lambda * ((Payment_matrix[i][0] * p[0]) + (Payment_matrix[i][1] * p[1]) + (Payment_matrix[i][2] * p[2]) + (Payment_matrix[i][3] * p[3]) + (Payment_matrix[i][4] * p[4])))
print(Criterions)
print("")