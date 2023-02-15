# Użyj listy składanej, aby stworzyć listę sześcianów (potęgi trzeciej) liczb z zakresu od 1 do 10.
# Następnie użyj pętli for in, aby zwrócić w konsoli liczby niepodzielne przez 2.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
three_numbers = []
something = [three_numbers.append(number*number*number) for number in numbers]
print(three_numbers)

not_three = []
for number in three_numbers:
    if number % 2 != 0:
        not_three.append(number)
print(not_three)

# Dana jest lista: [2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 3, 0, 0].
# Zadeklaruj ją w Pythonie, a następnie użyj slicingu, by otrzymać listę, która zawiera tylko zera z tej kolekcji.
# Potem użyj tej samej techniki do zwrócenia listy, która zawiera wszystkie inne liczby tylko nie zera z tej kolekcji.

lst = [2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 3, 0, 0]
print(lst[1:4]+lst[5:10]+lst[-2:])
print(lst[0:1] + lst[4:5] + lst[10:12])