from ssl import HAS_TLSv1_1
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from django.contrib.auth.models import User

from .models import Titan, Eldian
from .forms import FeedingForm

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')


# Add new view
def titans_index(request):
  #superusers = User.objects.filter(is_superuser=True)
  #print(superusers)
  titans = Titan.objects.all()

  return render(request, 'titans/index.html', { 'titans': titans })

def titans_detail(request, titan_id):
  titan = Titan.objects.get(id=titan_id)
  id_list = titan.eldians.all().values_list('id')
  eldians_titan_doesnt_have = Eldian.objects.exclude(id__in=id_list)
  feeding_form = FeedingForm()
  return render(request, 'titans/detail.html', { 'titan': titan, 'feeding_form': feeding_form, 'eldians': eldians_titan_doesnt_have })



def add_feeding(request, titan_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    # don't save the form to the db until it
    # has the titan_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.titan_id = titan_id
    new_feeding.save()
  return redirect('detail', titan_id=titan_id)

def assoc_eldian(request, titan_id, eldian_id):
  titan = Titan.objects.get(id=titan_id)
  titan.eldians.add(eldian_id)
  return redirect('detail', titan_id=titan_id)

def unassoc_eldian(request, titan_id, eldian_id):
  Titan.objects.get(id=titan_id).eldians.remove(eldian_id)
  return redirect('detail', titan_id=titan_id)



class TitanCreate(CreateView):
  model = Titan
  fields = ['name','power','description']

class TitanUpdate(UpdateView):
  model = Titan
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['power','description']

class TitanDelete(DeleteView):
  model = Titan
  success_url = '/titans/'



class EldianList(ListView):
  model = Eldian

class EldianDetail(DetailView):
  model = Eldian

class EldianCreate(CreateView):
  model = Eldian
  fields = '__all__'

class EldianUpdate(UpdateView):
  model = Eldian
  fields = ['name']

class EldianDelete(DeleteView):
  model = Eldian
  success_url = '/eldians/'