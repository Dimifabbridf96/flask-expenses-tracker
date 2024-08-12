from flask import Flask, render_template, url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from dataForm import Form, Salary
import json


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///expenses.db'
app.config['SECRET_KEY'] = "53LPSsRsJn"
db = SQLAlchemy(app)

from datetime import datetime

class ModelData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(100), nullable=False, default="Salary")
    date = db.Column(db.DateTime, nullable=False, default=datetime.now)
    type = db.Column(db.String(20), nullable=False, default="Income")
    
    def __repr__(self):
        return self.id


@app.route('/')
def index():
    expenses = ModelData.query.order_by(ModelData.date.desc()).all()
    return render_template('index.html', expenses=expenses)

@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/add', methods=["GET", 'POST'])
def add():
    form = Form()
    if form.validate_on_submit():
        new_expense = ModelData(amount=form.amount.data, category=form.category.data, type=form.type.data)
        db.session.add(new_expense)
        db.session.commit()
        flash('Expense added successfully!','sucess')  # Add flash message
        return redirect(url_for('index'))  # Redirect to index page
    return render_template('add.html', form=form )

@app.route('/delete/<int:expense_id>', methods=['GET'])
def delete(expense_id):
    expense = ModelData.query.get_or_404(int(expense_id))
    db.session.delete(expense)
    db.session.commit()
    flash('Expense deleted successfully!', 'danger')  # Add flash message
    return redirect(url_for('index'))  # Redirect to index page

@app.route('/update/<int:expense_id>', methods=['GET', 'POST'])
def update(expense_id):
    form = Form()
    expense = ModelData.query.get_or_404(int(expense_id))
    form.amount.data = expense.amount
    form.category.data = expense.category
    form.type.data = expense.type
    if request.method == 'POST':
        expense.amount = request.form['amount']
        expense.category = request.form['category']
        expense.type = request.form['type']  # Update the form data in the expense object
        try: # Add the expense to the session
            db.session.commit()
        except:
            db.session.rollback()  # Rollback the session if there is an error
            flash('There was an error updating the expense. Please try again.', 'danger')
        flash('Expense updated successfully!', 'success')  # Add flash message
        return redirect(url_for('index'))  # Redirect to index page
    return render_template('update.html', form=form)

@app.route('/charts', methods=['GET'])
def charts():
    income_vs_expenses = db.session.query(db.func.sum(ModelData.amount), ModelData.type).group_by(ModelData.type).order_by(ModelData.type).all()
    
    income_vs_expenses_category = db.session.query(db.func.sum(ModelData.amount), ModelData.type, ModelData.category).group_by(ModelData.type, ModelData.category).order_by(ModelData.category).all()
    
    expenses_on_dates = db.session.query(db.func.sum(ModelData.amount), ModelData.date).filter(ModelData.type == 'Expense').group_by(ModelData.date).order_by(ModelData.date).all()
    
    income_on_dates = db.session.query(db.func.sum(ModelData.amount), ModelData.date).filter(ModelData.type == 'Income').group_by(ModelData.date).order_by(ModelData.date).all()

    income_expense = []
    for total_income, _ in income_vs_expenses:
        income_expense.append(total_income)
    
    income_vs_expense_category = []
    type_label = []
    category_label = []
    
    for total_category, types, category in  income_vs_expenses_category:
        income_vs_expense_category.append(total_category)
        type_label.append(types)
        category_label.append(category)

    expense_amount = []
    dates_expense = []
    for total_expense_date, date_expense in expenses_on_dates:
        expense_amount.append(total_expense_date)
        dates_expense.append(date_expense.strftime("%m-%d-%y, %H:%M"))
        
    income_amount = []
    dates = []
    for total_date, date in income_on_dates:
        income_amount.append(total_date)
        dates.append(date.strftime("%m-%d-%y, %H:%M"))
        
    return render_template('charts.html', income_expenses_json = json.dumps(income_expense),
                           income_expense_category = json.dumps(income_vs_expense_category),
                           type_label = json.dumps(type_label),
                           category_label = json.dumps(category_label),
                           expense_amount = json.dumps(expense_amount),
                           dates_expense = json.dumps(dates_expense),
                           income_dates = json.dumps(income_amount),
                           dates_income = json.dumps(dates))
    
@app.route('/salary', methods = ['GET', 'POST'])
def salary():
    form = Salary()
    annual_income = monthly_income = weekly_income = hourly_income = daily_income = hours_per_day = None
    if form.validate_on_submit():
        salary = form.salary.data
        hours_per_day = form.hour.data
        if hours_per_day > 24:
            flash('Warning: Hours per day should not exceed 24.', 'warning')
        else:
            annual_income = salary
            monthly_income = "{:.2f}".format(annual_income / 12)
            daily_income = "{:.2f}".format(annual_income / 365)
            weekly_income = "{:.2f}".format(float(daily_income) * 7)
            hourly_income = "{:.2f}".format(float(daily_income) / hours_per_day)
            flash('Salary Calculated Successfully!','success')  # Add flash message
    return render_template('salary.html', form=form, annual_income=annual_income, monthly_income=monthly_income,
                           weekly_income=weekly_income, hourly_income=hourly_income, daily_income=daily_income)


if __name__ == '__main__':
    app.run(debug=True)