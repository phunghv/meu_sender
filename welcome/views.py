import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.views.generic import ListView
from . import database
from .models import PageView, Sender, Receiver, History, Email

# Create your views here.
class HistoryList(ListView):
    model = Sender

def index(request):
    # hostname = os.getenv('HOSTNAME', 'unknown')
    # PageView.objects.create(hostname=hostname)

    # return render(request, 'welcome/index.html', {
    #     'hostname': hostname,
    #     'database': database.info(),
    #     'count': PageView.objects.count()
    # })
    senders = Sender.objects.all()
    receivers = Receiver.objects.all()
    histories = History.objects.all()
    return render(request,'welcome/home.html',{
                  'senders':senders,
                  'receivers':receivers,
                  'histories':histories
    })

def execute(request):
	#mesg = send_mail()
	return render(request,'welcome/execution.html')

def result(request):
	return HttpResponse("This is a view of result")

def send_mail():
	# using SendGrid's Python Library
	# https://github.com/sendgrid/sendgrid-python
	sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
	from_email = Email("from@email.com")
	to_email = Email("to@email.com")
	subject = "Sending with SendGrid"
	content = Content("text/plain", "and easy to do anywhere, even with Python")
	mail = Mail(from_email, subject, to_email, content)
	response = sg.client.mail.send.post(request_body=mail.get())
	print(response.status_code)
	print(response.body)
	print(response.headers)
	return response.body

def health(request):
    return HttpResponse(PageView.objects.count())
