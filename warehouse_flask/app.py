from flask import Flask, request, redirect, render_template

app = Flask(__name__)


@app.route('/warehouse')
def warehouse():
    items = ['screwdriver', 'hammer', 'saw']
    errors = ["Fakap!!!"]
    return render_template('warehouse.html', items=items, errors=errors)
