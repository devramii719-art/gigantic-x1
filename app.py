from flask import Flask, render_template
import os
from dotenv import load_dotenv

# تحميل المتغيرات السرية من ملف .env
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'gigantic-secret-key')

# استيراد وتسجيل الـ Routes (كل خاصية وحدها في ملفها)
from routes.auth import auth_bp
from routes.dashboard import dashboard_bp
from routes.leads import leads_bp
from routes.send import send_bp
from routes.payment import payment_bp

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(dashboard_bp, url_prefix='/dashboard')
app.register_blueprint(leads_bp, url_prefix='/leads')
app.register_blueprint(send_bp, url_prefix='/send')
app.register_blueprint(payment_bp, url_prefix='/payment')

# الصفحة الرئيسية للمنصة
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)