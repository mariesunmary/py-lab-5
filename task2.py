рядки = 7
стовпці = 7

масив = []

# Заповнення масиву
for i in range(рядки, 0, -1):
    рядок = [i] * стовпці
    масив.append(рядок)

# Виведення масиву на екран
for рядок in масив:
    for елемент in рядок:
        print(елемент, end=' ')
    print()
