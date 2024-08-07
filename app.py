from flask import Flask, render_template, url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from dataForm import Form



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///expenses.db'
app.config['SECRET_KEY'] = "53LPSsRsJn"
db = SQLAlchemy(app)

from datetime import datetime

class ModelData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(100), nullable=False, default="salary")
    date = db.Column(db.DateTime, nullable=False, default=datetime.now)
    type = db.Column(db.String(20), nullable=False, default="income")
    
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

if __name__ == '__main__':
    app.run(debug=True)