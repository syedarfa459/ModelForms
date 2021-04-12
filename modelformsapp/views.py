from django.shortcuts import render, redirect
from .forms import AuthorForm
from .models import Author
# Create your views here.

def successpage(request):
    return render(request, 'success.html')


def index(request):

    if request.method == 'POST':
        authorform = AuthorForm(request.POST)
        if (authorform.is_valid()):

            authorform.save(commit=True)
            # authorname = authorform.cleaned_data['name']
            # authortitle = authorform.cleaned_data['title']
            # authorbirthdate = authorform.cleaned_data['birthdate']
            # authorbook = authorform.cleaned_data['bookname']
            # authorinstance = Author(authorname, authortitle, authorbirthdate, authorbook)
            print('Saved the data')

            return render(request, 'success.html')
    else:
        authorform = AuthorForm()

    return render(request, 'index.html', context={'authorform': authorform})

def home(request):
    return render(request, 'x.html')


