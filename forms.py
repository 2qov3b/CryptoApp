# forms.py

from wtforms import Form, SelectField, validators

class SearchForm(Form):
    choices = [(1, 'Q1'),
               (2, 'Q2'),
               (3, 'Q3'),
               (4, 'Q4')]
    select = SelectField('Search for questions:', choices=choices)
