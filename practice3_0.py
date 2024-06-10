import random
import statistics

numbers = [random.randint(1, 100) for _ in range(10)]

print("Список чисел:", numbers)

sum_numbers = sum(numbers)
print("Сумма чисел:", sum_numbers)

mean_numbers = statistics.mean(numbers)
print("Среднее значение:", mean_numbers)

median_numbers = statistics.median(numbers)
print("Медиана:", median_numbers)

stdev_numbers = statistics.stdev(numbers)
print("Стандартное отклонение:", stdev_numbers)

random_choice = random.choice(numbers)
print("Случайное число из списка:", random_choice)


random_sample = random.sample(numbers, 3)
print("Случайная выборка из списка:", random_sample)