from flask import Blueprint, render_template, request, jsonify

leads_bp = Blueprint('leads', __name__)

@leads_bp.route('/leads', methods=['GET', 'POST'])
def leads_view():
    if request.method == 'POST':
        # هنا يتم معالجة طلب البحث المستهدف (سيتم ربطه بـ AI أو محرك الاستخراج لاحقاً)
        search_query = request.form.get('query', '')
        # بيانات وهمية مؤقتة للنتائج المعروضة فورياً
        dummy_results = [
            {"company": "Tech Solutions DZ", "email": "contact@techdz.com", "status": "متاح"},
            {"company": "Algiers Web Agency", "email": "info@algiersweb.com", "status": "متاح"},
        ]
        return jsonify({"status": "success", "results": dummy_results})
        
    return render_template('leads.html')