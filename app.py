# Loan Calculator, app.py
# Kimberly Souravong 02/23/2020

from flask import Flask
from flask import render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        form = request.form
        loan = float(form['loanAmount'])
        numPay = float(form['numPayments'])
        intRate = float(form['intRate'])

        #print(loan)
        #print(numPay)
        #print(intRate)

        A = loan
        n = numPay * 12
        i = intRate / 12
        D = (((1 + i)**n ) - 1 ) / ( i*(1 + i)**n)
        P = A/D 
        P = round(P,2)
        
        print(P)

    return render_template('index.html', pageTitle='Loan Calculator')
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
