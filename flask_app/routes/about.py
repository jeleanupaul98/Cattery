from flask import Blueprint, render_template

about_bp = Blueprint('about', __name__)

@about_bp.route('/despre')
def about():
    return render_template('about.html', page_name = "Despre Nobu's Friends")