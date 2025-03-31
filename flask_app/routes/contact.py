from flask import Blueprint, render_template, request, redirect, url_for

contact_bp = Blueprint('contact', __name__)

# Route to display the contact form and handle the submission
@contact_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # You can process the form data here if needed
        # For now, we'll just redirect to the thank-you page
        return redirect(url_for('contact.thank_you'))
    return render_template('contact.html', page_name="Contacteaza-ne")

# Route for the Thank You page
@contact_bp.route('/thank-you')
def thank_you():
    return render_template('thank_you.html', page_name="Multumim!")  # render the thank you page template