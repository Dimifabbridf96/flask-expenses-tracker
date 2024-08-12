from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired

class Form(FlaskForm):
    amount = IntegerField("Amount",validators=[DataRequired()])
    type = SelectField("Type", validators=[DataRequired()],
                            choices=[('Expense', 'Expense'), ('Income', 'Income')])
    category = SelectField("Category", validators=[DataRequired()],
                           choices=[('rental', 'Rental'), ('salary', 'Salary'), ('shopping', 'Shopping'),
                                    ('amusement', 'Amusement'),('crypto', 'Crypto'),('other', 'Other')])
    submit =SubmitField("Submit")

class Salary(FlaskForm):
    salary = IntegerField("Salary", validators=[DataRequired()])
    hour = IntegerField("Daily Hours", validators=[DataRequired()])
    submit = SubmitField("Submit")
