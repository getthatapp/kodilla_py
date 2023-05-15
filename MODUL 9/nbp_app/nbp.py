from flask import Flask, request, render_template
import requests
import json
import csv

app = Flask(__name__)


@app.route('/save', methods=["GET"])
def save_csv():
    response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
    data = json.loads(response.text)
    rates = data[0]['rates']
    fields = ['currency', 'code', 'bid', 'ask']

    with open('rates.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fields, delimiter=';')
        writer.writeheader()
        for rate in rates:
            writer.writerow(rate)

    return "Plik poprawnie zapisany"


@app.route('/', methods=['GET', 'POST'])
def form():
    response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
    data = json.loads(response.text)
    rates = data[0]['rates']
    print(rates)
    if request.method == 'POST':
        currency_code = request.form.get('currency')
        amount = float(request.form.get('amount'))

        for rate in rates:
            if rate['code'] == currency_code:
                cost_pln = amount * rate['ask']
                return render_template('form.html', rates=rates, result=cost_pln, currency=currency_code, amount=amount)
    return render_template('form.html', rates=rates)


if __name__ == '__main__':
    app.run(debug=True)
