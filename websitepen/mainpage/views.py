from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

import smtplib
import imghdr
from email.message import EmailMessage

def home(request):
	return render(request, 'mainpage/index.html')

def contactus(request):
	name = request.POST.get('name')
	emailid = request.POST.get('email')
	subject = request.POST.get('Subject')
	message = request.POST.get('Message')
	

	EMAIL_ADDRESS = 'email@gmail.com'
	EMAIL_PASSWORD = 'passwrod'

	msg = EmailMessage()
	msg['Subject'] = f'Contact Request from {name}'
	msg['From'] = emailid
	msg['To'] = 'emailgmail.com'

	msg.set_content(f'message : {message}')

	msg.add_alternative(f"""\
	<!DOCTYPE html>
	<html>
	    <body>
	        <h2 style="color:SlateGray;">This message is sent by {name}.</h2>
	        <h3>Subject : {subject}</h3>
	        <h3>From : {emailid}</h3>
	        <p style="font-size: large;">{message}</p>
	    </body>
	</html>
	""", subtype='html')


	with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
	    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
	    smtp.send_message(msg)

	return render(request, 'mainpage/index.html')


		
