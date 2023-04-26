# def demo_function():
#     print("I'm inside!!!")
# demo_function()
#
# def add_numbers():
#     print(2 + 5)
# add_numbers()

# a = 1
# def scope_demo():
#     a = 2
#     print(a)
# scope_demo()
# print(a)

# def shopping():
#     shopping_items = [
#         "jajka",
#         "bułka",
#         "ser feta",
#         "masło",
#         "pomidor"
#     ]
#     shopping_cart = "Koszyk zawiera: "
#     for item in shopping_items:
#         shopping_cart += item + '\n'
#     return shopping_cart
# print(shopping())

# print(type(None))

# def day_types():
#     return "morning", "afternoon", "evening", "night"
# times = day_types()
# print(times)
# print(type(times))
#
# first, second, third, fourth = day_types()
# print("Trzeci element to %s" % third)

# def add(a, b):
#     print(a+b)
# add(44344533, 5665444)

# def customize_hello(first_name, last_name):
#     print("Hello Mr. %s %s" % (first_name, last_name))
# customize_hello("John", "Cleese")

# def customize_hello(first_name, last_name, gender_prefix='Mr'):
#     print(f"Hello {gender_prefix} {first_name} {last_name}")
# customize_hello("Anna", "Maria", "Ms")

# shopping_items = [
#     "jajka",
#     "bułka",
#     "ser feta",
#     "masło",
#     "pomidor"
# ]
# def shopping(items):
#     shopping_cart = "Koszyk zawiera: "
#     for item in items:
#         shopping_cart += item + '\n'
#     return shopping_cart
# shopping_items.append("chusteczki")
# shopping_items.append("papier toaletowy")
# basket = shopping(shopping_items)
# print(basket)
#
# shopping_items = [
#     "jajka",
#     "bułka",
#     "ser feta",
#     "masło",
#     "pomidor"
# ]
# def shopping(itens, payment='card', shop='local'):
#     pass
# shopping(shopping_items) #domyslne argumenty dla payment i shop (card i local)
# shopping(shopping_items, 'card', 'supermarket') #argumenty pozycyjne
# shopping(shopping_items, shop='supermarket') #argumenty po kluczu, payment domyslny (card)
#
# def shopping(items, *, payment='card', shop='local'): #gwiazdka oznacza, ze po niej przekazywane sa tylko argumenty nazwane, przez klucz-wartosc
#     pass
# #shopping(shopping_items, 'cash') #zwraca blad
#
# def name(positional_only_parameters, /, positional_or_keyword_parameters,
#          *, keyword_only_parameters): # / oddziela pozycyjne od standardowych a * od nazwanych
#     pass
# name(1,positional_or_keyword_parameters=2,keyword_only_parameters=3)
# name(1,2,keyword_only_parameters=3) #2 moze byc bo mozna podac zarowno pozycyjny jak i nazwany
#
# def count_them_all(*args): #argumenty pozycyjne trafia do listy ARGS
#     pass
#
# def count_them_all(*args, **kwargs):
#     positional_args_count = len(args)
#     named_kwargs_count = len(kwargs)
#     print(f'I have received {positional_args_count} positional arguments!')
#     print(f'I have received {named_kwargs_count} named arguments!')
# count_them_all(1, 2, 3, 'A', a=1, b=2)

### LAMBDA ###

shopping_items = [
    ("ziemniak", 2.5, 0.51),
    ("cebula", 3, 1.60),
    ("ser", 0.8, 15.50)
]

def get_index_1_tuple_element(given_tuple):
    return given_tuple[1]

# sorted_items = sorted(shopping_items, key=get_index_1_tuple_element)
# print(sorted_items)

sorted_items = sorted(shopping_items, key=lambda given_tuple: given_tuple[1])
print(sorted_items)