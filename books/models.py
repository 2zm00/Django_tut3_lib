from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Book(models.Model):
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=100)
	pub_date=models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.title
	def was_published_recently(self):
		return self.pub_date >= timezone.now()-datetime.timedelta(days=1)
	


class Review(models.Model):
	book = models.ForeignKey(Book, on_delete=models.CASCADE)
	review_text = models.TextField(max_length=255, blank=True)
	pub_date = models.DateTimeField(auto_now_add=True)