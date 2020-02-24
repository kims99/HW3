# Loan Calculator, app.py
# Kimberly Souravong 02/23/2020

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', pageTitle='Flask Server Home Page')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
