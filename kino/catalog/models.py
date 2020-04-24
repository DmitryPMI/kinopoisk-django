from django.db import models

# Create your models here.

class Film(models.Model):

	name = models.CharField(max_length=200, default='Название фильма')
	description = models.TextField()
	rate = models.FloatField()
	date = models.DateField()

	def show_less(self):
		if len(self.description) < 200:
			return self.description
		try:
			return ' '.join(self.description.split()[:30])
		except:
			return self.description

	def __str__(self):
		return self.name

class Type(models.Model):
	film = models.ForeignKey(Film, on_delete=models.CASCADE)
	boevik = models.BooleanField(default=False)
	drama = models.BooleanField(default=False)
	romantic = models.BooleanField(default=False)


# python manage.py makemigration
# python manage.py migrate
# django-admin shell