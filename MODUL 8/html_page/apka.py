from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/mypage/me')
def home():
    return render_template('home.html')


@app.route('/mypage/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        message = request.form.get('message')
        print('Wiadomość: ', message)

    return render_template('kontakt.html')


if __name__ == '__main__':
    app.run(debug=True)
