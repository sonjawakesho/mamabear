from django.forms import ModelForm
from pets.models import Pet

class PetForm(ModelForm):
	class Meta:
		model=Pet
		fields=['pet_type','type_of_breed','age','weight','colour','behaviour','name']
