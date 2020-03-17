from django.shortcuts import render, redirect
# this allows us to interact with out Cat model in view functions
from .models import Cat
from .forms import CatForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cats_index(request):
    cats = Cat.objects.all()
    return render(request, 'cats/index.html', { 'cats': cats })

def cats_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    return render(request, 'cats/detail.html', { 'cat': cat })

def new_cat(request):
    if request.method == 'POST':
        form = CatForm(request.POST)
        if form.is_valid():
            cat = form.save()
            return redirect('detail', cat.id)
    else:
        form = CatForm()
    context = { 'form': form }
    return render(request, 'cats/cat_form.html', context)