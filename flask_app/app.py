from flask import Flask, request, redirect, render_template

app = Flask(__name__)


@app.route('/hello')
def hello():
    my_name = "Johny"
    return f'Hello, {my_name}!'


@app.route('/blog')
def blog():
    return 'Welcome to my blog page'


@app.route('/blog/<id>')
def bloggo(id):
    return f'This blog entry #{id}'


# @app.route('/greetings')
# def greet():
#     return 'Welcome to my greeting page!'


@app.route('/message', methods=['GET', 'POST'])
def message():
    if request.method == 'GET':
        print('We received a GET request')
        return render_template('form.html')
    elif request.method == 'POST':
        print('We received a POST request')
        print(request.form)
        return redirect('/')


@app.route('/greeting', methods=['GET', 'POST'])
def greet():
    if request.method == 'GET':
        print('We received a GET request')
        return render_template('greeting.html')
    elif request.method == 'POST':
        print('We received a POST request')
        print(request.form)
        return redirect('/')
