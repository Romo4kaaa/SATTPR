import numpy as np

#
demand = np.array([
   [10, 15, 20],
])
# Ймовірності
Probability = np.array([
    0.3 , 0.6 , 0.1
])
# Закуп
purchase = np.array([
    [10 , 10 , 10],
    [15 , 15 , 15],
    [20 , 20 , 20]
])
# Продано
Sold = np.array([
    [10 , 10 , 10],
    [10 , 15 , 15],
    [10 , 15 , 20]
])
# Остаток
remainder = np.array([
    [0 , 0 , 0],
    [5 , 0 , 0],
    [10, 5 , 0]
])
# Незадоволений попит
unsatisfied_demand = np.array([
    [0 , 5 ,10],
    [0 , 0 , 5],
    [0 , 0 , 0]
])
# Чистий прибуток
net_profit = np.array([
    [0,0,0],
    [0,0,0],
    [0,0,0]
])
# Середній прибуток
average_profit = np.array([
    0,0,0
])

#Витрати
costs = 1500
#Загальний прибуток
total_profit = 2400

rows, cols = net_profit.shape

for i in range(rows):
    for j in range(cols):
        net_profit[i][j] =  (total_profit * Sold[i][j]) - (costs * purchase[i][j])

for i in range(rows):
    average_profit[i] = (net_profit[i][0] * Probability[0]) + (net_profit[i][1] * Probability[1]) + (net_profit[i][2] * Probability[2])

def main():
    print("Чистий прибуток")
    print(net_profit)
    print("Середній прибуток")
    print(average_profit)

main()