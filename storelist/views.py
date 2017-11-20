from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Stores
from .forms import Newstoreform
from django.shortcuts import redirect

def home(request):
    stores = Stores.objects.all()
    storeABClist = Stores.objects.order_by('storename')
    #return render(request, 'home.html', {'stores': stores})
    return render(request, 'home.html', {'storeABClist': storeABClist})

def store_list(request):
    stores = Stores.objects.all()
    return render(request, 'stores.html', {'stores': stores})

def storesbycategory(request):
    stores_food = Stores.objects.filter(category='Food')
    stores_travel = Stores.objects.filter(category='Travel')
    stores_electronic = Stores.objects.filter(category='Electronic')
    return render(request, 'storesbycategory.html', {'stores_food': stores_food,'stores_travel': stores_travel, 'stores_electronic': stores_electronic})

def new_store(request):
    form = Newstoreform()
    return render(request, 'new_store.html', {'form': form})

def new_store(request):
    if request.method == "POST":
        form = Newstoreform(request.POST)
        if form.is_valid():
            store = form.save(commit=False)
            store.save()

    else:
        form = Newstoreform()
    return render(request, 'new_store.html', {'form': form})
