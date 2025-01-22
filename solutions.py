#### E 1.5 List slicing

# 1. Skapa en lista som innehåller numren 1 till 10.
# 2. Använd list slicing för att skriva ut de första fem numren.
# 3. Använd list slicing för att skriva ut de sista fyra numren.
# 4. Skriv ut varannat nummer i listan, börjande med det första.
# 5. Skapa en ny lista som är en kopia av den omvända originallistan.

print("----------------------------------------------------------------------------------------------")
my_number_list = list(range(1, 11))
print(my_number_list)
# my_number_list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(my_number_list_2)

sublist1 = my_number_list[:5]
print(f" Our first slice is the first 5 numbers: {sublist1}")

sublist2 = my_number_list[5:]
print(f" Our second slice is the last 5 numbers: {sublist2}")

sublist_everyother = my_number_list[::2]
print(f" Our third slice includes every other numbebr in the list: {sublist_everyother}")

sublist_revered = my_number_list[::-1]
print(f" Our forth slice is the reveresed list using slicing symbols: {sublist_revered}")

print("----------------------------------------------------------------------------------------------")

#### 1.6 Minst och störst
# 1. Skapar en lista med 10 slumpmässiga heltal.
# 2. Letar reda på en inbyggd funktion för att hitta det största talet.
# 3. Letar reda på en funktion för att hitta det minsta talet.
# 4. Hittar summan av alla tal i listan.
# 5. Sorterar listan från lägst till högst.

import random
random_integers = [random.randint(1, 100) for _ in range(10)]
print("Random Integer list of ten:", random_integers)

largest_number = max(random_integers)
print("The largest number in the list is:", largest_number)

smallest_number = min(random_integers)
print("The smallest number in the list is:", smallest_number)

total_sum = sum(random_integers)
print("The sum of all numbers in the list is:", total_sum)

random_integers.sort()  # sort() Method
print("Sorted list from lowest to highest is :", random_integers)
sorted_integers = sorted(random_integers) # sorted () Function
print("Sorted list from lowest to highest is :", sorted_integers)

random_integers.sort(reverse=True)  # sort(reverese=True) Method
print("Sorted list from lowest to highest is :", random_integers)
sorted_integers = sorted(random_integers, reverse=True) # sorted (list, reverese=True) Function
print("Sorted list from lowest to highest is :", sorted_integers)

print("----------------------------------------------------------------------------------------------")

#### 1.7 Kombinera listor
# Skapa en funktion som tar två listor med heltal som argument och returnerar en kombinerad och sorterad lista av dessa.
# Creating two lists of integers

list1 = list(range(1, 6))
list2 = list(range(6, 11))
print("list1 is: ", list1)
print("list2 is: ", list2)

def combining_list_funcion(list1, list2):
    combined_list = list1 + list2
    sorted_combined_list = sorted(combined_list)
    print("The combined and sorted list is: ", sorted_combined_list)

combining_list_funcion(list1, list2)

print("----------------------------------------------------------------------------------------------")

#### 1.8 Jämna tal i listor
# Skapa en funktion som tar in en lista med helt som argument, och returnerar hur många jämna tal det finns i listan.

import random

def counting_evennumbers_function(numbers):
    even_count = sum(1 for num in numbers if num % 2 == 0)
    print("Number of even numbers in the list:", even_count)

random_integers = [random.randint(1, 100) for _ in range(20)]
print("List of 20 random integers:", random_integers)

counting_evennumbers_function(random_integers)

print("----------------------------------------------------------------------------------------------")

#### 1.9 Summan av två listor
# Skapa en funktion som tar in två lika långa listor som argument. Returnera en lista där varje element är summan av de två listornas respektive element.

def twolistsSum_function(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Both lists must be of the same length")
    summed_list = [a + b for a, b in zip(list1, list2)]
    return summed_list

# Example usage
list1 = [0, 1, 1, 2, 3]
list2 = [5, 8, 13, 21, 34]
print("List 1 is: ", list1)
print("List 1 is: ", list2)

result = twolistsSum_function(list1, list2)
print("Summed list:", result)


print("----------------------------------------------------------------------------------------------")