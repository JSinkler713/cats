from django.shortcuts import render, redirect
# this allows us to interact with out Cat model in view functions
from .models import Cat
from .forms import CatForm, FeedingForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cats_index(request):
    cats = Cat.objects.all()
    return render(request, 'cats/index.html', { 'cats': cats })

# adds a view function for showing a single cat's data
def cats_detail(request, cat_id):
    # retrieve a cat from the DB using the ID
    cat_data = Cat.objects.get(id=cat_id)
    # instantiate a new FeedingForm to be rendered in the template
    feeding_form = FeedingForm()
    # return the detail template with the data for a signle cat
    return render(request, 'cats/detail.html', { 
        'cat': cat_data,
        'feeding_form': feeding_form 
    })
    # render takes arguments for the request, 
    # the template and the context



def add_feeding(request, cat_id):
    # create the ModelForm using the data in request.POST
    form = FeedingForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save it to DB until cat_id is assigned
        new_feeding = form.save(commit=False)
        new_feeding.cat_id = cat_id
        new_feeding.save()
    # the 'detail' in the redirect takes a path's name (from urls.py)
    # and sends the user to that page using the name
    return redirect('detail', cat_id=cat_id)


# When creating something in the database we need a combined view function like this one
# We call it combined because it handles both POST (or DELETE or PUT) and GET requests
def new_cat(request):
    # If a post request is made to this view function
    if request.method == 'POST':
        # We save the form data to a new variable
        form = CatForm(request.POST)
        # We make sure the data passes validations
        if form.is_valid():
            # If it does, save it in the database
            cat = form.save()
            # Redirect the user to the new cat's detail page
            return redirect('detail', cat.id)
    else:
        # If it's a get request, load the form from forms.py
        form = CatForm()
    # Save the form to a new variable
    context = { 'form': form }
    # Render the cat form template with the form
    return render(request, 'cats/cat_form.html', context)