from flask import Flask, render_template_string

app = Flask(__name__)

HTML = '''<!DOCTYPE html>
<html><head><title>Pricing</title><style>body{background:#0a0a0a;color:#fff;text-align:center;font-family:Arial}.plan{background:#1a1a1a;border:2px solid #00ff88;border-radius:20px;padding:30px;margin:20px;display:inline-block;width:300px}.price{font-size:48px;color:#00ff88}.btn{background:#00ff88;color:#000;padding:15px 40px;border-radius:10px;text-decoration:none;font-weight:bold}</style></head>
<body><h1>Choose Your Plan</h1>
<div class="plan"><h2>TRIAL</h2><div class="price">$0</div><p>200 Emails</p><a href="#" class="btn">Start Now</a></div>
<div class="plan"><h2>PRO</h2><div class="price">$79</div><p>5000 Emails</p><a href="#" class="btn">Start Now</a></div>
<div class="plan"><h2>AGENCY</h2><div class="price">$250</div><p>Unlimited</p><a href="#" class="btn">Start Now</a></div>
</body></html>'''

@app.route('/')
def home():
    return "GIGANTIC AI is UP. Go to /pricing"

@app.route('/pricing')
def pricing():
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run()