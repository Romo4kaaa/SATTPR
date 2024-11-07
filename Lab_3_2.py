import numpy as np


# Функція для розрахунку очікуваного доходу для кожного значення в таблиці
def calculate_expected_income(data, defect_limit):
    expected_incomes = []

    for row in data:
        defect_rate, probability = row[0], row[1]

        # Розрахунок штрафу та доплати
        fine = max(0, 1000 * (defect_rate - defect_limit) * 10)
        allowance = max(0, 500 * (defect_limit - defect_rate) * 10)

        # Розрахунок очікуваного доходу
        income = allowance - fine
        expected_incomes.append(income)

    return expected_incomes


# Функція для підрахунку загального очікуваного доходу
def calculate_total_income(data, expected_incomes):
    total_income = sum(row[1] * income for row, income in zip(data, expected_incomes))
    return total_income


# Вхідні дані для кожного споживача
consumer_A = np.array([[0.8, 0.4, 0, 0, 0],
                  [1, 0.3, 2000, 0, -2000],
                   [1.2, 0.25, 4000, 0, -4000],
                   [1.4, 0.05, 6000, 0, -6000]])

consumer_B = np.array([[0.8, 0.4, 0, 2000, 2000],
                       [1, 0.3, 0, 1000, 1000],
                       [1.2, 0.25, 0, 0, 0],
                       [1.4, 0.05, 2000, 0, -2000]])

consumer_C = np.array([[0.8, 0.4,  0, 3000, 3000],
                       [1  , 0.3,  0, 2000, 2000],
                       [1.2, 0.25, 0, 1000, 1000],
                       [1.4, 0.05, 0,    0,    0]])

# Ліміти браку для кожного споживача
defect_limits = {'A': 0.8, 'B': 1.2, 'C': 1.4}

# Розрахунок очікуваного чистого прибутку для кожного споживача
expected_incomes = {
    'A': calculate_expected_income(consumer_A, defect_limits['A']),
    'B': calculate_expected_income(consumer_B, defect_limits['B']),
    'C': calculate_expected_income(consumer_C, defect_limits['C'])
}

# Підрахунок повного доходу для кожного споживача
total_incomes = {
    'A': calculate_total_income(consumer_A, expected_incomes['A']),
    'B': calculate_total_income(consumer_B, expected_incomes['B']),
    'C': calculate_total_income(consumer_C, expected_incomes['C'])
}

# Виведення результатів
for consumer, income in total_incomes.items():
    print(f"Очікуваний чистий прибуток для альтернативи {consumer}: {income:.2f}")

# Визначення оптимального споживача для укладання контракту
optimal_consumer = max(total_incomes, key=total_incomes.get)
print(f"Найкраще заключити контракт зі Споживачем {optimal_consumer}")
