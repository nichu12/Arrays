from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
@app.route('/register')
def home():
    return render_template('Home.html')

@app.route('/confirm',methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        n = request.form.get('name')
        n = request.form.get('name')

        return render_template('confirm.html', name=n)


if __name__ == "__main__":
    app.run(debug=True)
