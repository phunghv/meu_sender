from django.db import models

# Create your models here.

class PageView(models.Model):
    hostname = models.CharField(max_length=32)
    timestamp = models.DateTimeField(auto_now_add=True)


class Sender( models.Model ):
	mail = models.EmailField()
	name = models.CharField(max_length  = 20)
	api_key = models.CharField(max_length = 200)
	is_active = models.BooleanField()
	sended_count = models.IntegerField(default = 0)
	error_count  = models.IntegerField(default = 0)
	retry  = models.IntegerField(default = 5)

	def __str__(self):
		return self.name

class Receiver (models.Model):
	mail = models.EmailField()
	name = models.CharField(max_length = 20)
	status = models.IntegerField(default = 0)

	def __str__(self):
		return self.mail

class Email (models.Model):
	sender = models.ForeignKey(Sender)
	receiver = models.ForeignKey(Receiver)
	subject = models.TextField(default = '')
	content = models.TextField(default = '')
	date  = models.DateTimeField('date send')

	def __str__(self):
		return self.content

class History (models.Model):
	email = models.ForeignKey(Email)
	date = models.DateTimeField('date send')
	status = models.CharField(max_length=10)

	def __str__(self):
		return self.email + ':'+self.status
