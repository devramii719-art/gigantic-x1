from flask import Blueprint, render_template

interface_bp = Blueprint('interface', __name__)

@interface_bp.route('/dashboard')
def dashboard():
    return render_template('interface_main.html')