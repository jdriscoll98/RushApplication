from django import forms
from .models import Code, Rushee


class CodeForm(forms.Form):
    code = forms.IntegerField()

    def clean_code(self):
        data = super(CodeForm, self).clean()
        code = Code.objects.filter(pk=1).first()
        if data['code'] == code.code:
            return data
        else:
            print("error")
            raise forms.ValidationError("Invalid Code")


class RusheeForm(forms.ModelForm):
    class Meta:
        model = Rushee
        fields = ['name', 'phone_number', 'grade']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
        }
