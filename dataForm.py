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
    salary = IntegerField("Annual Salary", validators=[DataRequired()])
    hour = IntegerField("Daily Hours", validators=[DataRequired()])
    relation = SelectField("Relation", validators=[DataRequired()],
                            choices=[('Single', 'Single'), ('Spouse 1 income', 'Spouse 1 income'), ('Spouse 2 income', 'Spouse 2 income'),
                                    ('Lone parent', 'Lone parent')])
    submit = SubmitField("Submit")
