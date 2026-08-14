from flask import Blueprint, render_template

payment_bp = Blueprint('payment', __name__)

@payment_bp.route('/settings')
def settings_home():
    return render_template('settings.html')