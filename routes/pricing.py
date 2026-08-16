from flask import Blueprint, render_template

pricing_bp = Blueprint('pricing', __name__, url_prefix='/pricing')

@pricing_bp.route('/')
def show_pricing():
    plans = [
        {"name": "TRIAL", "price": "0", "currency": "$", "emails": "200 Emails", "features": ["Limited AI Leads"]},
        {"name": "PRO", "price": "79", "currency": "$ / month", "emails": "5000 Emails", "features": ["Full AI Leads", "AI Writer"]},
        {"name": "AGENCY", "price": "250", "currency": "$ / month", "emails": "Unlimited", "features": ["All AI Engines"]}
    ]
    return render_template('pricing.html', plans=plans)