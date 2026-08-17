from flask import Flask, render_template
import os

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

# استدعاء الـ blueprints بالاسم الصحيح
from routes.auth import auth_bp
from routes.dashboard import bp as dashboard_bp
from routes.leads import leads_bp
from routes.send import send_bp
from routes.payment import payment_bp

app.register_blueprint(auth_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(leads_bp)
app.register_blueprint(send_bp)
app.register_blueprint(payment_bp)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)