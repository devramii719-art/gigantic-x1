from flask import Blueprint, render_template, request, jsonify

payment_bp = Blueprint('payment', __name__)

@payment_bp.route('/settings', methods=['GET', 'POST'])
def settings_view():
    if request.method == 'POST':
        # استقبال طلب إنشاء فاتورة دفع جديدة عبر Cryptomus
        plan_type = request.form.get('plan', 'pro')
        
        # محاكاة رابط الدفع الوهمي (سيتم ربطه بـ API الحقيقي لـ Cryptomus لاحقاً)
        fake_payment_url = "https://pay.cryptomus.com/pay/sandbox-gigantic-invoice-123"
        
        return jsonify({
            "status": "success",
            "payment_url": fake_payment_url,
            "message": f"تم إنشاء رابط الدفع لباقة {plan_type} بنجاح!"
        })
        
    return render_template('settings.html')

@payment_bp.route('/payment/webhook', methods=['POST'])
def payment_webhook():
    # هذا المسار يستقبل الإشعار أوتوماتيكياً من Cryptomus كي يخلص العملاء
    webhook_data = request.json
    if webhook_data and webhook_data.get('status') == 'paid':
        # هنا يتم ترقية حساب المستخدم في قاعدة البيانات تلقائياً
        return jsonify({"status": "received", "action": "account_upgraded"})
        
    return jsonify({"status": "ignored"}), 400