import numpy as np

expert_one_criteria = np.array([
   [1, 0.2, 5],
   [5, 1, 8],
   [0.2, 0.125, 1]
])

expert_two_criteria = np.array([
   [1, 0.25, 4],
   [4, 1, 8],
   [0.25, 0.125, 1]
])

k1_expert_one = np.array([
    [1, 4, 5],
    [0.25, 1, 2],
    [0.2, 0.5, 1]
])

k1_expert_two = np.array([
    [1, 5, 4],
    [0.2, 1, 0.25],
    [0.25, 4, 1]
])

k2_expert_one = np.array([
    [1, 2, 4],
    [0.5, 1, 4],
    [0.25, 0.25, 1]
])

k2_expert_two = np.array([
    [1, 2, 5],
    [0.5, 1, 4],
    [0.2, 0.25, 1]
])

k3_expert_one = np.array([
    [1, 0.5, 2],
    [2, 1, 5],
    [0.5, 0.2, 1]
])

k3_expert_two = np.array([
    [1, 0.25, 5],
    [4, 1, 8],
    [0.2, 0.125, 1]
])

def calculate_normalized_geometric_means(matrix):
    # Функція для обчислення середнього геометричного значення списку
    def geometric_mean(lst):
        product = np.prod(lst)
        geometric_mean = product ** (1 / len(lst))
        return geometric_mean

    # Обчислення середнього геометричного для кожного рядка
    geometric_means = [geometric_mean(row) for row in matrix]

    # Обчислення суми всіх середніх геометричних
    total_geometric_sum = sum(geometric_means)

    # Поділ середнього геометричного кожного рядка на суму всіх середніх геометричних
    normalized_geometric_means = [mean / total_geometric_sum for mean in geometric_means]

    return normalized_geometric_means

criteria_weights_expert_one = calculate_normalized_geometric_means(expert_one_criteria)
criteria_weights_expert_two = calculate_normalized_geometric_means(expert_two_criteria)

print("Ваги критеріїв (експерт 1):", np.array(criteria_weights_expert_one))
print("Ваги критеріїв (експерт 2):", np.array(criteria_weights_expert_two))

# Calculate the average priority of criteria between two experts
average_priority = [(w1 * w2) ** 0.5 for w1, w2 in zip(criteria_weights_expert_one, criteria_weights_expert_two)]

print("Середній пріоритет критеріїв:", np.array(average_priority))

k1_weights_expert_one = calculate_normalized_geometric_means(k1_expert_one)
k1_weights_expert_two = calculate_normalized_geometric_means(k1_expert_two)

print("Критерій 1 (експерт 1):", np.array(k1_weights_expert_one))
print("Критерій 1 (експерт 2):", np.array(k1_weights_expert_two))

max_weights_k1 = np.maximum(k1_weights_expert_one, k1_weights_expert_two)
print("Критерій 1:", max_weights_k1)

k2_weights_expert_one = calculate_normalized_geometric_means(k2_expert_one)
k2_weights_expert_two = calculate_normalized_geometric_means(k2_expert_two)

print("Критерій 2 (експерт 1):", np.array(k2_weights_expert_one))
print("Критерій 2 (експерт 2):", np.array(k2_weights_expert_two))

max_weights_k2 = np.maximum(k2_weights_expert_one, k2_weights_expert_two)
print("Критерій 2:", max_weights_k2)

k3_weights_expert_one = calculate_normalized_geometric_means(k3_expert_one)
k3_weights_expert_two = calculate_normalized_geometric_means(k3_expert_two)

print("Критерій 3 (експерт 1):", np.array(k3_weights_expert_one))
print("Критерій 3 (експерт 2):", np.array(k3_weights_expert_two))

max_weights_k3 = np.maximum(k3_weights_expert_one, k3_weights_expert_two)
print("Критерій 3:", max_weights_k3)

global_priorities3 = []
for i in range(len(max_weights_k1)):
    for j in range(len(max_weights_k1)):
        # Розраховуємо глобальний пріоритет для поточного ПК та додаємо його до рядка
        cell_value = max_weights_k1[i] * average_priority[0] + max_weights_k2[i] * average_priority[1] + max_weights_k3[i] * average_priority[2]
    global_priorities3.append(cell_value)
print("Глобальні пріоритети:", np.array(global_priorities3))

best_pc_index = np.argmax(global_priorities3)
print(f"Найкращі Навушники - Навушники{(best_pc_index + 1)} з глобальним пріорітетом: {global_priorities3[best_pc_index]}")