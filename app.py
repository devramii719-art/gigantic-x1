from flask import Flask, render_template

# استيراد جميع الـ Blueprints المفروزة
from routes.auth import auth_bp
from routes.dashboard import dashboard_bp
from routes.leads import leads_bp
from routes.send import send_bp
from routes.payment import payment_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'gigantic-secret-key-2026'

# تسجيل المسارات
app.register_blueprint(auth_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(leads_bp)
app.register_blueprint(send_bp)
app.register_blueprint(payment_bp)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)