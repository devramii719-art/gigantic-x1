from flask import Blueprint, request, redirect
from services.cryptomus import create_payment

register_bp = Blueprint('register', __name__)

@register_bp.route('/register')
def register():
    plan = request.args.get('plan')
    prices = {"TRIAL": 0, "PRO": 79, "AGENCY": 250}
    amount = prices.get(plan, 0)
    if amount == 0: return "Trial Activated"
    payment_url = create_payment(amount, plan)
    return redirect(payment_url)