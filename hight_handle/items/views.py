from django.shortcuts import render, redirect
from .models import Item, ShapeItem, Category, Modality
from .forms import ItemForm, CategoryForm

# Create your views here.

def index (request):
    items = Item.objects.all ()

    context = {
        'items': items
    }

    return render (request, 'items/index.html', context)


def add (request):
    categories = Category.objects.all ()
    shapes = ShapeItem.objects.all ()
    modalities = Modality.objects.all ()

    form = ItemForm () 
    if request.method == 'POST':
        form = ItemForm (request.POST)
        if form.is_valid ():
            form.save ()
            return redirect ('items:index')

    context = {
        'form': form,
        'categories': categories,
        'shapes': shapes,
        'modalities': modalities
    }

    return render (request, 'items/add.html', context)


def edit (request, id):
    item = Item.objects.get (pk=id)
    
    categories = Category.objects.all ()
    shapes = ShapeItem.objects.all ()
    modalities = Modality.objects.all ()

    form = ItemForm (instance=item) 
    if request.method == 'POST':
        form = ItemForm (request.POST, instance=item)
        if form.is_valid ():
            form.save ()
            return redirect ('items:index')

    context = {
        'form': form,
        'categories': categories,
        'shapes': shapes,
        'modalities': modalities
    }

    return render (request, 'items/edit.html', context)


def remove (request, id):
    item = Item.objects.get (pk=id)
    item.delete ()

    return redirect ('items:index')


def category (request):
    categories = Category.objects.all ()

    context = {
        'categories': categories
    }

    return render (request, 'items/category.html', context)


def category_details (request):

    context = {
    }

    return render (request, 'items/category_details.html', context)


def category_add (request):
    form = CategoryForm ()

    if request.method == 'POST':
        form = CategoryForm (request.POST)
        if form.is_valid ():
            form.save ()
            return redirect ('items:category')

    context = {
        'form': form
    }

    return render (request, 'items/category_add.html', context)


def category_edit (request, id):
    category = Category.objects.get (pk=id)

    form = CategoryForm (instance=category) 
    if request.method == 'POST':
        form = CategoryForm (request.POST, instance=category)
        if form.is_valid ():
            form.save ()
            return redirect ('items:category')

    context = {
        'form': form
    }

    return render (request, 'items/category_edit.html', context)


def category_delete (request, id):
    category = Category.objects.get (pk=id)
    category.delete ()
    
    return redirect ('items:category')

def statistics (request):
    context = {

    }

    return render (request, 'items/statistics.html', context)