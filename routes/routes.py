from flask import Blueprint, render_template

routes_bp = Blueprint('routes', __name__)

@routes_bp.route('/dashboard')
def show_dashboard():
    return render_template('dashboard/main.html')