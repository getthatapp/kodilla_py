# def shopping(items, payment='card', shop='local'):
#     result = ""
#     result = result + "Idę na zakupy do %s .\n" % shop
#     result = result + "Kupię następujące rzeczy: \n"
#     for item in items:
#         result = result + " - %s\n" % item
#     result = result + "By zapłacić, używam %s." % payment
#     return result
#
# if __name__ == "__main__":
#     items_text = input("Podaj produkty rozdzielone przecinkiem: ")
#     items = items_text.split(',')
#     shopping_result = shopping(items)
#     print(shopping_result)

# name = input('Podaj imie i nazwisko: ')
# # print(f"Witaj {name}")

print('Witaj, ten program pomoże Ci sprawdzić czy jesteś pełnoletni/a')
adult = None
sex = input('Podaj swoją płeć [K/M]: ')
if sex == 'M':
    age = int(input("Twój wiek? "))
    adult = age >= 18
elif sex == 'K':
    print('Kobiet o wiek się nie pyta, więc spytamn delikatnie')
    over18_yesno = input('Czy miałaś już osiemnastkę? [T/N] ')
    adult = (over18_yesno == 'T')
else:
    print('Nie ma takiej płci!')
    exit(1)
print('Już wiem. Twoja pełnoletniość w boolean to %s' % str(adult))