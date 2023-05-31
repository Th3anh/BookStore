from django import forms
import re
from .models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm

class CustomNameInput(forms.TextInput):
    def __init__(self, *args, **kwargs):
        attrs = kwargs.setdefault('attrs', {})
        attrs.update({
            'placeholder': 'Nhập Tên',
            'class': 'form-control form-control-lg',
            'required': True,
            'data-validation': 'required',
            'data-validation-error-msg': 'Không được để trống',
        })
        super().__init__(*args, **kwargs)

class CustomEmailInput(forms.EmailInput):
    def __init__(self, *args, **kwargs):
        attrs = kwargs.setdefault('attrs', {})
        attrs.update({
            'placeholder': 'Nhập Địa chỉ Email',
            'class': 'form-control form-control-lg',
            'required': True,
            'data-validation': 'email',
            'pattern': '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,63}$',
            'data-validation-error-msg': 'Email sai định dạng',
        })
        super().__init__(*args, **kwargs)
        
class CustomPasswordInput(forms.PasswordInput):
    def __init__(self, *args, **kwargs):
        attrs = kwargs.setdefault('attrs', {})
        attrs.update({
            'placeholder': 'Nhập Mật khẩu',
            'class': 'form-control form-control-lg',
            'required': True,
            'data-validation': 'required',
            'data-validation-error-msg': 'Không được để trống',
        })
        super().__init__(*args, **kwargs)
        
class CustomRePasswordInput(forms.PasswordInput):
    def __init__(self, *args, **kwargs):
        attrs = kwargs.setdefault('attrs', {})
        attrs.update({
            'placeholder': 'Nhập Lại Mật khẩu',
            'class': 'form-control form-control-lg',
            'required': True,
            'data-validation': 'required',
            'data-validation-error-msg': 'Không được để trống',
        })
        super().__init__(*args, **kwargs)
        
class RegistrationForm(forms.Form):
    username = forms.CharField(label='Tài khoản', max_length=30, widget=CustomNameInput())
    email = forms.EmailField(label='Email', widget=CustomEmailInput())
    password1 = forms.CharField(label='Mật khẩu', widget=CustomPasswordInput())
    password2 = forms.CharField(label='Nhập lại mật khẩu', widget=CustomRePasswordInput())

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 == password2 and password1:
            return password2
        raise forms.ValidationError("Mật khẩu không khớp")

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError("Tên tài khoản có kí tự đặc biệt")
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("Tài khoản đã tồn tại")

    def save(self):
        User.objects.create_user(username=self.cleaned_data['username'], email=self.cleaned_data['email'], password=self.cleaned_data['password1'])
        


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Nhập UserName',
            'data-validation': 'required',
        })
        self.fields['password'].widget.attrs.update({
            'placeholder': 'Nhập Mật khẩu',
            'type': 'password',
            'data-validation': 'required'
        })
        
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username is not None and password:
            
            self.user_cache = authenticate(
                self.request, username=username, password=password
            )
            if self.user_cache is None:
                self.add_error(None, 'Tên người dùng hoặc mật khẩu không đúng.')
            else:
                
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data


            

    
    
    

        

    

            
        
  



