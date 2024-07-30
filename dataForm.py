from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired

class Form(FlaskForm):
    amount = IntegerField("Amount",validators=[DataRequired()])
    type = SelectField("Type", validators=[DataRequired()],
                            choices=[('expense', 'expense'), ('income', 'income')])
    category = SelectField("Category", validators=[DataRequired()],
                           choices=[('rental', 'rental'), ('salary', 'salary'), ('shopping', 'shopping'),
                                    ('amusement', 'amusement'),('crypto', 'crypto'),('other', 'other')])
    submit =SubmitField("Submit")
    