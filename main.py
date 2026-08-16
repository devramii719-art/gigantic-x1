from flask import Flask

app = Flask(__name__)

@app.route('/pricing')
def pricing():
    return '''<!DOCTYPE html><html><head><style>body{background:#0a0a0a;color:#fff;text-align:center;font-family:Arial;padding:50px}.plan{background:#1a1a1a;border:2px solid #00ff88;border-radius:20px;padding:30px;margin:20px;display:inline-block;width:300px}.price{font-size:48px;color:#00ff88}</style></head><body><h1>GIGANTIC AI PRICING</h1><div class="plan"><h2>TRIAL</h2><div class="price">$0</div><p>200 Emails</p></div><div class="plan"><h2>PRO</h2><div class="price">$79</div><p>5000 Emails</p></div><div class="plan"><h2>AGENCY</h2><div class="price">$250</div><p>Unlimited</p></div></body></html>'''

if __name__ == '__main__':
    app.run()