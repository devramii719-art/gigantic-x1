from flask import Blueprint, render_template

leads_bp = Blueprint('leads', __name__)

@leads_bp.route('/')
def leads_finder():
    return render_template('leads.html')