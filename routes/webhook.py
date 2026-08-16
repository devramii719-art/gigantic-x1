from flask import Blueprint, request, jsonify
from services.subscription import activate_subscription

webhook_bp = Blueprint('webhook', __name__)

@webhook_bp.route('/webhook', methods=['POST'])
def cryptomus_webhook():
    data = request.get_json()
    
    if data.get('status') == 'paid':
        order_id = data.get('order_id')  # PRO or AGENCY
        user_email = data.get('email')
        
        activate_subscription(user_email, order_id)
        return jsonify({"status": "ok"}), 200
    
    return jsonify({"status": "failed"}), 400