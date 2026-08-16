from flask import Flask
from routes.pricing import pricing_bp
from routes.register import register_bp
from routes.webhook import webhook_bp  # زيد هذا

app = Flask(__name__)
app.register_blueprint(pricing_bp)
app.register_blueprint(register_bp)
app.register_blueprint(webhook_bp)  # وزيد هذا

if __name__ == '__main__':
    app.run(debug=True)