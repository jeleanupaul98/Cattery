from flask import Blueprint, render_template, request, redirect, url_for

contact_bp = Blueprint('contact', __name__)

@contact_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        return redirect(url_for('contact.thank_you'))
    return render_template('contact.html', page_name="Contacteaza-ne")

@contact_bp.route('/thank-you')
def thank_you():
    return render_template('thank_you.html', page_name="Multumim!")