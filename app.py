from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "GIGANTIC AI is UP. Go to /pricing"

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)