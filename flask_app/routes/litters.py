from flask import Blueprint, render_template

litters_bp = Blueprint('litters', __name__)

@litters_bp.route('/cuiburi')
def litters():
    return render_template('litters.html', page_name = "Cuiburi")