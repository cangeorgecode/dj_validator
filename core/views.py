from django.shortcuts import render, redirect
from core.forms import WaitingForm

def index(request):
    form = WaitingForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('success')
    return render(request, 'core/index.html', {'form': form})

def success(request):
    return render(request, 'core/success.html')
