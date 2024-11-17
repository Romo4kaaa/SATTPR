import numpy as np
from numpy.ma.core import minimum

K = 7
a = 0.25
p = np.array([0.1, 0.2, 0.25, 0.35, 0.1])
# Платіжна матриця
Payment_matrix = np.array([[180, 140, 7  , 217, 232],
                           [420, 190, 140, 220, 100],
                           [81 , 315, 35 ,  49, 250],
                           [220,   7, 9  , 610, 201]])
# Критерій песимізму
Criterion_pessimism = np.array([[180, 140, 7  , 217, 232 , 0], # [6][0]
                                [420, 190, 140, 220, 100 , 0], # [6][1]
                                [81 , 315, 35 ,  49, 250 , 0], # [6][2]
                                [220,   7, 9  , 610, 201 , 0]])# [6][3]
# Критерій оптимізму
Criterion_optimism = np.array([[180, 140, 7  , 217, 232 , 0], # [6][0]
                               [420, 190, 140, 220, 100 , 0], # [6][1]
                               [81 , 315, 35 ,  49, 250 , 0], # [6][2]
                               [220,   7, 9  , 610, 201 , 0]])# [6][3]
# Критерій Баеса-Лапласа
Criterion_BaesLaplas = np.array([[180, 140, 7  , 217, 232 , 0.0], # [6][0]
                                 [420, 190, 140, 220, 100 , 0], # [6][1]
                                 [81 , 315, 35 ,  49, 250 , 0], # [6][2]
                                 [220,   7, 9  , 610, 201 , 0]])# [6][3]
# Критерій Гурвіца
Criterion_Gurvitsa = np.array([[180, 140, 7  , 217, 232 , 0.0], # [6][0]
                                 [420, 190, 140, 220, 100 , 0], # [6][1]
                                 [81 , 315, 35 ,  49, 250 , 0], # [6][2]
                                 [220,   7, 9  , 610, 201 , 0]])# [6][3]
# Критерій Лапласа
Criterion_Laplasa = np.array([[180, 140, 7  , 217, 232 , 0.0], # [6][0]
                                 [420, 190, 140, 220, 100 , 0], # [6][1]
                                 [81 , 315, 35 ,  49, 250 , 0], # [6][2]
                                 [220,   7, 9  , 610, 201 , 0]])# [6][3]
# Критерій Холджа-Лемана
Criterion_Hodja_Lemana = np.array([[180, 140, 7  , 217, 232 , 0.0], # [6][0]
                                 [420, 190, 140, 220, 100 , 0], # [6][1]
                                 [81 , 315, 35 ,  49, 250 , 0], # [6][2]
                                 [220,   7, 9  , 610, 201 , 0]])# [6][3]
row , col = Payment_matrix.shape
print("Платіжна матриця")
print(Payment_matrix)
print("Критерій песимізму")
for i in range(row):
 Criterion_pessimism[i][5] = min(Payment_matrix[i])
print(Criterion_pessimism)
print("Критерій оптимізму")
for i in range(row):
 Criterion_optimism[i][5] = max(Payment_matrix[i])
print(Criterion_optimism)
print("Критерій Баеса-Лапласа")
for i in range(row):
    Criterion_BaesLaplas[i][5] = (Payment_matrix[i][0]*p[0])+(Payment_matrix[i][1]*p[1])+(Payment_matrix[i][2]*p[2])+(Payment_matrix[i][3]*p[3])+(Payment_matrix[i][4]*p[4])
print(Criterion_BaesLaplas)
print("Критерій Гурвіца")
for i in range(row):
    Criterion_Gurvitsa[i][5] = (max(Payment_matrix[i])*a)+(min(Payment_matrix[i])*(1-a))
print(Criterion_Gurvitsa)
print("Критерій Лапласа")
for i in range(row):
    Criterion_Laplasa[i][5] = sum(Payment_matrix[i])/5
print(Criterion_Laplasa)
print("Критерій Холджа-Лемана")
for i in range(row):
    Criterion_Hodja_Lemana[i][5] = ((1-a)*min(Payment_matrix[i]))+(a*((Payment_matrix[i][0]*p[0])+(Payment_matrix[i][1]*p[1])+(Payment_matrix[i][2]*p[2])+(Payment_matrix[i][3]*p[3])+(Payment_matrix[i][4]*p[4])))
print(Criterion_Hodja_Lemana)
print("")