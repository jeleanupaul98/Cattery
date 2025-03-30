from flask import Blueprint, render_template

contact_bp = Blueprint('contact', __name__)

@contact_bp.route('/contact')
def home():
    return render_template('contact.html', page_name = "Contacteaza-ne")