# Kardelen Gel - 181805057

number_of_elements = int(input("Please, enter the number of elements: "))
numbers = []

def bubbleSort(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers) - i -1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j + 1] = numbers[j + 1],numbers[j]

for i in range(number_of_elements):
    numbers.append(input())

bubbleSort(numbers)

print("Min number : " ,numbers[0])
print("Max number : " ,numbers[i])


