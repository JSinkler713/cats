from django.shortcuts import render, redirect

# these imports are strictly for use with Class-based views
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

# this allows us to interact with out Cat and Toy models in view functions
from .models import Cat, Toy
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
    # get all toys that this cat does not have an association
    toys_cat_doesnt_have = Toy.objects.exclude(id__in = cat_data.toys.all().values_list('id')) # [2, 1, 3]
    # instantiate a new FeedingForm to be rendered in the template
    feeding_form = FeedingForm()
    # return the detail template with the data for a signle cat
    return render(request, 'cats/detail.html', { 
        'cat': cat_data,
        'feeding_form': feeding_form,
        'toys': toys_cat_doesnt_have 
    })
    # render takes arguments for the request, 
    # the template and the context

def assoc_toy(request, cat_id, toy_id):
    # The add method accepts both the whole model object or its ID for associations
    Cat.objects.get(id=cat_id).toys.add(toy_id)
    return redirect('detail', cat_id=cat_id)

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


def cats_update(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    
    if request.method == "POST":
        form = CatForm(request.POST, instance=cat)
        if form.is_valid():
            cat = form.save()
            return redirect('detail', cat.id)
    else: # if a GET request is made to this view function
        form = CatForm(instance=cat)
    return render(request, 'cats/cat_form.html', { 'form': form })


def cats_delete(request, cat_id):
    Cat.objects.get(id=cat_id).delete()
    return redirect('index')

#------------------------------------
# Class-based Views for the Toy model
#------------------------------------
# CBVs are great for getting basic CRUD functionality 
# up and running in a very short period of time. However,
# CBVs are not a coding pattern that you are likely to see
# in production Django apps. We used them here to free up 
# time for lessons. Read the documentation below to get a
# brief introduction CBVs.

# CBVs fall into 5 types: List, Detail, Create, Update, Delete
# Notice that each class below inherits from one of those 5 types

# List and Detail Views are the easiest to set up; all we need to 
# do is declare the model we want to build a view for.
# class ToyList(ListView):
  # This line associates the ListView with the Toy model
  # model = Toy

def toy_index(request):
    toys = Toy.objects.all()
    print(toys)
    return render(request, 'main_app/toy_list.html', { 'toys': toys })

class ToyDetail(DetailView):
  model = Toy

# The editable view types include Create, Update, and Delete
# They're also relatively easy to set up but require a little more work
class ToyCreate(CreateView):
  model = Toy
  # The CreateView requires a field property to set
  # Here we are saying that all fields associated with a Toy should 
  # be displayed in the form
  fields = '__all__'
  # This CBV will render the template toy_form.html  

class ToyUpdate(UpdateView):
  model = Toy
  # In the UpdateView we set the name and color fields as the only two in the form
  fields = ['name', 'color']
  # This CBV will render the template toy_form.html as well


class ToyDelete(DeleteView):
  model = Toy
  # The DeleteView requires a success_url be declared to redirect 
  # the user to when they successfully delete a toy
  success_url = '/toys/'
  # This CBV will render the toy_confirm_delete.html template