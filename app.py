from flask import Flask
from routes.pricing import pricing_bp
from routes.register import register_bp
from routes.webhook import webhook_bp

app = Flask(__name__)
app.register_blueprint(pricing_bp)  # هذا مهم
app.register_blueprint(register_bp)
app.register_blueprint(webhook_bp)

@app.route('/')
def home():
    return "GIGANTIC AI is UP. Go to /pricing"

if __name__ == '__main__':
    app.run(debug=True)