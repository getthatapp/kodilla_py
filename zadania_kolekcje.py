### ZADANIE 1 ###
name_list = ["John", "Michael", "Terry", "Eric", "Graham"]
print(name_list)

name_dictionary = {
    "name1": "John",
    "name2": "Michael",
    "name3": "Terry",
    "name4": "Eric",
    "name5": "Graham"
}
values = name_dictionary.values()
for value in list(values):
    print(f"Dlugosc imienia {value} wynosi {len(value)}")

### ZADANIE 2 ###

numbers = [1, 2, 3, 5, 6, 11, 12, 18, 19, 21]
primes = []
for i in numbers:
    counter = 0
    for j in range(1, i):
        if i % j == 0:
            counter += 1
    if counter == 1:
        primes.append(i)
print(primes)

### ZADANIE 3 ###

days = ['pon','śro','pią','sob']
days.insert(1, "wt")
days.insert(3, "czw")
days.append("niedz")
print(days)

### ZADANIE 4 ###
herbata = ["włącz czajnik", "znajdź opakowanie herbaty", "zalej herbatę", "nalej wody do czajnika", "wyjmij kubek", "włóż herbatę do kubka"]
order = [1, 4, 5, 3, 0, 2]
zrob_herbate = [herbata[i] for i in order]
print(zrob_herbate)
