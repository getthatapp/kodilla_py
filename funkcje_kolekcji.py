# greet = "czesc, poskramiaczu lwow"
# print(dir(greet))

# my_list = list()
# print(dir(my_list))

# shopping_list = ["chleb", "mleko", "kasztany"]
# print(len(shopping_list))

# shopping_A = {"chleb", "wedlina", "mleko", "maslo"}
# shopping_B = {"cukier", "maka", "awokado", "maslo"}
# sets_sum = shopping_A | shopping_B
# print(sets_sum)
#
# sets_sum2 = shopping_A.union(shopping_B)
# print(sets_sum2)
#
# sets_multiplication = shopping_A & shopping_B
# print(sets_multiplication)
# sets_multiplication2 = shopping_A.intersection(shopping_B)
# print(sets_multiplication2)
#
# sets_difference = shopping_A - shopping_B
# print(sets_difference)
# sets_difference2 = shopping_A.difference(shopping_B)
# print(sets_difference2)

# shopping_dict = {
#     "warzywniak": ["buraki", "ziemniaki"],
#     "piekarnia": ["bułka", "chleb"]
# }
# print(shopping_dict.keys())
# print(shopping_dict.values())
# shopping_dict["papuga"]
# print(shopping_dict.get("papuga"))
# print(shopping_dict.get("warzywniak"))

# shopping_list = ["owoce", "maslo", "chleb"]
# print(shopping_list)
# shopping_list[2] = "chleb bezglutenowy"
# print(shopping_list)
# shopping_list.append("tunczyk")
# print(shopping_list)
# shopping_list = shopping_list + ["woda"]
# print(shopping_list)

# worldwide = ["polnoc", "poludnie"]
# print(worldwide)
# worldwide = worldwide + ["wschod"]
# print(worldwide)
# worldwide.append("zachod")
# print(worldwide)
# del worldwide[0]
# del worldwide[0]
# print(worldwide)
# worldwide.remove("zachod")
# print(worldwide)

# shopping_list = ["ryz", "buraki", "masło", "chleb"]
# sorted_shopping_list = sorted(shopping_list)
# print(f"Lista przed sortowaniem: {shopping_list}")
# print(f"Lista po sortowaniu: {sorted_shopping_list}")
#
# shopping_list.sort()
# print(f"Po kolejnym sortowaniu: {shopping_list}")

# numbers_list = [3, 6, 17, 4, 0, -20, 20, 100]
# sorted_numbers_list = sorted(numbers_list)
# print(sorted_numbers_list)
# numbers_list.sort()
# print(numbers_list)

# krotka = (1, 2, 3)
# del krotka[0]
# print(krotka)

# my_set = {1, 2, 4}
# print(f"Zestaw pierwotny: {my_set}")
# my_set.update({3})
# print(f"Po zmianach: {my_set}")

# my_week = {'pon', 'wto', 'sro', 'pia', 'sob', 'nie'}
# my_week.update({"czw"})
# print(my_week)

# salads = {
#     "owocowa": ["ananas", "truskawka", "jagody"],
#     "moja_buraczana": ["buraki", "ser kozi", "rukola"],
#     "mamina": ["groszek", "kukurydza", "majonez", "ziemniaki"]
# }
#
# print(salads["owocowa"])
#
# salads["miesna"] = ["szynka", "kurczak", "ryz", "ogorek"]
# print(salads.keys())
#
# salads["owocowa"].append("cukier")
# print(salads["owocowa"])
#
# print(salads.keys())
# del salads["mamina"]
# print(salads.keys())