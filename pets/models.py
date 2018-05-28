from django.db import models
from django.utils import timezone
from datetime import datetime


class Pet(models.Model):
	PET_TYPE= (
		('CAT','cat'),
		('DOG','dog'),
		('BIRD','bird'),
		('COW','cow'),
		('GOAT','goat'),
		('REPTILE','reptile'),
		('PIG','pig'),)
	pet_type=models.CharField(max_length=5,choices=PET_TYPE)
	type_of_breed= models.CharField(max_length= 30)
	age=models.CharField(max_length=30, default='')
	weight=models.CharField(max_length=30,default='')
	colour=models.CharField(max_length=40)
	behaviour=models.CharField(max_length= 200)
	name=models.CharField(max_length=30,default='')
	gender=models.CharField(max_length=12,default='')
	location=models.CharField(max_length=30,default='') 


	def __str__(self):
		return self.name

	def is_old_currently(self):

		return self.age >=datetime.timedelta(months=7)

	class Meta:
			verbose_name_plural="Pets"
  



	