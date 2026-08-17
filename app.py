from flask import Flask, render_template
import os
from routes import auth, dashboard, leads, send, payment

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key')

app.register_blueprint(auth.bp)
app.register_blueprint(dashboard.bp)
app.register_blueprint(leads.bp)
app.register_blueprint(send.bp)
app.register_blueprint(payment.bp)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)