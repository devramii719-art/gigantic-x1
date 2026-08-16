from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "GIGANTIC AI is UP. Go to /pricing"

@app.route('/pricing')
def show_pricing():
    plans = [
        {"name": "TRIAL", "price": "0", "currency": "$", "emails": "200 Emails"},
        {"name": "PRO", "price": "79", "currency": "$ / month", "emails": "5000 Emails"},
        {"name": "AGENCY", "price": "250", "currency": "$ / month", "emails": "Unlimited"}
    ]
    return render_template('pricing.html', plans=plans)

if __name__ == '__main__':
    app.run(debug=True)