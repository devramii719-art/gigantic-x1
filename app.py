from flask import Flask, render_template
from routes import routes_bp  # الاستيراد المباشر من ملف routes.py تاعك

app = Flask(__name__)
app.config['SECRET_KEY'] = 'gigantic-secret-key-2026'

# تسجيل الـ Blueprint
app.register_blueprint(routes_bp)

@app.route('/')
def index():
    return render_template('dashboard/main.html')

if __name__ == '__main__':
    app.run(debug=True)