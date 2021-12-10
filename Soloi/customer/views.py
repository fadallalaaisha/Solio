from customer .models import Customer
from django.shortcuts import render
from .form import CustomerForm


def register_Customer(request):
    if request.method == 'POST':
        form=CustomerForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)    

    else:
            form=CustomerForm()

    return render(request,'Index.html', {"form":form})
    
