from django.shortcuts import render
from .forms import InputForm
from .home_bot import process_input

# Create your views here.


# def home(request):
#     return render(request, "tools/home.html", {})

def home(request):
    result = None
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data['user_input']
            result = process_input(user_input)  # Call your function here
    else:
        form = InputForm()
    
    return render(request, 'tools/home.html', {'form': form, 'result': result})