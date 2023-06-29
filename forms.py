from django import forms


GUGUDAN_CHOICES = [
    ('2', '2단'),
    ('3', '3단'),
    ('4', '4단'),
    ('5', '5단'),
    ('6', '6단'),
    ('7', '7단'),
    ('8', '8단'),
    ('9', '9단'),
]


class GugudanForm(forms.Form):
    dan = forms.CharField(label="출력할 단", widget=forms.RadioSelect(choices=GUGUDAN_CHOICES))