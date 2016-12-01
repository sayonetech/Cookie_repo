from django import forms

class InputForm(forms.Form):
    """
    form for Entering the cookie to be processed
    """
    input = forms.CharField(max_length=1000, required=False,
                                 widget=forms.Textarea(attrs={'placeholder': 'Input Here',
                                                               'name': 'input',
                                                               'id': 'input',
                                                               }))
    output = forms.CharField(max_length=1000,required=False,
                                 widget=forms.Textarea(attrs={'placeholder': 'Formatted cookie here',
                                                               'name': 'output',
                                                               'id': 'output',
                                                               }))