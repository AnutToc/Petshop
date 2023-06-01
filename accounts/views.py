from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from myapp.models import Customer

def register(request):
    print('Test')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save new user to database
            print(user)
            customer = Customer(id='2',name='anut',email='anut@gmail.com')
            customer.save()  # Save new customer to database
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
