from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "GIGANTIC AI is UP. Go to /pricing"

@app.route('/pricing')
def pricing():
    return """
    <html><body style="background:#0a0a0a;color:#00ff88;text-align:center;font-family:Arial">
    <h1>Choose Your Plan</h1>
    <div style="border:2px solid #00ff88;border-radius:20px;padding:30px;margin:20px;display:inline-block">
        <h2>TRIAL</h2><h3>$0</h3><p>200 Emails</p>
    </div>
    <div style="border:2px solid #00ff88;border-radius:20px;padding:30px;margin:20px;display:inline-block">
        <h2>PRO</h2><h3>$79</h3><p>5000 Emails</p>
    </div>
    <div style="border:2px solid #00ff88;border-radius:20px;padding:30px;margin:20px;display:inline-block">
        <h2>AGENCY</h2><h3>$250</h3><p>Unlimited</p>
    </div>
    </body></html>
    """

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)