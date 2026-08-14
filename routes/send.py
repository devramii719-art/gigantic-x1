from flask import Blueprint, render_template

send_bp = Blueprint('send', __name__)

@send_bp.route('/')
def campaigns_home():
    return render_template('campaigns.html')