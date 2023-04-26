import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename='logfile_calc.txt')

choice = input('Podaj działanie, posługując się odpowiednią liczbą: [1] Dodawanie, [2] Odejmowanie, [3] Mnożenie, [4] Dzielenie: ')
if choice == '1':
    num1 = float(input("Podaj pierwszą liczbę: "))
    num2 = float(input("Podaj drugą liczbę: "))
    score = num1 + num2
    logging.info('Wynik:', score)
elif choice == '2':
    num1 = float(input("Podaj pierwszą liczbę: "))
    num2 = float(input("Podaj drugą liczbę: "))
    score = num1 - num2
    logging.info('Wynik:', score)
elif choice == '3':
    num1 = float(input("Podaj pierwszą liczbę: "))
    num2 = float(input("Podaj drugą liczbę: "))
    score = num1 * num2
    logging.info('Wynik:', score)
elif choice == '4':
    num1 = float(input("Podaj pierwszą liczbę: "))
    num2 = float(input("Podaj drugą liczbę: "))
    score = num1 / num2
    logging.info('Wynik:', score)
else:
    exit(1)

if __name__ == '__main__':
    logging.info('Oto wynik działania: %s' % score)