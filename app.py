from flask import Flask, render_template

# استيراد المسارات المفصولة اللي خدمناها
from routes.dashboard_route import dashboard_bp
from routes.pricing import pricing_bp
from routes.payment import payment_bp
from routes.language import language_bp
from routes.lead_finder import lead_finder_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'gigantic-secret-key-2026'

# تسجيل جميع المسارات (Blueprints) بدقة
app.register_blueprint(dashboard_bp)
app.register_blueprint(pricing_bp)
app.register_blueprint(payment_bp)
app.register_blueprint(language_bp)
app.register_blueprint(lead_finder_bp)

@app.route('/')
def index():
    # توجيه الصفحة الرئيسية مباشرة للوحة التحكم المقسمة اللي خدمناها
    return render_template('dashboard/main.html')

if __name__ == '__main__':
    app.run(debug=True)