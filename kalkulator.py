choice = input('Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ')
def calculator(a, b):
    if choice == 1:
        score = a + b
    elif choice == 2:
        score = a - b
    elif choice == 3:
        score = a * b
    elif choice == 4:
        score = a / b
    else:
        exit(1)

