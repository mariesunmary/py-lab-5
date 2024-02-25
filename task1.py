def find_positiv_numbers(array):
    positive = []
    for number in array:
        if number > 0:
            positive.append(number)
    return positive

def main():
    length = int(input("Введіть довжину масиву: "))
    array = []
    for i in range(length):
        number = int(input("Введіть ціле число для масиву: "))
        array.append(number)
    positive_numbers = find_positiv_numbers(array)
    if positive_numbers:
        print("Позитивні елементи масиву:")
        for number in positive_numbers:
            print(number)
    else:
        print("У введеному масиві відсутні позитивні елементи.")

main()

