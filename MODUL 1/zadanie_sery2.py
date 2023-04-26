cheese_1 = "Roquefort"
price_cheese_1 = 12.50
cheese_1_weight = 2.0
cheese_2 = "Stilton"
price_cheese_2 = 11.24
cheese_2_weight = 1
cheese_3 = "Brie"
price_cheese_3 = 9.30
cheese_3_weight = 1
cheese_4 = "Gouda"
price_cheese_4 = 8.55
cheese_4_weight = 1
cheese_5 = "Edam"
price_cheese_5 = 11
cheese_5_weight = 1
cheese_6 = "Parmezan"
price_cheese_6 = 16.50
cheese_6_weight = 3.5
cheese_7 = "Mozzarella"
price_cheese_7 = 14
cheese_7_weight = 0.13
cheese_8 = "czechosłowacki ser z owczego mleka"
price_cheese_8 = 122.32
cheese_8_weight = 0.22
desert = "Listek miętowy"
desert_price = 20
desert_weight = 0.2

prices = (price_cheese_1*cheese_1_weight)+(price_cheese_2*cheese_2_weight)+(price_cheese_3*cheese_3_weight)+\
         (price_cheese_4*cheese_4_weight)+(price_cheese_5*cheese_5_weight)+(price_cheese_6*cheese_6_weight)+\
         (price_cheese_7*cheese_7_weight)+(price_cheese_8*cheese_8_weight)+(desert_price*desert_weight)

cheese_report = f"Raport z zakupów: " \
                f"Produkt: {cheese_1}, masa: {cheese_1_weight}kg, cena: {price_cheese_1 * cheese_1_weight}zł; " \
                f"Produkt: {cheese_2}, masa: {cheese_2_weight}kg, cena: {price_cheese_2 * cheese_2_weight}zł; " \
                f"Produkt: {cheese_3}, masa: {cheese_3_weight}kg, cena: {price_cheese_3 * cheese_3_weight}zł; " \
                f"Produkt: {cheese_4}, masa: {cheese_4_weight}kg, cena: {price_cheese_4 * cheese_4_weight}zł; " \
                f"Produkt: {cheese_5}, masa: {cheese_5_weight}kg, cena: {price_cheese_5 * cheese_5_weight}zł; " \
                f"Produkt: {cheese_6}, masa: {cheese_6_weight}kg, cena: {price_cheese_6 * cheese_6_weight}zł; " \
                f"Produkt: {cheese_7}, masa: {cheese_7_weight}kg, cena: {price_cheese_7 * cheese_7_weight}zł; " \
                f"Produkt: {cheese_8}, masa: {cheese_8_weight}kg, cena: {price_cheese_8 * cheese_8_weight}zł; " \
                f"Produkt: {desert}, masa: {desert_weight}kg, cena: {desert_price * desert_weight}zł; " \
                f"Suma zł: {prices}"
print(cheese_report)