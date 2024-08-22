from datetime import datetime
from flask import Blueprint, render_template, request, redirect, url_for
from .models import Purchase
from . import db


main = Blueprint('main', __name__)

@main.route('/')
def index():
    return redirect(url_for('main.add_purchase'))

@main.route('/add', methods=['GET', 'POST'])
def add_purchase():
    if request.method == 'POST':
        date_str = request.form['date']
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        farmer_name = request.form['farmer_name']
        location = request.form['location']
        quantity = float(request.form['quantity'])
        cost_per_kg = float(request.form['cost_per_kg'])
        total_cost = quantity * cost_per_kg
        payment_method = request.form['payment_method']

        new_purchase = Purchase(date=date, farmer_name=farmer_name, location=location,
                                quantity=quantity, cost_per_kg=cost_per_kg, total_cost=total_cost, payment_method=payment_method)
        db.session.add(new_purchase)
        db.session.commit()

        return redirect(url_for('main.view_records'))

    return render_template('form.html')

@main.route('/records')
def view_records():
    records = Purchase.query.all()
    return render_template('records.html', records=records)
