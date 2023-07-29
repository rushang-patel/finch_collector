from django.shortcuts import render

finches = [
  {'name': 'Rosey', 'breed': 'House Finch', 'description': 'Rose colored finch', 'age': 3},
  {'name': 'Feather', 'breed': 'Pine Siskin', 'description': 'Migratory bird', 'age': 2},
]

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
  return render(request, 'finches/index.html', {
    'finches': finches
  })
