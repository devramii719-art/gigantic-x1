from flask import Blueprint, render_template, request

payment_bp = Blueprint('payment', __name__)

@payment_bp.route('/payment')
def payment_page():
    selected_plan = request.args.get('plan', 'trial')
    
    # الأسعار بالدولار فقط
    prices = {
        'trial': {'name': 'Trial (تجريبي)', 'amount': '$0'},
        'pro': {'name': 'Pro (محترف)', 'amount': '$79'},
        'agency': {'name': 'Agency (وكالة)', 'amount': '$250'}
    }
    
    plan_info = prices.get(selected_plan, prices['trial'])
    
    return render_template('payment.html', plan=plan_info)

@payment_bp.route('/process-payment', methods=['POST'])
def process_payment():
    payment_method = request.form.get('method')
    plan_name = request.form.get('plan')
    return f"Redirecting to Cryptomus payment gateway for plan: {plan_name} via {payment_method} 🚀"