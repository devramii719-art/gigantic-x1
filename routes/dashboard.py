from flask import Blueprint, render_template

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard')
def dashboard_view():
    # بيانات تجريبية عملاقة للوحة التحكم (يمكن ربطها بقاعدة البيانات لاحقاً)
    stats = {
        "total_revenue": 18450,
        "leads_used": 142,
        "leads_limit": 200,
        "active_campaigns": 5
    }
    return render_template('dashboard.html', stats=stats)