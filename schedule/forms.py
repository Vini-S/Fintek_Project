from django import forms
from schedule.models import Users



class UsersForm(forms.ModelForm):
	class Meta:
		model = Users
		fields = "__all__"
		widgets = {
		'password':forms.PasswordInput(),
					}

