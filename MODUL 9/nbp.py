import requests
import json
import csv

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = json.loads(response.text)

rates = data[0]['rates']
fields = ['currency', 'code', 'bid', 'ask']

with open('rates.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields,  delimiter=';')
    writer.writeheader()
    for rate in rates:
        writer.writerow(rate)

# print(rates)