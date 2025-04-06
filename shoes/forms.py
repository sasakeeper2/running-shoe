from django import forms

class ShoeSearchForm(forms.Form):
    surface = forms.ChoiceField(choices=[
        ('road',   'Road'),
        ('trail',  'Trail'),
    ])
    foot_strike = forms.ChoiceField(choices=[
        ('midfoot', 'Midfoot'),
        ('heel',    'Heel'),
        ('forefoot','Forefoot'),
    ])
    cushioning = forms.ChoiceField(choices=[
        ('Medium', 'Medium'),
        ('Soft',   'Soft'),
        ('Plush',  'Plush'),
    ])
    pronation_support = forms.BooleanField(required=False)
