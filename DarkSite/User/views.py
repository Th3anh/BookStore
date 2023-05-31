from django.shortcuts import render
from .forms import RegistrationForm
from django.http import HttpResponseRedirect 
from .forms import CustomAuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required


class login_view(LoginView):
    form_class = CustomAuthenticationForm
    template_name = "User/login.html" 



def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'User/register.html', {'form': form})

