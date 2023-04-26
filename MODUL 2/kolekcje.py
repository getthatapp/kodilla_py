################### KOLEKCJE ######################

#my_list = list()

# my_list = []
#
# print(type(my_list))
#
# print(bool(my_list))

# for i in range(0, 5):
#     print(i)

# my_list = [0,1,2,3,4]
# for i in my_list:
#     print(i)

# sentence = ["Zacznij", "kodować", "z", "Kodillą"]
# for word in sentence:
#     print(word)

# tasty_coctail = [1, "mydło", None, "powidło", 0.1]
# print(tasty_coctail)

# shopping_list = ["mielonka", "jajka", "boczek"]
# print(shopping_list)
# shopping_list.append("woda")
# print(shopping_list)

# my_list = ["koty", 2.0, "netflix", None]
# for word in my_list:
#     print(word)

# shopping_list = ["mielonka", "jajka", "boczek"]
# print(f"Pierwszy element listy to: {shopping_list[0]}")
# print(f"Trzeci element listy to: {shopping_list[2]}")


################### KROTKA/TUPLE ######################

# days = ("pon", "wt", "sr", "czw")
# print(type(days))
#
# days = tuple(["pon", "wt", "sr", "czw"])
# print(type(days))

################### ZBIOR/SET ######################

# my_set = set([1,2,3])
# print(type(my_set))
# my_set2 = {1,2,3}
# print(type(my_set2))
# my_set3 = {1,4,3,4,4,5}
# print(my_set3)

################### SLOWNIK/DICT ######################

# my_dictionary = {
#     "key1": "value1",
#     "key2": "value2",
#     "key3": "value3"
# }
# print(my_dictionary)

# my_dictionary2 = dict((("key1", "value1"), ("key2", "value2"), ("key3", "value3")))
# print(my_dictionary2)

shopping_dict = {
    "warzywniak": ["buraki", "ziemniaki"],
    "piekarnia": ["bulka", "chleb"]
}
print("Wchodzę do warzywniaka")
print(shopping_dict["warzywniak"])