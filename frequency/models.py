from django.db import models
class givenurl(models.Model):
	URL=models.CharField(max_length=1000)
	def __str__(self):
		return self.URL
class resulttable(models.Model):
	URL=models.ForeignKey(givenurl,on_delete=models.CASCADE)
	Keyword=models.CharField(max_length=100)
	wordfrequency=models.IntegerField()
	# Create your models here.
	def __str__(self):
		return self.Keyword
