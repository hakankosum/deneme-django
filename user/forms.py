from django import forms

class registerForm(forms.Form):
    username = forms.CharField(max_length=25,label="User name")
    password = forms.CharField(max_length=25,label="Password",widget=forms.PasswordInput)
    confirm=forms.CharField(max_length=25,label="Confirm your password",widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")
        if password and confirm and password != confirm :
            raise forms.ValidationError("Password does not match.")
        values = {
            "username":username,
            "password":password
        }
        return values
class loginForm(forms.Form):
    username = forms.CharField(max_length=25,label="User name")
    password = forms.CharField(max_length=25,label="Password",widget=forms.PasswordInput)
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        values = {
        "username":username,
        "password":password
        }
        return values