from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required 
from pets.forms import PetForm
from .models import Pet
from django.http import HttpResponse

def signup(request):
	if request.method == 'POST':
		form= UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username= form.cleaned_data.get('username')
			raw_password= form.cleaned_data.get('password1')
			user= authenticate(username=username,password= raw_password)
			login(request,user)
			return redirect('home')
	else: 
		form=UserCreationForm()
	return render(request, 'signup.html',{'form':form})



def home(request): 
	eldest_pet_list= Pet.objects.order_by('-age')
	print (eldest_pet_list)
	context= {'eldest_pet_list':eldest_pet_list}
	return render(request,'home.html', context)


@login_required
def create_pet(request):
	if request.method == 'POST':
		form= PetForm(request.POST)
		form.save()
	else:
		form= PetForm()
	return render (request,'add_pet.html',{'form':form})

