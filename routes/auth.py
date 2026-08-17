from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login_view():
    if request.method == 'POST':
        # استقبال بيانات الدخول من المستخدم
        email = request.form.get('email', '')
        password = request.form.get('password', '')
        
        # تحقق بسيط (سيتم ربطه بقاعدة البيانات والنظام الأمني لاحقاً)
        if email and password:
            session['user_email'] = email
            return jsonify({"status": "success", "redirect": "/dashboard"})
            
        return jsonify({"status": "error", "message": "الرجاء إدخال البريد وكلمة المرور بدقة!"}), 400
        
    return render_template('login.html')

@auth_bp.route('/logout')
def logout_view():
    # إنهاء جلسة المستخدم وتوجيهه لصفحة الدخول
    session.clear()
    return redirect(url_for('auth.login_view'))