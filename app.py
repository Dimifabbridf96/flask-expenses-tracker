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
    return render_template('index.html')

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
        flash('Expense added successfully!')  # Add flash message
        return redirect(url_for('index'))  # Redirect to index page
    return render_template('add.html', form=form )

if __name__ == '__main__':
    app.run(debug=True)