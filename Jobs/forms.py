from django import forms
from .models import Jobs,Dept,Status,Job_type


class Dept_Form(forms.ModelForm):
    class Meta:
        model = Dept
        fields ='__all__'
class Type_Form(forms.ModelForm):
    class Meta:
        model = Job_type
        fields ='__all__'
class Status_Form(forms.ModelForm):
    class Meta:
        model = Status
        fields ='__all__'

class Jobs_Form(forms.ModelForm):
    class Meta:
        model = Jobs
        fields ='__all__'




        widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'dept': forms.TextInput(attrs={'class': 'form-control'}),
			'job_location': forms.TextInput(attrs={'class': 'form-control'}),
			'vacancy': forms.TextInput(attrs={'class': 'form-control'}),
			'exp': forms.TextInput(attrs={'class': 'form-control'}),
			'salary_from': forms.TextInput(attrs={'class': 'form-control'}),
			'salary_to': forms.TextInput(attrs={'class': 'form-control'}),
			'job_type': forms.TextInput(attrs={'class': 'form-control'}),
			'status': forms.TextInput(attrs={'class': 'form-control'}),
			'start_date': forms.TextInput(attrs={'class': 'form-control'}),
			'end_date': forms.TextInput(attrs={'class': 'form-control'}),
			'desc': forms.TextInput(attrs={'class': 'form-control'}),
			'skill': forms.TextInput(attrs={'class': 'form-control'}),
		}