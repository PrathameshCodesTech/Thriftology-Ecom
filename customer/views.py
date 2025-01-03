from django.shortcuts import render, redirect
from .forms import CustomerRegistrationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,"Welcome to Thriftology! Your account is successfully created. 🌟 Start exploring our unique, pre-loved pieces and embrace sustainable fashion. Happy thrifting! 🛍️")
            form.save()
            # return redirect('login')  # Redirect to login page after registration
    else:
        form = CustomerRegistrationForm()
    return render(request, 'customerRegistration.html', {'form': form})
