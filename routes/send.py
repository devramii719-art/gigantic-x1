from flask import Blueprint, render_template, request, jsonify

send_bp = Blueprint('send', __name__)

@send_bp.route('/campaigns', methods=['GET', 'POST'])
def campaigns_view():
    if request.method == 'POST':
        # استقبال بيانات الحملة الجديدة (الموضوع، المحتوى، والهدف)
        campaign_title = request.form.get('title', '')
        target_audience = request.form.get('audience', '')
        
        # محاكاة عملية إطلاق الحملة بنجاح
        return jsonify({
            "status": "success",
            "message": f"تم إطلاق الحملة '{campaign_title}' بنجاح وإرسالها للعملاء المستهدفين!"
        })
        
    return render_template('campaigns.html')